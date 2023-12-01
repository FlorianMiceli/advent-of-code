input = open('04 input.txt', 'r')
lignes = input.readlines()

# convert ligns to list:
def split_lign(lign):
    liste = []
    tempo = ''
    for i in range(len(lign)):
        if lign[i].isdigit() :
            tempo += lign[i]
        elif lign[i] == '-' or lign[i] == ',':
            liste.append(int(tempo))
            tempo = ''
    liste.append(int(tempo))
    return liste

assignments = []
for i in range(len(lignes)):
    assignments.append(split_lign(lignes[i]))

# nbr of peers which have assignments that ones contains the other:
count = 0
for i in range(len(assignments)):
    if assignments[i][0] <= assignments[i][2] and assignments[i][1] >= assignments[i][3]:
        count += 1
    elif assignments[i][0] >= assignments[i][2] and assignments[i][1] <= assignments[i][3]:
        count += 1

print(count)

### Part 2 ###

# nbr of peers which have assignments that overlaps:
count = 0
for i in range(len(assignments)):
    if  (
        (assignments[i][0] <= assignments[i][2] and assignments[i][1] >= assignments[i][2]) 
        or 
        (assignments[i][2] <= assignments[i][0] and assignments[i][3] >= assignments[i][0])
        ):
        count += 1

print(count)