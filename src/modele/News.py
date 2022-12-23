class News:
    def __init__(self, title, author, description,
                 link, image_url, content, pub_date):
        self.number = 0
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.image_url = image_url
        self.content = content
        self.pub_date = pub_date
        self.initialise()

    # Methods
    def initialise(self):
        # Content and description
        if self.description is None:
            self.description = "Vide"
        if self.content is None:
            self.content = "Vide"

    def to_str(self) -> str:
        return ""+self.title+" : "+self.pub_date+"\n"

