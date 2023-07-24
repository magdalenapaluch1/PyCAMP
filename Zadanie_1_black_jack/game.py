from card import *
from deck import Deck
from player import *
from io_interface import *

class Game:
    def __init__(self, gui) -> None:
        if gui is True:
            self.io = GUI()
            self.guiEnable = True
        else:
            self.io = IO()
            self.guiEnable = False

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

        self.io.show_card(self.human.hand[0], "human")
        self.io.show_card(self.human.hand[1], "human")
        self.io.update_human_points(str(self.human.get_hand_value()))

        self.io.show_card(self.croupier.hand[0], "croupier")

        if self.guiEnable is True:
            self.io.enable_action_buttons()

    def human_decision(self):
        decision = None
        bust = False

        if self.human.get_hand_value() != 21:
            while decision != "s":
                decision = self.io.get_human_decision()

                if decision == 's':
                    if self.guiEnable is True:
                        self.io.disable_action_buttons()
                elif decision == 'h':
                    self.human.draw_card(self.deck)
                    # self.io.human_display("Your cards: " + str(self.human.hand))
                    self.io.show_card(self.human.hand[-1], "human")
                    self.io.update_human_points(str(self.human.get_hand_value()))
                    if self.human.get_hand_value() > 21:
                        bust = True
                        break

                else:
                    self.io.game_display("Pardon?")
        else:
            self.io.game_display("Black Jack!")

        return bust
    
    def croupier_decision(self):
        self.io.show_card(self.croupier.hand[-1], "croupier")
        self.io.update_croupier_points(str(self.croupier.get_hand_value()))
        bust = False
        while self.croupier.get_hand_value() < 17:
            self.croupier.draw_card(self.deck)
            self.io.show_card(self.croupier.hand[-1], "croupier")
            self.io.update_croupier_points(str(self.croupier.get_hand_value()))

        if self.croupier.get_hand_value() > 21:
            bust = True

        return bust

    def check_result(self, human_bust, croupier_bust):
        self.io.game_display("Game finished!")

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
