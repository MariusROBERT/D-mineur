#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *


#Variables
cote = 10
minesmax = 20
minestrouvees = 0
mines = 0
fichiermap = "map.txt"
texte = ""
mineautour = 0
casestestees = 0

#Fenetre Principale
Fenetre = Tk()


#Classe pour les boutons

class boutons:

    def __init__(self, ligne, colonne):
        self.ligne = ligne
        self.colonne = colonne

    def creation(self):
        Button(Fenetre, text = "     ", command = lambda:check(self.ligne, self.colonne)).grid(row = self.ligne, column = self.colonne)
        #if texte[ligne+cote*colonne] == "1":
        #    bombe = True




#Génération Mines
def generation():
    global texte, mines
    #mapd = open(fichiermap, "w")
    """for i in range(cote):
        for j in range(cote):
            texte += "0"
    """
        #texte += "\n"
    texte = str(cote*cote * "0")



    while mines < minesmax: #Tant qu'il n'y a pas assez de mines
        caractere = randint(0, cote*cote) #Emplacement aléatoire
        if texte[caractere-1] == "0": #Met une mine si y'en a pas déjà une
            texte = texte[:caractere] + "1" + texte[caractere+1:]
            mines += 1


def check(ligne, colonne):
    global mineautour, texte, casestestees
    #texte2 = texte
    """
    for l in range(cote):
        texte2 = texte2[:cote*l] + "00" + texte2[cote*l+1:]
    texte2 = "0"+texte2+"0"
    """
    if texte[ligne+cote*colonne] == "1":
        print("perdu")
        showerror("Perdu", "Vous êtes tombé sur une mine, vous aurez peut-être plus de chance la prochaine fois")
        Button(Fenetre, text = "  X  ").grid(row = ligne, column = colonne)

    else:
        for i in range(-1,2):
            for j in range(-1,2):
                if ligne+i+cote*(colonne+j) <= 0 or ligne+i+cote*(colonne+j) > len(texte):
                    pass
                elif texte[ligne+i+cote*(colonne+j)] == "1":
                    mineautour +=1

        Button(Fenetre, text = "  "+ str(mineautour) +"  ").grid(row = ligne, column = colonne)
        mineautour = 0 #Reset du nombre de mines pour les autres boutons
        if casestestees + mines == cote^2:
            showinfo("Gagné !", "Vous avez trouvé toutes les mines")


def remplissage():
    """
    for i in range(cote):
        for j in range(cote):
            Button(Fenetre, text = "     ", command = lambda:check(grid_info()['row'], grid_info()['column'])).grid(row = i, column = j)
    """
    for i in range(cote):
        for j in range(cote):
            bouton = boutons(i, j)
            bouton.ligne = i
            bouton.colonne = j
            bouton.creation()





generation()
remplissage()
Fenetre.mainloop()
