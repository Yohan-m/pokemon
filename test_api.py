import pokebase as pb

class Pokemon:
    def __init__(self, id):
        self.name = pb.pokemon(id).name
        self.height = pb.pokemon(id).height
        self.type = pb.pokemon(id).types[0].type.name
        self.atk = pb.pokemon(id).stats[1].base_stat
        self.hp = pb.pokemon(id).stats[0].base_stat
        self.vit = pb.pokemon(id).stats[5].base_stat


# b = Pokemon(1)
# print(b.name)
# print(b.hp)

# boucle création pokémon api vers objet
# le premier pokémon à pour indez 0 mais son id dans l'api est 1
pokelist = []
for i in range(1,13,1):
    onepok = Pokemon(i)
    pokelist.append(onepok)

# boucle affiché les noms des pokémon
j = 0

while j < 12:
    
    print("Le nom de pokémon : " + pokelist[j].name)
    print("La taille de ce pokémon est : " + str(pokelist[j].height))
    print("Ce pokémon est de type : " + str(pokelist[j].type))
    print("Les stats d'attack de ce pokémon est de : "+ str(pokelist[j].atk))
    print("Les stats de vie de ce pokémon est de : "+ str(pokelist[j].hp))
    print("La vitesse de ce pokémon est de : "+ str(pokelist[j].vit))

    print(" ")
    j = j+1

# compléter class pokémon avec toutes les données qu'on a besoin
# Faire une fonction hors class de tri genre affcihé que les pokémons commencant par un c (reduce ou filter) possibilité d'evoluer que ce soit l'utilistateur qui rentre la 1er lettre
# Faire une méthode afficher le nombre de pokémon par types (possibilité dico clé type et valuer le nombre)
# Faire une fonction qui affiche le pokemon en donnant l'index
# Faire une fonction donnant un pokemon aleatoire biblioeque math random (demandé)

# Faire une sorte d'interface taper 1 pour entrer un index et voir les stat du pokémon taper 2 pour affiché les pokémon commencant par c...
# Le programme ne doit pas s'arrêter donc à chaque fin d'execution on retourne à l'interface et c'est sur l'interface en tapant "close" que le programme s'arrete
# faire les docs

# Si on a le temps affiché les sorties avec la bibliothèque vu en cours