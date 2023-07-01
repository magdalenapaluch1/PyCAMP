from card import *
from deck import Deck
from player import *
from game import *

if __name__ == '__main__':

    game = Game()

    name = input("What's your name?")

    game.prepare(name)

    game.initial_draw_and_show_hands()

    human_bust = game.human_decision()

    croupier_bust = game.croupier_decision()

    game.check_result(human_bust, croupier_bust)
