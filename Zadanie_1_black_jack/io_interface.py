from tkinter import *

class IO:
    def __init__(self) -> None:
        pass

    def game_display(self, text):
        print(text)

    def human_display(self, text):
        print(text)
    
    def croupier_display(self, text):
        print(text)

    def get_human_name(self) -> str:
        return input("What is your name? ")

    def get_human_decision(self) -> str:
        return input("(s)tand or (h)it? ")
    
class GUI(IO):
    def __init__(self) -> None:
        self.mainWindow = Tk()
        self.mainWindow.geometry("800x600")
        self.mainWindow.title("Black Jack")

        entry_label = Label(text="What is your name? ")
        entry_label.grid(row = 0, column = 0)
        self.entry = Entry(fg="black", bg="white", width=50)
        self.entry.grid(row = 0, column = 1)
        self.button_pressed = StringVar()
        self.entry_button = Button(self.mainWindow, text="Enter", command=lambda: self.button_pressed.set("button pressed"))
        self.entry_button.grid(row = 0, column = 2)

        self.human_button_decision = StringVar()
        self.hit_button = Button(self.mainWindow, text="Hit", command=lambda: self.human_button_decision.set("h"))
        self.hit_button.grid(row = 1, column = 0)
        self.stand_button = Button(self.mainWindow, text="Stand", command=lambda: self.human_button_decision.set("s"))
        self.stand_button.grid(row = 1, column = 1)

        self.game_status = Text(width = 40, height = 5)
        self.game_status.grid(row = 2, column = 0, columnspan = 2)

        self.player_cards = Text(width = 40)
        self.player_cards.grid(row = 3, column = 0)

        self.croupier_cards = Text(width = 40)
        self.croupier_cards.grid(row = 3, column = 1)

        #self.mainWindow.mainloop()

    def get_human_name(self) -> str:

        self.entry_button.wait_variable(self.button_pressed)

        return self.entry.get()

    def get_human_decision(self) -> str:
        self.hit_button.wait_variable(self.human_button_decision)

        return self.human_button_decision.get()

    def game_display(self, text):
        self.game_status.insert(END, text + '\n')

    def human_display(self, text):
        self.player_cards.insert(END, text + '\n')
    
    def croupier_display(self, text):
        self.croupier_cards.insert(END, text + '\n')
        
