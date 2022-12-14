from ArticleApi import ArticleApi
from News import ArticleData


class ArticleList:
    def __init__(self, articles_api, articles_data):
        self.status_api = articles_api["status"]
        self.status_data = articles_data["status"]
        self.totalResults = articles_data["totalResults"]
        self.articles = self.articles_dict_to_list(articles_data["results"])

    # Méthodes
    def articles_dict_to_list(self, all_articles):
        listArticles = []
        for i in range(len(all_articles)):
            listArticles.append(Article(all_articles[i]))
        return listArticles
    
    def print_all_titles(self):
        for i in range(len(self.articles)):
            print(self.articles[i].title,"\n")

    def print_nb_articles(self, number):
        if number > len(self.articles) :
            number = len(self.articles)
        
        elif number < 0 :
            number = 0
        
        for i in range(number):
            print("---" ,self.articles[i].title, "---")
            print("[", self.articles[i].link, "]")
            print(self.articles[i].content,"\n")