from newsapi import NewsApiClient
from datetime import datetime, timedelta
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class News:
    def __init__(
        self,
        newsapi_key: str,
        source: str = "bbc-news,cnn",
        language: str = "en",
        sort_by: str = "popularity",
        page: int = 3,
        page_size: int = 30,
    ):
        """
        Initialize News object for fetching news from NewsAPI.
        """

        try:
            self.newsapi = NewsApiClient(api_key=newsapi_key)
        except Exception as e:
            logging.error(f"Failed to initialize NewsApiClient: {e}")
            raise
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
        """
        Fetch articles using the News API within the calculated date range.
        """
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
            logging.error(f"Error fetching articles: {e}")

            return []

    def articles(self):
        """
        Public method to retrieve articles.
        """
        return self.__all_articles()
