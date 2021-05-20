import pokebase as pb
import random
# import tkinter
print("Lancement du pokédex chargement des pokémons")
# #Fenetre 
# window = tkinter.Tk()
# window.mainloop 
# window.title('PokéQuizz')
# window.geometry("300x300")
# window.iconbitmap("logo.ico")



class Pokemon:
    def __init__(self, id):
        self.name = pb.pokemon(id).name
        self.height = pb.pokemon(id).height*10
        self.type = pb.pokemon(id).types[0].type.name
        self.atk = pb.pokemon(id).stats[1].base_stat
        self.hp = pb.pokemon(id).stats[0].base_stat
        self.vit = pb.pokemon(id).stats[5].base_stat
    
        
   
# boucle création pokémon api vers objet
# le premier pokémon à pour indez 0 mais son id dans l'api est 1
pokelist = []
for i in range(1,5,1):
    onepok = Pokemon(i)
    pokelist.append(onepok)

# b = Pokemon(1)
# print(b.name)
# print(b.hp)

#Toutes les fonctions doivent être écrites en dessous

#Quiz nom pokémon
def Quizz():
    print("Bienvenu dans le Quizz pokémon appuyer a tout moment sur 'c' pour quitter le jeu")
    id = input('Rentrez un numéro de pokémon ! ')
    
    testInt = id.isnumeric()

    while testInt != True or int(id) > 5:
        print("Veuillez entrer un chiffre entre 1 et 5")
        id = input('Rentrez un numéro de pokémon ! ')
        testInt = id.isnumeric()
        

    id = int(id)-1


    mot = pokelist[id].name
    lettre = mot[:1]
    secLetter = mot[:2]
    nblettre = 1

    print("La taille de ce pokémon est : " + str(pokelist[id].height)+' cm')
    print("Ce pokémon est de type : " + str(pokelist[id].type))
    print("Les stats d'attack de ce pokémon est de : "+ str(pokelist[id].atk))
    print("Les stats de vie de ce pokémon est de : "+ str(pokelist[id].hp))
    print("La vitesse de ce pokémon est de : "+ str(pokelist[id].vit))
    print("La premiere lettre du prénom de ce pokémon lettre est : " + str(lettre))
    print("")

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
        Stat(j)
        print(" ")
        j = j+1

def Stat(id):
        print("Le nom de pokémon : " + pokelist[id].name)
        print("La taille de ce pokémon est : " + str(pokelist[id].height))
        print("Ce pokémon est de type : " + str(pokelist[id].type))
        print("Les stats d'attack de ce pokémon est de : "+ str(pokelist[id].atk))
        print("Les stats de vie de ce pokémon est de : "+ str(pokelist[id].hp))
        print("La vitesse de ce pokémon est de : "+ str(pokelist[id].vit))  

def pokeName():
    id = int(input('Rentre un numéro de pokémon '))
    Stat(id)

def randomPoke():
    n = random.randint(0,4)
    Stat(n)
    
def Filtre():
    print("Fonction de tri de pokémon via leur 1er lettre")
    letter = input("Rentrer la 1er lettre du pokémon ")[0]
    result = []
    for j in range(0,4,1):
        if pokelist[j].name[0] == letter:
            result.append(j)
    
    k = len(result)

    print("Il y a " + str(k) + " pokémons commencant par la lettre " + letter)

    while k > 0:
        Stat(result[k-1])
        k = k-1
       

# fin des fonctions

# Exécution du code

print("Pokémon chargés en attente d'instruction") 

#interface 

panel = 0
while panel != 5:
    print('Bienvenue sur notre Pokedex interactif pour enfant !')
    print('Vous avez 5 commandes possibles qui sont les suivantes ')
    print("1-Voir l'ensemble des pokémons ")
    print('2-Petit quizz ')
    print('4-Générer un pokémon aléatoirement')
    print('5- Terminer la partie')
    panel = int(input("commande entre 1 et 4 ?"))
    if panel == 1:
        Allpok()
    if panel == 2:
        Quizz()
    if panel == 3:
        pokeName()
    if panel == 4:
        randomPoke()
print ("Merci d'avoir jouer !")


# Faire une méthode afficher le nombre de pokémon par types (possibilité dico clé type et valuer le nombre)
# fonction ou ajouter à la suite des fonctions affiché 1 pokémon générateur / itérateur pour afficher le pokémon suivant
# faire les docs

# Si on a le temps essayer de regroupé tous les affichages des stats pokémon dans la fonction stat 
# donc dans fonction quizz faire un appel à stat mais avec un parametre pour pas afficher le nom
# pour ensuite affiché la fonction stat avec la bibliothèque vu en cours
# ou directement faire la biblioteque à plusieur endrit dans le code si plus simple
