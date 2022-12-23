from tkinter import *

from src.controller.Controller import *
from src.modele.NewsList import NewsList
from src.modele.Settings import Settings

class Fenetre:

    def __init__(self):
        self.list_news = NewsList()
        self.settings = Settings()
        self.fenetre = Tk()
        self.fenetre.geometry("640x400")

        self.menuBar = Menu(self.fenetre)
        # Création des menus principaux
        self.menuArticles = Menu(self.menuBar, tearoff=0)

        self.listeBox = Listbox(self.fenetre, width=100, height=23, font=('Times', 14))

    def lancement(self):
        self.menuBar.add_cascade(label="Articles", menu=self.menuArticles)
        self.menuArticles.add_command(label="Télecharger", command=self.telecharger())
        self.menuArticles.add_command(label="Quitter", command=quit)
        self.fenetre.config(menu=self.menuBar)

        self.fenetre.mainloop()

    def reload_news(self):
        self.listeBox.delete(0, END)
        pair = False
        color = "#bffff3"
        for i in range(self.list_news.len) :
            self.listeBox.insert(i, self.list_news.articles[i].to_str())
            self.listeBox.itemconfig(i, {'bg': color})
            if pair :
                color = "#d4fffe"
            else :
                color = "#d4d8ff"
            pair = not pair
        self.listeBox.pack()

    def telecharger(self):
        self.list_news = load_news_from_internet()
        self.reload_news()

if __name__ == '__main__':
    fenetre = Fenetre()
    fenetre.lancement()