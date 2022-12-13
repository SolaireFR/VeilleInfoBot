

class Article:
    def __init__(self, article):
        self.source_id = article["source"]["id"]
        self.source_name = article["source"]["name"]
        self.author = article["author"]
        self.title = article["title"]
        self.description = article["description"]
        self.url = article["url"]
        self.url_to_image = article["urlToImage"]
        self.published_at = article["publishedAt"]
        self.content = article["content"]
        self.initialise()
    

    # Méthodes
    def initialise(self):
        if self.content == None and self.description != None :
            self.content = self.description
        
        elif self.description == None and self.content != None :
            max = 255
            if max > len(self.content) :
                max = len(self.content)
                
            self.description = self.content[0:max]
        
        elif len(self.content) < len(self.description) :
            self.content = self.description + " " + self.content
    
    def get_api():
        return NewsDataApiClient(apikey='pub_14335257c88334563a6d6035196c3c7d8e917')
