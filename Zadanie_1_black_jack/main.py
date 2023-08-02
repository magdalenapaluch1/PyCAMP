from card import *
from player import *
from game import *
import sys
import os
import argparse

def restart_program(event):
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--cmd', required = False, default = "off")
    args = parser.parse_args()

    if args.cmd == "on":
        guiEnabled = False
    else:
        guiEnabled = True

    game = Game(guiEnabled)

    name = game.io.get_human_name()

    game.prepare(name)

    game.initial_draw_and_show_hands()

    human_bust = game.human_decision()

    croupier_bust = game.croupier_decision()

    game.check_result(human_bust, croupier_bust)

    if guiEnabled:
        game.io.restart_button["state"] = NORMAL
        game.io.restart_button.bind("<Button-1>", restart_program)
        game.io.mainWindow.mainloop()
