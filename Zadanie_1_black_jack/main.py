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

    human.show_hand()
    croupier.show_first_hand()

    decision = None
    bust = False

    while decision != "s":
        decision = input("(s)tand or (h)it? ")

        if decision == 's':
            pass
        elif decision == 'h':
            human.draw_card(deck)
            print("Your cards: ", human.hand)

            if human.get_hand_value() > 21:
                bust = True
                break

        else:
            print("Pardon?")
############################ koniec ruchu uzytkownika

############################## ewentualny ruch krupiera
    while croupier.get_hand_value() < 17:
        croupier.draw_card(deck)

###########################sprawdzanie wynikow
    if bust != True:
        if (human.get_hand_value() > croupier.get_hand_value()):
            print(human.name, "wins")
        elif (human.get_hand_value() == croupier.get_hand_value()):
            print("Draw!")
        else:
            print(croupier.name, "wins")
    else:
        print("BUST!", croupier.name, "wins")    

    human.show_hand()
    croupier.show_hand()


    #TODO
    # jesli od razu 21 to brak wyboru uzytkownika
