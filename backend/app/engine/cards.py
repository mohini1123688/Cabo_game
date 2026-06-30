import numpy as np
from collections import deque

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

deck_stack = deque()
discard_pile = deque()
# Deck with all 4 suits
deck = np.array([
    # Hearts
    [Card("H", 1), Card("H", 2), Card("H", 3), Card("H", 4), Card("H", 5), 
     Card("H", 6), Card("H", 7), Card("H", 8), Card("H", 9), Card("H", 10), 
     Card("H", 11), Card("H", 12), Card("H", 13)],
    # Clubs
    [Card("C", 1), Card("C", 2), Card("C", 3), Card("C", 4), Card("C", 5), 
     Card("C", 6), Card("C", 7), Card("C", 8), Card("C", 9), Card("C", 10), 
     Card("C", 11), Card("C", 12), Card("C", 13)],
    # Spades
    [Card("S", 1), Card("S", 2), Card("S", 3), Card("S", 4), Card("S", 5), 
     Card("S", 6), Card("S", 7), Card("S", 8), Card("S", 9), Card("S", 10), 
     Card("S", 11), Card("S", 12), Card("S", 13)],
    # Diamonds
    [Card("D", 1), Card("D", 2), Card("D", 3), Card("D", 4), Card("D", 5), 
     Card("D", 6), Card("D", 7), Card("D", 8), Card("D", 9), Card("D", 10), 
     Card("D", 11), Card("D", 12), Card("D", 13)]
])
def shuffle_deck(deck):
    return np.random.permutation(deck.flatten()).reshape(deck.shape)

def create_stack(deck):
    for card_type in deck:
        for card in card_type:
            deck_stack.append(card)
            print("appended!")
            print(f"{card.value}")

def draw_card(deck_stack):
    discard_pile.append(deck_stack.pop())
    print(f"drawn card {discard_pile[0]}")

shuffled = shuffle_deck(deck)
stack = create_stack(shuffled)
draw_card(stack)
print(discard_pile.pop())