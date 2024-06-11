from card import *
from player import *
from game import *
import sys
import os

def restart_program(event):
    python = sys.executable
    os.execl(python, python, * sys.argv)

def main():
    game = Game()

    name = game.gui.get_human_name()

    game.prepare(name)

    game.initial_draw_and_show_hands()

    human_bust = game.human_decision()

    croupier_bust = game.croupier_decision()

    game.check_result(human_bust, croupier_bust)

    game.gui.restart_button["state"] = NORMAL
    game.gui.restart_button.bind("<Button-1>", restart_program)
    game.gui.mainWindow.mainloop()

if __name__ == '__main__':
    main()