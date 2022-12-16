import unittest
from src.modele.GestionnaireCSV import *
from src.modele.NewsList import NewsList


class TestArticle(unittest.TestCase):

    def test_create_a_news(self):
        news_1 = News("title1", "author1", "description1", "link1", "image_url1", "content1", "pub_date1")
        self.assertEqual("title1", news_1.title)

    def test_create_list_news(self):
        news_list = NewsList()
        news_list.append_news(News("title1", "author1", "description1", "link1",
                                   "image_url1", "content1", "pub_date1"))
        news_list.append_news(News("title2", "author2", "description2", "link2",
                                   "image_url2", "content2", "pub_date2"))
        self.assertEqual(2, news_list.len)
        print(news_list.articles)
        self.assertEqual(1, news_list.articles[1].number)

    def test_create_csv_with_list(self):
        news_1 = News("title1", "author1", "description1", "link1", "image_url1", "content1", "pub_date1")
        news_2 = News("title2", "author2", "description2", "link2", "image_url2", "content2", "pub_date2")
        list_news = [news_1, news_2]
        save_news_into_csv(list_news)

    def test_load_csv(self):
        list_news = load_news_from_csv("../../res/TestNewsList.csv")
        self.assertEqual(2, len(list_news))
        self.assertEqual("title1", list_news[0].title)


if __name__ == '__main__':
    unittest.main()
