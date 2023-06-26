from card import *
from deck import Deck
from player import *

if __name__ == '__main__':

    deck = Deck()
    deck.shuffle()

    human = Human("Wojtek")
    croupier = Croupier()

    human.draw_card(deck)
    croupier.draw_card(deck)

    human.draw_card(deck)
    croupier.draw_card(deck)

    print("Your cards: ", human.hand)
    print("Croupier cards: ", croupier.hand)

    decision = input("(s)tand or (h)it?")
    if decision == 's':
        pass
    elif decision == 'h':
        human.draw_card(deck)
    else:
        print("Pardon?")

    if (human.get_hand_value() > croupier.get_hand_value()):
        print(human.name, "wins")
    else:
        print(croupier.name, "wins")

    print(human.hand)
    print(croupier.hand)


    #TODO
    #przegrana gracza
    #ocena kto wygrywa
    #decyzja krupiera
    #