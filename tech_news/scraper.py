import requests
import time
from parsel import Selector


def fetch(url: str, wait: int = 3) -> str:
    try:
        headers = {"user-agent": "Fake user-agent"}
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=wait)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


def scrape_novidades(html_content: str) -> list:
    selector = Selector(html_content)
    news_links = selector.css(".cs-overlay-link::attr(href)").getall()

    return news_links


def scrape_next_page_link(html_content: str) -> list:
    selector = Selector(html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
