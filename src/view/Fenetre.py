from tkinter import *

fenetre = Tk()

# Création de la barre des menu
menuBar = Menu(fenetre) 

fenetre.geometry("640x400")
 
# Création des menus principaux
menuArticles = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Articles", menu=menuArticles) 
 
# Création des sous menus
menuArticles.add_command(label="Nouveau") 
menuArticles.add_command(label="Quitter", command=quit) 

fenetre.config(menu=menuBar)

fenetre.mainloop()
