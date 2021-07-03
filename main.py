
from classes.ArgsParse import ParseArgs
from classes.CommandArgs import CommandArgs
from classes.Scraper import Scraper
from db.init import engine, Session, Base

from db.models.article import Article, ArticleSchema


def init_db():
    Base.metadata.create_all(engine)


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
    article_found = session.query(Article).filter(Article.title==title).first()
    session.close()
    return article_found

def get_default_command_args():
    url_arg = CommandArgs(["-u", "--url"], str,
                          help="url to scrape",
                          default="https://finance.yahoo.com/topic/stock-market-news"
                          )
    return [url_arg]


def main():
    argsParser = ParseArgs(get_default_command_args())
    args = argsParser.get_args()
    init_db()
    scraper = Scraper(args.url)
    articles = scraper.get_articles_list()
    insert_articles_to_db(articles)
    get_all_articles()


if __name__ == '__main__':
    main()
