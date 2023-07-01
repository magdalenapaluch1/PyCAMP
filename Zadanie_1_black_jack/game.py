from card import *
from deck import Deck
from player import *

class Game:
    def __init__(self) -> None:
        pass

    def prepare(self, player_name):
        self.deck = Deck()
        self.deck.shuffle()
        self.human = Human(player_name)
        self.croupier = Croupier()
    
    def initial_draw_and_show_hands(self):
        self.human.draw_card(self.deck)
        self.croupier.draw_card(self.deck)

        self.human.draw_card(self.deck)
        self.croupier.draw_card(self.deck)

        self.human.show_hand()
        self.croupier.show_first_hand()

    def human_decision(self):
        decision = None
        bust = False

        if self.human.get_hand_value() != 21:
            while decision != "s":
                decision = input("(s)tand or (h)it? ")

                if decision == 's':
                    pass
                elif decision == 'h':
                    self.human.draw_card(self.deck)
                    print("Your cards: ", self.human.hand)

                    if self.human.get_hand_value() > 21:
                        bust = True
                        break

                else:
                    print("Pardon?")
        else:
            print("Black Jack!")

        return bust
    
    def croupier_decision(self):
        bust = False
        while self.croupier.get_hand_value() < 17:
            self.croupier.draw_card(self.deck)

        if self.croupier.get_hand_value() > 21:
            bust = True

        return bust

    def check_result(self, human_bust, croupier_bust):
        self.human.show_hand()
        self.croupier.show_hand()

        if human_bust != True:
            if (self.human.get_hand_value() > self.croupier.get_hand_value()):
                print(self.human.name, "wins")
            elif (self.human.get_hand_value() == self.croupier.get_hand_value()):
                print("Draw!")
            else:
                if croupier_bust != True:
                    print(self.croupier.name, "wins")
                else:
                    print("CROUPIER BUST!", self.human.name, "wins")  
        else:
            print("BUST!", self.croupier.name, "wins")   
