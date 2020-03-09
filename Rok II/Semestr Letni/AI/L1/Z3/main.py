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
for number in types:
    for color in colors:
        deck.append((number, color))
for number in types:
    if number > 10:
        for color in colors:
            cheater_deck.append((number, color))
for number in types:
    if number < 11:
        for color in colors:
            naive_deck.append((number, color))

def info(hand):
    for card in hand:
        print(types[card[0]], colors[card[1]])

def draw(deck, hand):
    for i in range(5):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)


cheater = []
naive = []
draw(cheater_deck, cheater)
draw(naive_deck, naive)
info(cheater)
print('-------')
info(naive)

cheater_wins = 0
naive_wins = 0
ties = 0

def best(hand):
    # Royal Flush
    for color in [1, 2, 3, 4]:
        flag = True
        for number in [10, 11, 12, 13, 14]:
            card = number, color 
            if card not in hand:
                flag = False
        if flag:
            print('Royal Flush')
            return 10 
    
    # Straight Flush

    # Four of a kind

    # Full house

    # Flush

    # Straight

    # Three of a kind

    # Two pair

    # One pair

    # High card

royal = [(10, 2), (11, 2), (13, 2), (14, 2), (12, 2)]
print(best(royal))