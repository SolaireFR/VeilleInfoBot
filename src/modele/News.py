from newsdataapi import NewsDataApiClient

class News:
    def __init__(self, article):
        self.title = article["title"]
        self.link = article["link"]
        self.keywords = article["keywords"]
        self.creator = article["creator"]
        self.videoURL = article["video_url"]
        self.description = article["description"]
        self.content = article["content"]
        self.pubDate = article["pubDate"]
        self.imageURL = article["image_url"]
        self.sourceID = article["source_id"]
        self.country = article["country"]
        self.category = article["category"]
        self.language = article["language"]
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
    
    
