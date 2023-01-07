from tkinter import *
from src.controller.Controller import *
from src.modele.NewsList import NewsList
from src.modele.Settings import Settings


class Window:

    def __init__(self):
        self.listNews = NewsList()
        self.settings = Settings()
        self.screen = Tk()

        self.menuBar = Menu(self.screen)
        # Création des menus principaux
        self.menuArticles = Menu(self.menuBar, tearoff=0)

        self.buttonOpen = Button(self.screen, text="Ouvrir Selection", command=self.show_article_data)

        self.listBox = Listbox(self.screen, width=120, height=23, font=('Times', 14))

    def launch(self):
        self.buttonOpen.pack()
        self.menuBar.add_cascade(label="Articles", menu=self.menuArticles)
        self.menuArticles.add_command(label="Télecharger", command=self.download)
        self.menuArticles.add_command(label="Quitter", command=quit)
        self.screen.config(menu=self.menuBar)
        #self.screen.attributes('-fullscreen', True)

        self.screen.mainloop()

    def reload_news(self):
        self.listBox.delete(0, END)
        pair = False
        color = "#EDEDED"
        for i in range(self.listNews.len):
            self.listBox.insert(i, self.listNews.articles[i].to_str())
            self.listBox.itemconfig(i, {'bg': color})
            if pair:
                color = "#EDEDED"
            else:
                color = "#D0D0D0"
            pair = not pair
        self.listBox.pack()

    def download(self):
        self.listNews = load_news_from_internet()
        self.reload_news()

    def show_article_data(self):
        print("--data--")
        liste = self.listBox.curselection()
        print(len(liste), " ", liste)


if __name__ == '__main__':
    window = Window()
    window.launch()
