from tkinter import *
import tkinter.font as font

CARD_HEIGHT = 240
CARD_WIDTH = 160
CARDS_IN_ROW = 4

class IO:
    def __init__(self) -> None:
        pass

    def game_display(self, text):
        print(text)

    def human_display(self, text):
        print(text)
    
    def croupier_display(self, text):
        print(text)
    
    def show_card(self, card, player):
        if player == "human":
            print("Human card: ", card)
        elif player == "croupier":
            print("Croupier card: ",card)

    def get_human_name(self) -> str:
        return input("What is your name? ")

    def get_human_decision(self) -> str:
        return input("(s)tand or (h)it? ")
    
class GUI(IO):
    player_cards = 0
    croupier_cards = 0

    def __init__(self) -> None:
        self.mainWindow = Tk()
        self.mainWindow.geometry("1400x900")
        self.mainWindow.title("Black Jack")
        self.mainWindow.resizable(False, False)

        entry_label = Label(text="What is your name? ")
        entry_label.grid(row = 0, column = 0, sticky = "W")
        self.entry = Entry(fg="black", bg="white", width=20)
        self.entry.insert(0, "player")
        self.entry.grid(row = 0, column = 0)
        self.button_pressed = StringVar()
        self.entry_button = Button(self.mainWindow, text="Enter", command=lambda: self.button_pressed.set("button pressed"))
        self.entry_button.grid(row = 0, column = 0, sticky = "E")

        self.restart_pressed = StringVar()
        self.restart_button = Button(self.mainWindow, text="Restart game", command=lambda: self.restart_pressed.set("restart pressed"))
        self.restart_button["state"] = DISABLED
        self.restart_button.grid(row = 0, column = 1)

        self.human_button_decision = StringVar()
        button_font = font.Font(size=30)
        self.hit_button = Button(self.mainWindow, text="Hit", bg="lightgreen", command=lambda: self.human_button_decision.set("h"))
        self.hit_button['font'] = button_font
        self.stand_button = Button(self.mainWindow, text="Stand", bg="red3", command=lambda: self.human_button_decision.set("s"))
        self.stand_button['font'] = button_font

        self.disable_action_buttons()

        self.hit_button.grid(row = 1, column = 0, sticky = "NEWS")
        self.stand_button.grid(row = 1, column = 1, sticky = "NEWS")

        self.human_points_label = Label(text="", font = ("Arial", 25))
        self.human_points_label.grid(row = 2, column = 0)

        self.croupier_points_label = Label(text="", font = ("Arial", 25))
        self.croupier_points_label.grid(row = 2, column = 1)

        self.game_status = Text(width = 30, height = 5)
        self.game_status["state"] = DISABLED
        self.game_status.grid(row = 2, column = 0, columnspan = 2)

        self.player_cards_frame = Frame(bg = "green")
        self.player_cards_frame.grid(row = 3, column = 0, sticky="news")

        self.croupier_cards_frame = Frame(bg = "green")
        self.croupier_cards_frame.grid(row = 3, column = 1, sticky="news")

        self.mainWindow.grid_columnconfigure(0, weight = 1)
        self.mainWindow.grid_columnconfigure(1, weight = 1)
        self.mainWindow.grid_rowconfigure(0, weight = 1)
        self.mainWindow.grid_rowconfigure(1, weight = 1)
        self.mainWindow.grid_rowconfigure(2, weight = 1)
        self.mainWindow.grid_rowconfigure(3, weight = 20)

    def get_human_name(self) -> str:

        self.entry_button.wait_variable(self.button_pressed)
        self.entry_button["state"] = DISABLED
        self.entry["state"] = DISABLED

        return self.entry.get()

    def get_human_decision(self) -> str:
        self.hit_button.wait_variable(self.human_button_decision)

        return self.human_button_decision.get()

    def game_display(self, text):
        self.game_status["state"] = NORMAL
        self.game_status.insert(END, text + '\n')
        self.game_status["state"] = DISABLED

    def draw_card(self, card, parent_widget, card_number):
        if card._color in ['hearts', 'diamonds']:
            color = "red"
        else:
            color = "black"

        card_frame = Frame(parent_widget, width = CARD_WIDTH, height = CARD_HEIGHT)
        card_frame.place(x = 10 + (CARD_WIDTH + 10) * (card_number % CARDS_IN_ROW) + 10, y = 10 + (CARD_HEIGHT + 10) * (card_number // CARDS_IN_ROW))
        card_label_upper_left = Label(card_frame, text = str(card), font = ("Arial", 15), fg = color)
        card_label_lower_right = Label(card_frame, text = str(card), font = ("Arial", 15), fg = color)
        card_label_center_symbol = Label(card_frame, text = str(card)[-1], font = ("Arial", 40), fg = color)
        card_label_upper_left.place(x = 2, y = 2)
        card_label_lower_right.place(relx = 1, rely = 1, anchor = "se")
        card_label_center_symbol.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    def show_card(self, card, player):
        if player == "human":
            self.draw_card(card, self.player_cards_frame, GUI.player_cards)
            GUI.player_cards += 1
        elif player == "croupier":
            self.draw_card(card, self.croupier_cards_frame, GUI.croupier_cards)
            GUI.croupier_cards += 1

    def disable_action_buttons(self):
        self.hit_button["state"] = DISABLED
        self.stand_button["state"] = DISABLED

    def enable_action_buttons(self):
        self.hit_button["state"] = NORMAL
        self.stand_button["state"] = NORMAL

    def update_human_points(self, points):
        self.human_points_label["text"] = points

    def update_croupier_points(self, points):
        self.croupier_points_label["text"] = points