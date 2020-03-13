import random

types = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}

colors = { 
    1: "Kier",
    2: "Karo",
    3: "Pik",
    4: "Trefl"
}

deck = []
cheater_deck = []
naive_deck = []

def make_deck():
    deck.clear()
    for number in types:
        for color in colors:
            deck.append((number, color))

def make_cheater_deck():
    cheater_deck.clear()
    for number in types:
        if number > 10:
            for color in colors:
                cheater_deck.append((number, color))

def make_naive_deck():
    naive_deck.clear()            
    for number in types:
        if number < 11:
            for color in colors:
                naive_deck.append((number, color))

def info(hand):
    for card in hand:
        print(types[card[0]], colors[card[1]])

def draw(deck, hand):
    while len(hand) != 5:
        card = random.choice(deck)
        if card not in hand:
            hand.append(card)

# make_deck()
# make_cheater_deck()
# make_naive_deck()


def best(hand):
    hand.sort()
    # Royal Flush
    for color in [1, 2, 3, 4]:
        flag = True
        for number in [10, 11, 12, 13, 14]:
            card = number, color 
            if card not in hand:
                flag = False
        if flag:
            # print('Royal Flush')
            return 10 
    
    # Straight Flush
    flag = True
    for step in range(4):
        if hand[step][0] != hand[step + 1][0] - 1 or hand[step][1] != hand[step + 1][1]:
            flag = False
    if flag:
        # print('Straight Flush')
        return 9

    # Four of a kind
    for number in range(2, 15):
        flag = True
        for color in [1, 2, 3, 4]:
            card = number, color
            if card not in hand:
                flag = False
        if flag:
            # print('Four of a kind')
            return 8


    # Full house
    counts = []
    for number in range(15):
        counts.append(0)
    for card in hand:
        counts[card[0]] += 1
    if 3 in counts and 2 in counts:
        # print('Full house')
        return 7

    # Flush
    flag = True
    for step in range(4):
        if hand[step][1] != hand[step + 1][1]:
            flag = False
    if flag:
        # print('Flush')
        return 6

    # Straight
    flag = True
    for step in range(4):
        if hand[step][0] != hand[step + 1][0] - 1:
            flag = False
    if flag:
        # print('Straight')
        return 5

    # Three of a kind
    counts = []
    for number in range(15):
        counts.append(0)
    for card in hand:
        counts[card[0]] += 1
    if 3 in counts:
        # print('Three of a kind')
        return 4 

    # Two pair
    counts = []
    for number in range(15):
        counts.append(0)
    for card in hand:
        counts[card[0]] += 1
    aux = 0
    for count in counts:
        if count == 2:
            aux += 1
    if aux == 2:
        # print('Two pair')
        return 3

    # One pair
    counts = []
    for number in range(15):
        counts.append(0)
    for card in hand:
        counts[card[0]] += 1
    if 2 in counts:
        # print('One pair')
        return 2 

    # High card
    # print('High Card')
    return 1


# Testing logic

"""
royal = [(10, 2), (11, 2), (13, 2), (14, 2), (12, 2)]
flush = [(7, 1), (9, 1), (6, 1), (8, 1), (10, 1)]
four = [(4, 3), (6, 1), (6, 2), (6, 4), (6, 3)]
full = [(12, 1), (12, 2), (12, 3), (7, 1), (7, 2)]
two = [(14, 1), (14, 2), (12, 3), (12, 4), (2, 2)]
print(best(royal))
print(best(flush))
print(best(four))
print(best(full))
print(best(two))
"""

# Monte Carlo for testing winratio between cheater and naive
TRIES = 10000

cheater_wins = 0
naive_wins = 0

make_cheater_deck()
make_naive_deck()

for i in range(TRIES):
    cheater = []
    naive = []
    draw(cheater_deck, cheater)
    draw(naive_deck, naive)
    if best(cheater) >= best(naive):
        cheater_wins += 1
    else:
        naive_wins += 1

print('cheater wins: ', cheater_wins)
print('naive wins:   ', naive_wins)
print("naive's winratio: ", naive_wins/TRIES)

# For TRIES = 1 000 000 winratio is: 0.084407
# Now winning naive deck:

winning_naive_deck = [
    (10, 1),
    (10, 2),
    (10, 3),
    (10, 4),
    (9, 1),
    (9, 2),
    (9, 3),
    (9, 4),
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
]

TRIES = 100000

cheater_wins = 0
naive_wins = 0

make_cheater_deck()
make_naive_deck()

for i in range(TRIES):
    cheater = []
    naive = []
    draw(cheater_deck, cheater)
    draw(winning_naive_deck, naive)
    if best(cheater) >= best(naive):
        cheater_wins += 1
    else:
        naive_wins += 1

print('cheater wins: ', cheater_wins)
print('naive wins:   ', naive_wins)
print("naive's winratio: ", naive_wins/TRIES)

# Here winratio is 0.569 and we use deck of 12 cards.