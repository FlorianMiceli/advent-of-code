input = open('03 input.txt', 'r')
lignes = input.readlines()


# priorités :
p = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# dico des priorités :
d = {}
for i in range(len(p)):
    d.update({p[i] : i+1})

# liste des compartiments où chaque rucksack est une liste de ses 2 compartiments:
compartments = []
for i in range(len(lignes)):
    compartments.append( [
        lignes[i][0 : int(len(lignes[i])/2)],                    #première moitié du rucksack (compartment 1)
        lignes[i][int(len(lignes[i])/2) : int(len(lignes[i]))].replace('\n', '')   #deuxième moitié du rucksack (compartment 2)
        ] )

# liste des items qui apparaissent dans les 2 compartiments pr chaque rucksack:
items = []

for i in range(len(compartments)):
    items.append([])
    for j in range(len(compartments[i][0])):
        if compartments[i][0][j] in compartments[i][1] :
            if compartments[i][0][j] not in items[i]:
                items[i] = compartments[i][0][j]


# remplaçons les itemps par leur priorité:
def replace_by_prirority(list):
    for i in range(len(list)):
        list[i] = d[list[i]]
    return list

print('somme des priorités :', sum(replace_by_prirority(items)))

### Partie 2

# liste des groupes de 3 lignes:
groupes = []
for i in range(len(lignes)):
    if i%3 == 0:
        groupes.append(
            [ lignes[i].replace('\n', ''),
            lignes[i+1].replace('\n', ''),
            lignes[i+2].replace('\n', '') ]
        )

# liste des items communs à chaque groupe de 3 lignes (badges):
badges = ['a'] * len(groupes)
for i in range(len(groupes)):
    for j in range(len(groupes[i][0])):
        if groupes[i][0][j] in groupes[i][1] and groupes[i][0][j] in groupes[i][2]:
            if groupes[i][0][j] not in badges[i]:
                badges[i] = groupes[i][0][j]

print('somme des priorités des badges :', sum(replace_by_prirority(badges)))