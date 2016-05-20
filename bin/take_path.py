from tkinter import *

def take_path():

    # Initialisation fenêtre
    fenetre = Tk()
    champ_label = Label(fenetre, text="Entrer le chemin du dossier des images :")
    #affichage du label
    champ_label.pack()
    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetre.mainloop()
