import pokebase as pb
import random
import matplotlib.pyplot as plt
import numpy as np
import pylab



print("Lancement du pokédex chargement des pokémons")

class Pokemon:
    def __init__(self, id):
        self.name = pb.pokemon(id).name
        self.height = pb.pokemon(id).height*10
        self.type = pb.pokemon(id).types[0].type.name
        self.atk = pb.pokemon(id).stats[1].base_stat
        self.hp = pb.pokemon(id).stats[0].base_stat
        self.vit = pb.pokemon(id).stats[5].base_stat
        self.img = pb.pokemon_form(id).sprites.front_default
    def pokeType(self):

        typeTable =[]
        typeNum=[]

        for i in range(1,18,1):
            typeTable.append(pb.type_(i).name)
            typeNum.append(len(pb.type_(i).pokemon))

        print("Rentrez 1 pour un affichage dictionnaire")
        print("Rentrez 2 pour un affichage graphique")

        choix= int(input("Rentrez 1 ou 2 : "))

        if choix == 1:
            dictionnaire = dict(zip(typeTable,typeNum))
            print(dictionnaire)
        if choix == 2:

            x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
            height = typeNum
            barName = typeTable
            width = 0.5
            pylab.xticks(x, barName, rotation=40)
            plt.bar(x, height, width, color="r" )
            plt.ylabel('Nombre de Pokémon©')
            plt.title('Nombre de Pokémon© par type')
            plt.show()
        


        

    
        
   
# boucle création pokémon api vers objet
# le premier pokémon à pour indez 0 mais son id dans l'api est 1
pokelist = []
for i in range(1,1,1):
    onepok = Pokemon(i)
    pokelist.append(onepok)


#Toutes les fonctions doivent être écrites en dessous
#Test Int
j = 0
def testIntFunc(chiffre):
    r = chiffre
    testInt = r.isnumeric()
    while testInt == True and int(r) > 5 or testInt != True:
        print("Veuillez entrez un chiffre entre 1 et 5")
        r = input('Rentrez un numéro de pokémon ! ')
        testInt = r.isnumeric()
    global j
    j = r
#Quiz nom pokémon
def Quizz():
    print("Bienvenu dans le Quizz pokémon appuyer a tout moment sur 'c' pour quitter le jeu")
    id = input('Rentrez un numéro de pokémon ! ')
    testIntFunc(id)
    id = int(j)

    mot = pokelist[id].name
    lettre = mot[:1]
    secLetter = mot[:2]
    nblettre = 1
    print("\nLa premiere lettre du prénom de ce pokémon lettre est : " + str(lettre))

    Stat(id,0)
    
    entryUser = input('Rentrez le nom du pokémon : ')

    while str(entryUser) != mot and str(entryUser) != "c":
        if nblettre == 1:
            questSecLetter = input('Voulez vous la 2ème lettre de ce pokémon ? - y or n ')
            if questSecLetter == 'y':
                print("La deuxième lettre du prénom de ce pokémon lettre est : " + str(secLetter))
                nblettre = 2
            
            entryUser = input('Rentrez le nom du pokémon : ')

        else:
            print("Ce n'est pas la bonne réponse")
            print("La deuxième lettre du prénom de ce pokémon lettre est : " + str(secLetter))
            entryUser = input('Rentrez le nom du pokémon : ')
    if str(entryUser) == mot:
        print('Bien joué le pokémon était bien : ' + str(pokelist[id].name))
    else:
        print("Retente ta chance plus tard")
        
def Allpok():
    j = 0
    while j < 4:
        Stat(j,1)
        print(" ")
        j = j+1

def Stat(id,a):
    if a == 1:
        print("\nLe nom de pokémon : " + pokelist[id].name)
        
    print("\nLa taille de ce pokémon est : " + str(pokelist[id].height)+' cm')
    print("Ce pokémon est de type : " + str(pokelist[id].type))
    print("Les stats d'attack de ce pokémon est de : "+ str(pokelist[id].atk))
    print("Les stats de vie de ce pokémon est de : "+ str(pokelist[id].hp))
    print("La vitesse de ce pokémon est de : "+ str(pokelist[id].vit))
    print("")

def pokeStat():
    id = input('Rentre un numéro de pokémon ')
    testIntFunc(id)
    id = int(j)
    Stat(id,1)                                                                      
    
def randomPoke():
    n = random.randint(0,4)
    print(n)
    Stat(1,1)
    
def Filtre():
    print("Fonction de tri de pokémon via leur 1er lettre")
    letter = input("Rentrer la 1er lettre du pokémon ")[0]
    result = []
    for j in range(0,5,1):
        if pokelist[j].name[0] == letter:
            result.append(j)
    
    k = len(result)

    print("Il y a " + str(k) + " pokémons commencant par la lettre " + letter)

    while k > 0:
        Stat(result[k-1],1)
        k = k-1


# fin des fonctions

# Exécution du code

print("Pokémon chargés en attente d'instruction") 

#interface 
panel = ""
while panel != 7:
    print('Bienvenue sur notre Pokedex interactif pour enfant !\n')
    print('Vous avez 5 commandes possibles qui sont les suivantes \n')
    print("1- Voir l'ensemble des pokémons ")
    print('2- Petit quizz ')
    print('3- Pokémon par numéro ! ')
    print('4- Générer un pokémon aléatoirement')
    print('5- Filtrer les pokémons')
    print('6- Afficher le nombres de pokémons par types')
    print('0- Pokégraph')
    print('7- Terminer la partie\n')
    panel = input("commande entre 1 et 7 ?\n")

    errorInt = panel.isnumeric()
    while errorInt == True and int(panel) > 7 or errorInt != True:
        print("Veuillez entrez un chiffre entre 1 et 6 ou 7 pour quitter")
        panel = input("commande entre 1 et 7 ?")
        errorInt = panel.isnumeric()
    panel=int(panel)

    if panel == 1:
        Allpok()
    if panel == 2:
        Quizz()
    if panel == 3:
        pokeStat()
    if panel == 4:
        randomPoke()
    if panel == 5:
        Filtre()
    if panel == 6:
        Pokemon(1).pokeType()
print ("Merci d'avoir jouer !")


# Faire une méthode afficher le nombre de pokémon par types (possibilité dico clé type et valeur le nombre)
# fonction ou ajouter à la suite des fonctions affiché 1 pokémon générateur / itérateur pour afficher le pokémon suivant
# faire les docs

# Si on a le temps essayer de regroupé tous les affichages des stats pokémon dans la fonction stat 
# donc dans fonction quizz faire un appel à stat mais avec un parametre pour pas afficher le nom
# pour ensuite affiché la fonction stat avec la bibliothèque vu en cours
# ou directement faire la biblioteque à plusieur endrit dans le code si plus simple
