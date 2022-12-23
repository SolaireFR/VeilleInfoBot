# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *

# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()

# Ajout d'un titre à la fenêtre principale :
fenetre.title("Veille Info Bot")

# Définir un icone :
fenetre.iconbitmap("../../res/news.ico")

# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
fenetre.config(bg = "#ADD8E6")

# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("800x600")

# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.minsize(640,480)
fenetre.maxsize(800,600)

# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Ceci est un Label")
texte1.pack()

# Ajout d'un bouton dans la fenêtre :
bouton1 = Button (fenetre, text = "Cliquez ici")
bouton1.pack()

# Création d'un cadre dans la fenêtre :
cadre1 = Frame(fenetre)
cadre1.pack()
# Ajout de boutons dans le cadre :
bouton1 = Button (cadre1, text = "bouton1")
bouton2 = Button (cadre1, text = "bouton2")
bouton3 = Button (cadre1, text = "bouton3")
bouton1.pack()
bouton2.pack()
bouton3.pack()

# Création d'un champ de saisie de l'utilisateur dans la fenêtre :
entrée1 = Entry (fenetre)
entrée1.pack()

# Création des cases à cocher "Checkbutton" dans la fenêtre :
case_cocher1 = Checkbutton (fenetre, text = "choix 1")
case_cocher2 = Checkbutton (fenetre, text = "choix 2")
case_cocher3 = Checkbutton (fenetre, text = "choix 3")
case_cocher1.pack()
case_cocher2.pack()
case_cocher3.pack()

# Création des cases à cocher "Radiobutton" dans la fenêtre :
case_cocher1 = Radiobutton (fenetre, text = "choix 1")
case_cocher2 = Radiobutton (fenetre, text = "choix 2")
case_cocher3 = Radiobutton (fenetre, text = "choix 3")
case_cocher1.pack()
case_cocher2.pack()
case_cocher3.pack()

# Création d'une liste dans la fenêtre :
# la méthode insert() sert à inserer des valeur à la liste :
liste1 = Listbox (fenetre)
liste1.insert(1, "valeur 1")
liste1.insert(2, "valeur 2")
liste1.insert(3, "valeur 3")
liste1.insert(4, "valeur 4")
liste1.pack()

# Création d'un Spinbox dans la fenêtre :
liste1 = Spinbox (fenetre)
liste1.pack()

# Création d'une barre de menu dans la fenêtre :
menu1 = Menu(fenetre)
menu1.add_cascade(label="sec1 Fichier")
menu1.add_cascade(label="sec2 Options")
menu1.add_cascade(label="sec3 Aide")
# Configuration du menu dans la fenêtre
fenetre.config(menu = menu1)

# Affichage de la fenêtre créée :
fenetre.mainloop()