from tkinter import *
from tkinter.filedialog import askdirectory
import os

directory_name = ""

def folder_name():
    global directory_name, label_directory_path
    directory_name = askdirectory()

def fenetre():
    # Initialisation fenêtre
    fenetre = Tk()
    fenetre.wm_title("Image Resize")

    champ_label_path = Label(fenetre, text="Sélectionner votre répertoire \
    contenant les images ")
    champ_label_path.pack()

    recherche_dossier = Button(fenetre, text="Parcourir", command=folder_name)
    recherche_dossier.pack()

    #label_directory_path = Label(fenetre, text=directory_name)
    #label_directory_path.pack()

    bout_quit=Button(fenetre, text='Quitter', command = fenetre.destroy)
    bout_quit.pack()
    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetre.mainloop()
