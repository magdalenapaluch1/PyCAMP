from card import *
from deck import Deck
from player import *
from io_interface import *

class Game:
    def __init__(self, gui) -> None:
        if gui is True:
            self.io = GUI()
        else:
            self.io = IO()

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

        self.io.human_display(self.human.get_hand())
        self.io.croupier_display(self.croupier.get_first_hand())

    def human_decision(self):
        decision = None
        bust = False

        if self.human.get_hand_value() != 21:
            while decision != "s":
                decision = self.io.get_human_decision()

                if decision == 's':
                    pass
                elif decision == 'h':
                    self.human.draw_card(self.deck)
                    self.io.human_display("Your cards: " + str(self.human.hand))

                    if self.human.get_hand_value() > 21:
                        bust = True
                        break

                else:
                    self.io.game_display("Pardon?")
        else:
            self.io.game_display("Black Jack!")

        return bust
    
    def croupier_decision(self):
        bust = False
        while self.croupier.get_hand_value() < 17:
            self.croupier.draw_card(self.deck)

        if self.croupier.get_hand_value() > 21:
            bust = True

        return bust

    def check_result(self, human_bust, croupier_bust):
        self.io.game_display("Game finished!")
        self.io.human_display(self.human.get_hand())
        self.io.croupier_display(self.croupier.get_hand())

        if human_bust != True:
            if (self.human.get_hand_value() > self.croupier.get_hand_value()):
                self.io.game_display(str(self.human.name) + " wins!")
            elif (self.human.get_hand_value() == self.croupier.get_hand_value()):
                self.io.game_display("Draw!")
            else:
                if croupier_bust != True:
                    self.io.game_display(str(self.croupier.name) + " wins!")
                else:
                    self.io.game_display("CROUPIER BUST! " + str(self.human.name) + " wins!")  
        else:
           self.io.game_display("BUST! " + str(self.croupier.name) + " wins!")   
