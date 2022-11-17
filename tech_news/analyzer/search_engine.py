from tech_news.database import find_news
import datetime


def search_by_title(title):
    notices = find_news()
    response = []

    for notice in notices:
        if title.upper() in notice["title"].upper():
            response.append((notice["title"], notice["url"]))

    return response


def search_by_date(date):
    notices = find_news()
    response = []

    try:
        bool(datetime.datetime.strptime(date, "%Y-%m-%d"))
    except ValueError:
        raise ValueError("Data inválida")

    for notice in notices:
        formatted_date = datetime.datetime.strptime(
            notice["timestamp"], "%d/%m/%Y"
        ).date()

        if date == str(formatted_date):
            response.append((notice["title"], notice["url"]))

    return response


def search_by_tag(tag):
    notices = find_news()
    response = []

    for notice in notices:
        for tag_notice in notice["tags"]:
            if tag.upper() in tag_notice.upper():
                response.append((notice["title"], notice["url"]))

    return response


def search_by_category(category):
    notices = find_news()
    response = []

    for notice in notices:
        if category.upper() in notice["category"].upper():
            response.append((notice["title"], notice["url"]))

    return response
