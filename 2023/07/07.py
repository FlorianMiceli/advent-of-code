input = open('input.txt', 'r')
lines = input.readlines()
lines = [line.split() for line in lines]

# input example
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

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

def whichIsStrongerSameType(hand1, hand2):
    card_hand1 = hand1[0]
    card_hand2 = hand2[0]
    # while

def whichIsStronger(hand1, hand2):
    hand1_type = getHandType(hand1)
    hand2_type = getHandType(hand2)
    if hand1_type == hand2_type:
        return whichIsStrongerSameType(hand1, hand2)
    else :
        if hand_types_order.index(hand1_type) > hand_types_order.index(hand2_type):
            return hand1
        return hand2

hand = lines[0][0]
# hand = 'AAAAA'

print(getHandType(hand))