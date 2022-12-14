from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key
newsdata_key = NewsDataApiClient(apikey='pub_14335257c88334563a6d6035196c3c7d8e917')
newsapi_key = NewsApiClient("7f7dca4824124b3a8bfc499ee1ac427d")

response_newsapi = newsapi_key.news_api(category="technology,science",
                        language="fr,en")

print("\nNOMBRE DE RESULTATS :", response_newsapi = newsapi_key.news_api(category="technology,science",
["totalResults"], "\n")

articleList = ArticleList(response_newsapi = newsapi_key.news_api(category="technology,science",
)
articleList.print_nb_articles(3)

#########################

print("Hello world")

# Init
newsapi = NewsApiClient(api_key='7f7dca4824124b3a8bfc499ee1ac427d')

# /v2/everything
all_articles = newsapi.get_everything(q='technology',
                                      from_param='2022-12-01',
                                      to='2022-12-08',
                                      language='fr')

print(all_articles)

articleList = ArticleList(all_articles)
articleList.print_nb_articles(1)
#articleList.print_all_titles()

import requests

"""content = requests.get("https://newsapi.org/v2/top-headlines?language=fr&source=techcrunch&apiKey=7f7dca4824124b3a8bfc499ee1ac427d")
print(content.text, "\n")
"""