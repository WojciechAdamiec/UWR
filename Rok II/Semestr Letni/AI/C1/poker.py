import random
import itertools

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


make_cheater_deck()
make_naive_deck()


def find_subsets(s, n):
    return list(itertools.combinations(s, n))


cheater_hands = find_subsets(cheater_deck, 5)
naive_hands = find_subsets(naive_deck, 5)


cheater_results = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
}

naive_results = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
}


for hand in cheater_hands:
    cheater_results[best(list(hand))] += 1
for hand in naive_hands:
    naive_results[best(list(hand))] += 1


counter = 0
omega = len(cheater_hands) * len(naive_hands)


for i in range(10, 2, -1):
    acc = 0
    for j in range(8, 1, -1):
        if i > j:
            acc += cheater_results[j]
    counter += acc * naive_results[i]


print('Chance is: ', counter/omega)
