import pokebase as pb

class Pokemon:
    def __init__(self, id):
        self.name = pb.pokemon(id).name
        self.hp = pb.pokemon(id).height

# b = Pokemon(1)
# print(b.name)
# print(b.hp)

# boucle création pokémon api vers objet
# le premier pokémon à pour indez 0 mais son id dans l'api est 1
a = []
for i in range(1,11,1):
    w = Pokemon(i)
    a.append(w)

# boucle affiché les noms des pokémon
j = 0
while j < i:
    print(a[j].name)
    j = j+1
