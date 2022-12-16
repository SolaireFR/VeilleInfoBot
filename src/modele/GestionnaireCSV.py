import pandas
import csv
from src.modele.News import News

def save_news_into_csv(news_list: list, path="../../res/NewsList.csv"):
    with open(path, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for news in news_list:
            writer.writerow(
                (news.title, news.author, news.description,
                 news.link, news.image_url, news.content, news.pub_date))


def load_news_from_csv(path="../../res/NewsList.csv") -> list:
    list_news = []
    with open(path) as stream:
        reader = csv.reader(stream)
        reader.__next__()
        for row in reader:
            if row.__len__() == 7:
                list_news.append(News(*row))
    return list_news


def load_newsdata() -> dict:
    return load_dict_from_csv("saveNewsData.csv")


def load_dict_from_csv(file_name: str) -> dict:
    return pandas.read_csv(file_name).to_dict()
