from newsapi import NewsApiClient
from datetime import datetime, timedelta


class News:
    def __init__(
        self,
        newsapi: str,
        source: str = "bbc-news,cnn",
        language: str = "en",
        sort_by: str = "popularity",
        page: int = 1,
        page_size: int = 50,
    ):
        self.newsapi = NewsApiClient(api_key=newsapi)
        self.__source = source
        self.__language = language
        self.__sort_by = sort_by
        self.__page = page
        self.__page_size = page_size

    def __get_date_range(self):
        today = datetime.now().date()
        last_saturday = today - timedelta(days=today.weekday() + 2)
        next_friday = last_saturday + timedelta(days=6)

        return last_saturday, next_friday

    def __all_articles(self):
        try:
            from_date, to_date = self.__get_date_range()
            articles = self.newsapi.get_everything(
                sources=self.__source,
                from_param=from_date,
                to=to_date,
                language=self.__language,
                sort_by=self.__sort_by,
                page=self.__page,
                page_size=self.__page_size,
            )

            return articles.get("articles", [])
        except Exception as e:
            print(f"Error fetching articles: {e}")

            return []

    def articles(self):
        return self.__all_articles()
