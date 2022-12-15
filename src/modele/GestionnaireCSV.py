import pandas
import csv

#----------------------------------------------------------------------------

def save_news_into_csv(news_list: list):
    data_frame = pandas.DataFrame(news_list)
    data_frame.to_csv("res/NewsList.csv")

def save_news_into_csv(news_list: list):
    with open('res/NewsList.csv', 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Link'])
        for news in news_list:
            writer.writerow([news.id, 
                             news.title, 
                             news.author, 
                             news.description, 
                             news.link, 
                             news.image_url, 
                             news.content, 
                             news.pub_date])
    
#-----------------------------------------------------------------------------
    
def load_news_from_csv() -> list:
    return load_dict_from_csv("saveNewsApi.csv")

#-----------------------------------------------------------------------------
  
def load_newsdata() -> dict:
    return load_dict_from_csv("saveNewsData.csv")

#-----------------------------------------------------------------------------
  
def load_dict_from_csv(file_name: str) -> dict:
    return pandas.read_csv(file_name).to_dict()
    
#-----------------------------------------------------------------------------
    