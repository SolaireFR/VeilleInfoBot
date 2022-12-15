
class News:
    number = 0

    def __init__(self, title, author, description, link, image_url, content, pub_date):
        self.id = News.number
        News.number += 1
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.image_url = image_url
        self.content = content
        self.pub_date = pub_date
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
    
    
