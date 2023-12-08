input = open('input.txt', 'r')
lines = input.readlines()
lines = [line.split() for line in lines]

card_types = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J' ,'Q', 'K', 'A']
hand_types_order = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind']

def getHandType(hand):
    hand_types = {
        (5,): 'five_of_a_kind',
        (4, 1): 'four_of_a_kind',
        (3, 2): 'full_house',
        (3, 1, 1): 'three_of_a_kind',
        (2, 2, 1): 'two_pairs',
        (2, 1, 1, 1): 'one_pair',
        (1, 1, 1, 1, 1): 'high_card'
    }

    card_counts = [hand.count(card) for card in set(hand)]
    counts_tuple = tuple(sorted(card_counts, reverse=True))

    return hand_types.get(counts_tuple)

# if the hands are the same type, compare the cards one by one, when one is stronger, return that hand
def whichIsStrongerSameType(hand1, hand2):
    card_hand1 = hand1[0]
    card_hand2 = hand2[0]
    for i in range(0, len(card_hand1)):
        if card_types.index(card_hand1[i]) > card_types.index(card_hand2[i]):
            return hand1
        elif card_types.index(card_hand1[i]) < card_types.index(card_hand2[i]):
            return hand2
    return hand1

def whichIsStronger(hand1, hand2):
    hand1_type = getHandType(hand1)
    hand2_type = getHandType(hand2)
    if hand1_type == hand2_type:
        return whichIsStrongerSameType(hand1, hand2)
    else :
        if hand_types_order.index(hand1_type) > hand_types_order.index(hand2_type):
            return hand1
        return hand2

# lines are composed of a hand, a bid amount, and the type of hand
# sort the lines by the type of hand, and if they are the same type, use whichIsStronger
def sortLines(lines):

    # sort by hand type
    lines.sort(key=lambda line: hand_types_order.index(line[2]))

    # sort by strength
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            if lines[i][2] == lines[j][2]:
                stronger_hand = whichIsStrongerSameType(lines[i], lines[j])
                if stronger_hand == lines[i]:
                    lines[i], lines[j] = lines[j], lines[i]
                    
    return lines

# append hand types
lines = [line + [getHandType(line[0])] for line in lines]

# sort lines
lines = sortLines(lines)

for line in lines:
    print(line)

# multiply the bid amount by the rank of the hand, starting from 1
# add the bid amounts together
total = 0
for i in range(0, len(lines)):
    total += (i+1) * int(lines[i][1])

print(f'Part 1 answer: {total}')