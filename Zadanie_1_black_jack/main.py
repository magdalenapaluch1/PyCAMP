from card import *
from deck import Deck

if __name__ == '__main__':

    deck = Deck()
    card = deck.draw_card()

    print(card)
    print(deck)

    deck.shuffle()
    print(deck)

