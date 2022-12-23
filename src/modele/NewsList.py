from src.modele.News import News


class NewsList:
    def __init__(self):
        self.len = 0
        self.articles = []

    # Method
    def append_news(self, news: News):
        news.number = self.len
        self.articles.append(news)
        self.len += 1

    def add_all(self, list_news: list):
        for news in list_news:
            self.append_news(news)
