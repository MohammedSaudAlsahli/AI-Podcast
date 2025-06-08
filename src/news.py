from utils import Settings
from newsapi import NewsApiClient
from datetime import datetime, timedelta


class News:
    def __init__(
        self,
        newsapi: NewsApiClient,
        source: str = "bbc-news,cnn",
        language: str = "en",
        sort_by: str = "popularity",
        page: int = 1,
        page_size: int = 10,
    ):
        self.newsapi = newsapi
        self.__source = source
        self.__language = language
        self.__sort_by = sort_by
        self.__page = page
        self.__page_size = page_size

    def __all_articles(self):
        try:
            to = datetime.now().date()
            from_param = to - timedelta(days=7)

            articles = self.newsapi.get_everything(
                sources=self.__source,
                from_param=from_param,
                to=to,
                language=self.__language,
                sort_by=self.__sort_by,
                page=self.__page,
                page_size=self.__page_size,
            )

            return articles.get("articles", [])
        except Exception as e:
            print(f"Error fetching articles: {e}")
            return []

    def all_articles(self):
        return self.__all_articles()


if __name__ == "__main__":
    settings = Settings()
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    news = News(newsapi=newsapi)

    print(news.all_articles())
