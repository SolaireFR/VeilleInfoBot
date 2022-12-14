# **VEILLE_INFO_BOT**
Par Morgan S

Début : 08/12/2022

## NEWSAPI.ORG

### CATEGORIES :
- h
- h
- h
- h
- h

```python
from newsapi import NewsApiClient

print("Hello world")

# Init
newsapi = NewsApiClient(api_key='7f7dca4824124b3a8bfc499ee1ac427d')

# /v2/everything
all_articles = newsapi.get_everything(q='technology',
                                      from_param='2022-12-01',
                                      to='2022-12-08',
                                      language='fr')
```

>{   
>    'status': 'ok', 
> 
>    'totalResults': 119, 
> 
>    'articles': 
>    [
>        {
>
>            'source': {
>            'id': 'hacker-news', 
>            'name': 'Hacker News'
>            }, 
>            'author': None, 
>            'title': 'Odiggo (YC S21) Hardware Startup – Looking for Tech Co-Founder', 
>            'description': 'Comments', 
>            'url': 'https://news.ycombinator.com/item?id=33886973', 
>            'urlToImage': None, 
>            'publishedAt': '2022-12-06T21:01:00Z', 
>            'content': 'We are on a mission to fundamentally transform the way humans interact with the world around them through an extended reality glasses, using the latest advancements in technology to improve the lives… [+981 chars]'
>            }, 
>        {
>            'source':


## NEWSDATA.IO

- 200 = Successful operation
- 400 = Parameter missing
- 401 = Unauthorized
- 403 = CORS policy failed. IP/Domain restricted
- 409 = Parameter duplicate
- 415 = Unsupported type
- 422 = Unprocessable entity
- 429 = Too many requests
- 500 = Internal server error

### CATEGORIES :
- h
- h
- h
- h
- h

```python
from newsdataapi import NewsDataApiClient


# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey='pub_14335257c88334563a6d6035196c3c7d8e917')


# News API
response = api.news_api(category="technology,science",
                        country="fr",
                        language="fr,en")

# Archive API
response = api.archive_api()
print(response)


# Sources API
response = api.sources_api()
print(response)

# Crypto API
response = api.crypto_api()
print(response)
```

> ['status': 'success', 
> 
> 'totalResults': 107290, 
> 
> 'results': [
> 
>    {
> 
>        'title': 'Журналисты подтвердили гибель 10 тысяч российских военных в Украине', 
>        'link': 'https://haqqin.az/news/268325', 
>        'keywords': None, 
>        'creator': None, 
>        'video_url': None, 
>        'description': 'Русская служба BBC, «Медиазона» и волонтеры по открытым источникам подтвердили гибель 10 002 российских военнослужащих в Украине. Это данные на 9 декабря. Среди погибших — 430 мобили...', 
>        'content': None, 
>        'pubDate': '2022-12-09 14:05:00', 
>        'image_url': None, 
>        'source_id': 'haqqin', 
>        'country': ['Azerbaijan'], 
>        'category': ['top'], 
>        'language': 'Azerbaijani'
>    }, 
>    {
> 
>        'title': ... ]]