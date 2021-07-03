from bs4 import BeautifulSoup
import requests

from classes.validators.urlValidator import urlValidator

class Scraper:

    def __init__(self, url):

        self.url = url if self.is_valid_url(url) else ''

    def is_valid_url(self, url):
        validator = urlValidator(url)
        return validator.validate()

    def get_articles_list(self):
        articles = []
        if not self.url:
            return articles
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, "html.parser")
        news_articles = soup.findAll(name="div", class_="Cf")

        for article in news_articles:
            link = article.find(name="a")
            link_text = link.getText()
            link_href = link.get("href")
            extended_text = ''
            if paragraph := article.find(name="p"):
                extended_text = paragraph.getText()

            article_dict = {"title": link_text, "link": link_href, "paragraph": extended_text}
            articles.append(article_dict)

        return articles