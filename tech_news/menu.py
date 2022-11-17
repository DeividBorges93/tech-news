import sys
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
    displays_the_options = {
        "0": lambda: analyzer_menu_get_tech_news(),
        "1": lambda: analyzer_menu_search_by_title(),
        "2": lambda: analyzer_menu_search_by_date(),
        "3": lambda: analyzer_menu_search_by_tag(),
        "4": lambda: analyzer_menu_search_by_category(),
        "5": lambda: analyzer_menu_top_5_news(),
        "6": lambda: analyzer_menu_top_5_categories(),
        "7": lambda: print("Encerrando script"),
    }

    options_answer = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    try:
        displays_the_options[options_answer]()
    except KeyError:
        print(sys.stderr.write("Opção inválida\n"))
