import pandas

#----------------------------------------------------------------------------

def save_newsapi(data_dict: dict):
    save_dict_to_csv(data_dict, "saveNewsApi.csv")
    
def save_newsapi(data_dict: dict):
    save_dict_to_csv(data_dict, "saveNewsData.csv")

def save_dict_to_csv(data_dict: dict, file_name: str):
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv(file_name)
    
#-----------------------------------------------------------------------------
    
def load_newsapi() -> dict:
    return load_dict_from_csv("saveNewsApi.csv")

def load_newsdata() -> dict:
    return load_dict_from_csv("saveNewsData.csv")
    
def load_dict_from_csv(file_name: str) -> dict:
    return pandas.read_csv(file_name).to_dict()
    
    