input = open('01 input.txt', 'r')
lignes = input.readlines()
calories = [0] * len(lignes)

# on met ttes les lignes dans une liste calories
for i in range(len(lignes)):
    calories[i] = lignes[i].replace('\n', '')

# on somme tte les calories tant qu'il n'y a pas de ligne vide 
# pour mettre ensuite ces sommes dans une liste elves
elves = []
compteur = 0
for i in range(len(calories)):
    if(calories[i] != ''):
        compteur += int(calories[i])
        continue
    else:
        elves.append(compteur)
        compteur = 0

print('premier :',max(elves))
first = max(elves)

### Partie 2

# on cherche 2 fois l'index de l'elfe qui a le plus de calories 
# on le retire de la liste 2 fois pr trouver le 2 elfes après le premier

indexpremier = elves.index(max(elves))
elves.remove(elves[indexpremier])
print('deuxième :',max(elves))
second = max(elves)

indexdeuxieme = elves.index(max(elves))
elves.remove(elves[indexdeuxieme])
print('troisième :',max(elves))
third = max(elves)

print('total des 3 premiers :',first+second+third)