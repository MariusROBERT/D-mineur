#!/usr/bin/env python3
# -- coding: utf-8 --

#test12

# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *


#Variables
cote = 20
minesmax = 25
minestrouvees = 0
mines = 0
mineautour = 0
casestestees = 0
map = []
#Map des cases testé pour pas faire une boucle
maptest = []

#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Démineur by Marius")



#Classe pour les boutons

class boutons:

    def __init__(self, ligne, colonne):
        self.ligne = ligne
        self.colonne = colonne
        #self.couleur = couleur

    def creation(self):
        Button(Fenetre, text = "     ", command = lambda:check(self.ligne, self.colonne), relief = RAISED).grid(row = self.ligne, column = self.colonne)
        #if texte[ligne+cote*colonne] == "1":
        #    bombe = True




#Génération Mines
"""def generation():
    global texte, mines
    for i in range(cote):
        map.append([])
        maptest.append([])
        for j in range(cote):
            map[i].append(0)
            maptest[i].append(0)"""


def generation():
    global texte, mines
    for i in range(cote+4):
        map.append([])
        maptest.append([])
        for j in range(cote+4):
            map[i].append(0)
            maptest[i].append(0)

    #ajout d'un double contour, 1 plein et 1 vide pour éviter erreur "out of range" lors de comparaison pour mines autour
    for i in range(cote+4):
        map[0][i] = 1
        map[cote+3][i] = 1
        map[i][0] = 1
        map[i][cote+3] = 1


    while mines < minesmax: #Tant qu'il n'y a pas assez de mines
        aleatoire = randint(0, cote-1) #Emplacement aléatoire
        aleatoire2 = randint(0, cote-1)
        if map[aleatoire+2][aleatoire2+2] == 0: #Met une mine si y'en a pas déjà une
            map[aleatoire+2][aleatoire2+2] = 1
            mines += 1


def check(ligne, colonne):
    global mineautour, texte, casestestees
    print("check    ",ligne, "    ", colonne)
    #Mémorisation des cases testées
    maptest[ligne][colonne] = 1

    #test si bombe
    if map[ligne][colonne] == 1:
        print("perdu")
        showerror("Perdu", "Vous êtes tombé sur une mine, vous aurez peut-être plus de chance la prochaine fois") #Perdu
        Label(Fenetre, text = "  X  ", fg = "red").grid(row = ligne, column = colonne) #affichage X sur la bombe
    #si pas bombe
    else:
        for x in range(-1,2):
            for y in range(-1,2): #Test bombe 3x3 autour
                if ligne+x >= cote+1 or colonne+y >= cote+1 or ligne+x < 2 or colonne+y < 2: #Pour pas dépasser de la map
                    pass

                elif map[ligne+x][colonne+y] == 1: #Ajout de 1 a mineautour si bombe autour
                    mineautour += 1


        #Check autour si 0 mines autour
        if mineautour == 0:
            for x in range(-1,2):
                for y in range (-1,2):
                    #print(str(ligne+x) + "     " + str(colonne+y))
                    if ligne+x >= cote+1 or colonne+y >= cote+1 or ligne+x < 2 or colonne+y < 2: #Pour pas dépasser de la map
                        pass

                    elif maptest[ligne+x][colonne+y] == 0: #Check encore si toujours 0 mines autour et case pas déjà testée
                        check(ligne+x,colonne+y)


        #Couleur en fonction du nombre de mines
        if mineautour == 0:
            couleur = "grey" #gris
        elif mineautour == 1:
            couleur = "#0039ff" #bleu
        elif mineautour == 2:
            couleur = "#017f04" #vert
        elif mineautour == 3:
            couleur = "#ff1b00" #rouge
        elif mineautour == 4:
            couleur = "#001882" #bleu foncé
        elif mineautour == 5:
            couleur = "#810802" #rouge foncé
        elif mineautour == 6:
            couleur = "#028081" #cyan
        elif mineautour == 7:
            couleur = "#000000" #noir
        elif mineautour == 8:
            couleur = "#818080" #gris


        if ligne >= cote+1 or colonne >= cote+1 or ligne < 2 or colonne < 2: #Pour pas sortir de la map
            pass
        else:
            Label(Fenetre, text = "  "+ str(mineautour) +"  ", fg = couleur, relief = FLAT).grid(row = ligne, column = colonne) #Afficahge du nombre de mine autour
            casestestees += 1
        mineautour = 0 #Reset du nombre de mines pour les autrse boutons
        if casestestees + mines == (cote+2)^2:
            showinfo("Gagné !", "Bien joué, vous avez trouvé toutes les mines")


def remplissage():
    for i in range(cote):
        for j in range(cote):
            bouton = boutons(i, j)
            bouton.ligne = i+2
            bouton.colonne = j+2
            #bouton.couleur = "grey"
            bouton.creation()

def action(event):
    #print("\n", event.type)
    #print(event.num)
    #print(event.widget)

    if event.type != "" and event.num == 3:
        #print("clique droit")
        #setattr(event.widget, text, " m ")
        #print(event.widget._gridconvvalue())
        #print(event.widget.winfo_x())
        #print(event.widget.winfo_y())
            #a, gpsbouton = event.widget.grid
        print(event.widget.winfo_x())
        print(event.widget.winfo_y())
        x , y  = (Tk().grid_location(event.widget.winfo_x(),event.widget.winfo_y()))
        Button(Fenetre, text = " M ", bg = "red").grid(row = y+1, column = x+1)


#B1 events:
#Fenetre.bind("<Button-1>", action)
#Fenetre.bind("<B1-Motion>", action)
#Fenetre.bind("<ButtonRelease-1>", action)

#B3 events :
Fenetre.bind("<Button-3>", action)
Fenetre.bind("<B3-Motion>", action)
Fenetre.bind("<ButtonRelease-3>", action)




#Lancement programme

generation()
remplissage()
for i in range(cote+4):
    print(map[i])
Fenetre.mainloop()
