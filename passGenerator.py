from tkinter import *
import random

class Cons:
    PASS_LEGNTH = 8
    GUI_WIDTH = 400
    GUI_HEIGHT = 400

class GUI(Frame):
    def __init__(self):
        super().__init__(height=Cons.GUI_HEIGHT,width=Cons.GUI_WIDTH)
        self.master.title("Random Password Generator - RPG")
        self.pack()
        self.initMain()
    def initMain(self):
        self.v1 = IntVar()
        Checkbutton(self, text='Include small letters',pady=10, variable=self.v1).grid(row=0, column = 0)
        self.v2 = IntVar()
        Checkbutton(self, text='Include Capital letters',pady=10, variable=self.v2).grid(row=1, column = 0)
        self.v3 = IntVar()
        Checkbutton(self, text='Include numbers (0-9)',pady=10, variable=self.v3).grid(row=2, column=0)
        self.v4 = IntVar()
        Checkbutton(self, text='Include random ascii chars (%/*#$^&)',pady=10, variable=self.v4).grid(row=3, column=0)
        self.v5 = IntVar()
        Checkbutton(self, text='Include ',pady=10, variable=self.v5).grid(row=4, column=0)
        self.v6 = IntVar()
        Checkbutton(self, text='Include ',pady=10, variable=self.v6).grid(row=5, column=0)
        btn = Button(self, text="Generate",pady=10, width = 10, command=self.generate).grid(columnspan=2, row=7,column=0)
    def generate(self):
        password = []
        z = 0
        while z < Cons.PASS_LEGNTH:
            small_letter = random.randint(97, 122)
            capital_letter = random.randint(65,90)
            random_number = random.randint(0, 9)
            random_char1 = random.randint(58, 64)
            random_char2 = random.randint(33,47)
            i = random.randint(0,4)
            if i == 0 and bool(self.v1.get()):
                password.append(chr(small_letter))
            elif i == 1 and bool(self.v2.get()):
                password.append(chr(capital_letter))
            elif i == 2 and bool(self.v3.get()):
                password.append(chr(random_number))
            elif i == 3 and bool(self.v4.get()):
                password.append(chr(random_char1))
            elif i == 4 and bool(self.v4.get()):
                password.append(chr(random_char2))
            z+=1
        Label(self, text=password).grid(row = 8, column = 0)
def main():
    root = Tk()
    loop = GUI()
    root.mainloop()

if __name__ == '__main__':
    main()