from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def analyzer_menu_get_tech_news():
    amount = input("Digite quantas notícias serão buscadas:")
    print(get_tech_news(int(amount)))


def analyzer_menu_search_by_title():
    title = input("Digite o título:")
    print(search_by_title(title))


def analyzer_menu_search_by_date():
    title = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(title))


def analyzer_menu_search_by_tag():
    title = input("Digite a tag:")
    print(search_by_tag(title))


def analyzer_menu_search_by_category():
    title = input("Digite a categoria:")
    print(search_by_category(title))


def analyzer_menu_top_5_news():
    print(top_5_news())


def analyzer_menu_top_5_categories():
    print(top_5_categories())


def analyzer_menu():
    """Seu código deve vir aqui"""
