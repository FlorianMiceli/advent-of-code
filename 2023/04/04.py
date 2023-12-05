input = open('input.txt', 'r')
lines = input.readlines()

# Example input
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# transform input line into example for line 1 : {1: {winning_numbers: [41, 48, 83, 86, 17], elf_numbers: [83, 86, 6, 31, 17, 9, 48, 53]}}
def lineToDict(line):
    line = line.split(':')
    data = line[1].split('|')
    winning_numbers = data[0].split(' ')
    winning_numbers = [int(i) for i in winning_numbers if i != '']
    elf_numbers = data[1].split(' ')
    elf_numbers = [int(i) for i in elf_numbers if i != '']
    return {'winning_numbers': winning_numbers, 'elf_numbers': elf_numbers}

# now we have 
# {'winning_numbers': [41, 48, 83, 86, 17], 'elf_numbers': [83, 86, 6, 31, 17, 9, 48, 53]}
# {'winning_numbers': [13, 32, 20, 16, 61], 'elf_numbers': [61, 30, 68, 82, 17, 32, 24, 19]}
# {'winning_numbers': [1, 21, 53, 59, 44], 'elf_numbers': [69, 82, 63, 72, 16, 21, 14, 1]}
# {'winning_numbers': [41, 92, 73, 84, 69], 'elf_numbers': [59, 84, 76, 51, 58, 5, 54, 83]}
# {'winning_numbers': [87, 83, 26, 28, 32], 'elf_numbers': [88, 30, 70, 12, 93, 22, 82, 36]}
# {'winning_numbers': [31, 18, 13, 56, 72], 'elf_numbers': [74, 77, 10, 23, 35, 67, 36, 11]}

# In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

def getPoints(winning_numbers, elf_numbers):
    points = 0
    for elf_number in elf_numbers:
        if elf_number in winning_numbers:
            points = points*2 if points > 0 else 1
    return points

points_sum = 0
for line in lines:
    line = lineToDict(line)
    points = getPoints(line['winning_numbers'], line['elf_numbers'])
    points_sum += points

# print(points_sum)

### Part 2 ###

def linesToDict(lines):
    cards = {}
    for line in lines:
        data = lineToDict(line)
        card_number = line.split(':')[0][-1]
        cards[card_number] = data
    return cards

def getNumberOfWinningNumbers(card):
    nbr_winning_numbers = 0
    for elf_number in card['elf_numbers']:
        if elf_number in card['winning_numbers']:
            nbr_winning_numbers += 1
    return nbr_winning_numbers

# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)
def storeCardsNumber(card, nbr_winning_numbers):
    # example: if nbr_winning_numbers is 5, add a "copies" key to each next 5 cards, incremented from 1 to 2
    if nbr_winning_numbers > 0:
        for i in range(card, nbr_winning_numbers+1):
            card_number = int(card['card_number']) + i
            print('add a copy to',card_number)
            cards[card_number]['copies'] = cards[card_number].get('copies', 0) + 1

cards = linesToDict(lines)
for card in cards:
    nbr_winning_numbers = getNumberOfWinningNumbers(cards[card])
    storeCardsNumber
    print(nbr_winning_numbers)

