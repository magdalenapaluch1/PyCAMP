from card import *
from deck import Deck
from player import *
from gui import *

class Game:
    def __init__(self) -> None:
        self.gui = GUI()

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

        self.gui.show_card(self.human.hand[0], "human")
        self.gui.show_card(self.human.hand[1], "human")
        self.gui.update_human_points(str(self.human.get_hand_value()))

        self.gui.show_card(self.croupier.hand[0], "croupier")

        self.gui.enable_action_buttons()

    def human_decision(self):
        decision = None
        bust = False

        if self.human.get_hand_value() != 21:
            while decision != "s":
                decision = self.gui.get_human_decision()

                if decision == 's':
                    self.gui.disable_action_buttons()
                elif decision == 'h':
                    self.human.draw_card(self.deck)
                    self.gui.show_card(self.human.hand[-1], "human")
                    self.gui.update_human_points(str(self.human.get_hand_value()))
                    if self.human.get_hand_value() > 21:
                        bust = True
                        break

                else:
                    self.gui.game_display("Pardon?")
        else:
            self.gui.game_display("Black Jack!")

        return bust
    
    def croupier_decision(self):
        self.gui.show_card(self.croupier.hand[-1], "croupier")
        self.gui.update_croupier_points(str(self.croupier.get_hand_value()))
        bust = False
        while self.croupier.get_hand_value() < 17:
            self.croupier.draw_card(self.deck)
            self.gui.show_card(self.croupier.hand[-1], "croupier")
            self.gui.update_croupier_points(str(self.croupier.get_hand_value()))

        if self.croupier.get_hand_value() > 21:
            bust = True

        return bust

    def check_result(self, human_bust, croupier_bust):
        self.gui.game_display("Game finished!")

        if human_bust != True:
            if (self.human.get_hand_value() > self.croupier.get_hand_value()):
                self.gui.game_display(str(self.human.name) + " wins!")
            elif (self.human.get_hand_value() == self.croupier.get_hand_value()):
                self.gui.game_display("Draw!")
            else:
                if croupier_bust != True:
                    self.gui.game_display(str(self.croupier.name) + " wins!")
                else:
                    self.gui.game_display("CROUPIER BUST! " + str(self.human.name) + " wins!")  
        else:
           self.gui.game_display("BUST! " + str(self.croupier.name) + " wins!")   
