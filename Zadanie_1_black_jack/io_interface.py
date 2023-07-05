from tkinter import *

class IO:
    def __init__(self) -> None:
        pass

    def display(self, text):
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
        entry_label.pack()
        self.entry = Entry(fg="black", bg="white", width=50)
        self.entry.pack()
        self.button_pressed = StringVar()
        self.entry_button = Button(self.mainWindow, text="Enter", command=lambda: self.button_pressed.set("button pressed"))
        self.entry_button.pack()

        self.human_button_decision = StringVar()
        self.hit_button = Button(self.mainWindow, text="Hit", command=lambda: self.human_button_decision.set("h"))
        self.hit_button.pack()
        self.stand_button = Button(self.mainWindow, text="Stand", command=lambda: self.human_button_decision.set("s"))
        self.stand_button.pack()

        self.text_box = Text()
        self.text_box.pack()

        self.mainWindow.mainloop()

    def get_human_name(self) -> str:

        self.entry_button.wait_variable(self.button_pressed)

        return self.entry.get()

    def get_human_decision(self) -> str:
        self.hit_button.wait_variable(self.human_button_decision)

        return self.human_button_decision.get()

    def display(self, text):
        self.text_box.insert(END, text + '\n')
        
