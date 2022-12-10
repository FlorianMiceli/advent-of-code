input = open('02 input.txt', 'r')
lignes = input.readlines()

# on met chaque ligne (chaque round) dans une liste 
# chaque round devient une liste de 2 éléments dans la liste de tous ces rounds
rounds = []
for i in range(len(lignes)):
    rounds.append(lignes[i].split())

# opponent A,B,C
# me X,Y,Z

# A,X rock 
# B,Y paper
# C,Z scissors

# score :

# shape : 1 for Rock, 2 for Paper, and 3 for Scissors
# outcome : 0 lost, 3 draw, 6 won

score = 0
for i in range(len(rounds)):
    if rounds[i][1] == 'X':           # rock
        if rounds[i][0] == 'A':         # draw
            score += (1+3)
        if rounds[i][0] == 'B':         # lost
            score += (1+0)                
        if rounds[i][0] == 'C':         # won
            score += (1+6)
    if rounds[i][1] == 'Y':           # paper
        if rounds[i][0] == 'A':         # won
            score += (2+6)
        if rounds[i][0] == 'B':         # draw
            score += (2+3)
        if rounds[i][0] == 'C':         # lost
            score += (2+0)
    if rounds[i][1] == 'Z':           # scissors
        if rounds[i][0] == 'A':         # lost
            score += (3+0)
        if rounds[i][0] == 'B':         # won
            score += (3+6)
        if rounds[i][0] == 'C':         # draw
            score += (3+3)

print('part one :',score)

### Partie 2

# A rock
# B paper
# C scissors

# X lose
# Y draw
# Z win

# shape : 1 for Rock, 2 for Paper, and 3 for Scissors
# outcome : 0 lost, 3 draw, 6 won

score = 0
for i in range(len(rounds)):
    if rounds[i][0] == 'A':           # rock
        if rounds[i][1] == 'X':         # lose : scissors
            score += (3+0)
        if rounds[i][1] == 'Y':         # draw : rock
            score += (1+3)                
        if rounds[i][1] == 'Z':         # win : paper
            score += (2+6)
    if rounds[i][0] == 'B':           # paper
        if rounds[i][1] == 'X':         # lose : rock
            score += (1+0)
        if rounds[i][1] == 'Y':         # draw : paper
            score += (2+3)
        if rounds[i][1] == 'Z':         # win : scissors
            score += (3+6)
    if rounds[i][0] == 'C':           # scissors
        if rounds[i][1] == 'X':         # lose : paper
            score += (2+0)
        if rounds[i][1] == 'Y':         # draw : scissors
            score += (3+3)
        if rounds[i][1] == 'Z':         # win : rock
            score += (1+6)

print('part two :',score)