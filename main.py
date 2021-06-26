from bs4 import BeautifulSoup
import requests
from db.init import engine, Session, Base

from db.models.article import Article, ArticleSchema


def init_db():
    Base.metadata.create_all(engine)

def get_articles_list():
    res = requests.get("https://finance.yahoo.com/topic/stock-market-news")
    soup = BeautifulSoup(res.text, "html.parser")

    news_articles = soup.findAll(name="div", class_="Cf")
    articles = []

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


def insert_articles_to_db(articles):
    session = Session()
    for article_dict in articles:
        if not get_article_by_title(article_dict.get("title", "")):
            new_article = Article(article_dict.get("title", ""), article_dict.get("link", ""), article_dict.get("paragraph", ""))
            session.add(new_article)
            session.commit()
    session.close()


def get_all_articles():
    session = Session()
    articles = session.query(Article).all()
    for article_row in articles:
        schema = ArticleSchema()
        print(schema.dumps(article_row))
    session.close()


def get_article_by_title(title):
    session = Session()
    article_found = {
        session.query(Article)
        .filter(Article.title==title)
        .first()
    }
    session.close()
    return article_found

if __name__ == '__main__':
    articles_list = get_articles_list()
    init_db()
    insert_articles_to_db(articles_list)
    get_all_articles()
