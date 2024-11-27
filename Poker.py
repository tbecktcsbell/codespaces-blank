import random
values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['Hearts','Diamonds','Spades','Clubs']
deck = []

def build_deck():
    for value in values:
        for suit in suits:
            deck.append((value, suit))



def shuffle():
    for i in range(len(deck)):
        r_num = random.randint(0,len(deck)-1)
        temp = deck[r_num]
        deck[r_num] = deck[i] 
        deck[i] = temp
build_deck()
shuffle()

def draw_card():
    return deck.pop()

print(draw_card())