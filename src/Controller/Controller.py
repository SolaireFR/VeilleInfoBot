
from ArticleList import ArticleList
from newsapi import NewsApiClient

# API key authorization, Initialize the client with your API key


# News API
response = get_api().news_api(category="technology,science",
                        country="fr",
                        language="fr,en")

print("\nNOMBRE DE RESULTATS :", response["totalResults"], "\n")

articleList = ArticleList(response)
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