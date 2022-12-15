class News:
    max = 0

    def __init__(self, number: -1, title: str, author: str, description: str,
                 link: str, image_url: str, content: str, pub_date: str):
        self.number = number
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
        # number
        if self.number == -1:
            self.number = News.max
        News.max += 1

        # Content and description
        if self.description is None:
            self.description = "Vide"
        if self.content is None:
            self.content = "Vide"

