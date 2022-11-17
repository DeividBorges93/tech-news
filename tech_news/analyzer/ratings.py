from tech_news.database import get_collection


def top_5_news():
    news_collection = get_collection()

    five_news = list(
        news_collection.find(
            {},
            {
                "_id": False,
                "title": True,
                "url": True,
                "comments_count": True,
            },
        )
        .sort("comments_count", -1)
        .limit(5)
    )

    five_formatted_news = []

    for notice in five_news:
        five_formatted_news.append((notice["title"], notice["url"]))

    return five_formatted_news


def top_5_categories():
    news_collection = get_collection()

    ranking_categories = list(
        news_collection.aggregate(
            [
                {
                    "$group": {
                        "_id": "$category",
                        "count": {"$sum": 1},
                    },
                },
                {"$sort": {"count": -1, "_id": 1}},
            ]
        )
    )

    categories = []

    for notice in ranking_categories:
        categories.append(notice["_id"])

    return categories
