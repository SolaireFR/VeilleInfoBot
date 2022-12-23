import newsapi
from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient
from src.modele.News import News
from src.modele.NewsList import NewsList
from src.modele.Settings import Settings


def load_news_from_internet() -> NewsList:
    news_list = NewsList()

    newsapi_client = NewsApiClient(Settings.api_keys.get("NewsApi.org"))
    all_articles_newsapi = newsapi_client.get_top_headlines(category='technology',
                                                            language='fr')
    news_list.add_all(dict_newsapi_to_list_news(all_articles_newsapi))

    newsdata_client = NewsDataApiClient(Settings.api_keys.get("NewsData.io"))
    all_articles_newsdata = newsdata_client.news_api(language="fr", category="technology")
    news_list.add_all(dict_newsdata_to_list_news(all_articles_newsdata))

    return news_list

def dict_newsapi_to_list_news(all_articles: dict) -> list:
    list_news = []
    for news in all_articles.get("articles") :
        list_news.append(News(news.get("title"),
                              news.get("author"),
                              news.get("description"),
                              news.get("url"),
                              news.get("urlToImage"),
                              news.get("content"),
                              news.get("publishedAt")))
    return list_news

def dict_newsdata_to_list_news(all_articles: dict) -> list:
    list_news = []
    for news in all_articles.get("results") :
        list_news.append(News(news.get("title"),
                              news.get("creator"),
                              news.get("description"),
                              news.get("link"),
                              news.get("image_url"),
                              news.get("content"),
                              news.get("pubDate")))
    return list_news

def save_news_into_csv(news_list: list, path="../../res/NewsList.csv"):
    save_news_into_csv(news_list, path)


def load_news_from_csv(path="../../res/NewsList.csv") -> list:
    return load_news_from_csv(path)


def save_settings_into_csv(path="../../res/Settings.csv"):
    save_settings_into_csv(path)


def load_settings_from_csv(path="../../res/NewsList.csv") -> list:
    return load_settings_from_csv(path)