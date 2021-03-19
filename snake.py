from tkinter import *
import random
import sys

class Cons:
    bg = "black"
    height = 400
    width = 400
    DELAY = 100
    DOT_SIZE = 10
    STEP_SIZE = 10

class Board(Canvas):
    def __init__(self):
        super().__init__(bg=Cons.bg, height=Cons.height, width=Cons.width)
        self.initGame()
        self.pack()
    
    def initGame(self):
        self.isInGame = True
        self.moveX = 200
        self.moveY = 200
        self.toMoveX = 10
        self.toMoveY = 0
        self.player()
        self.drawSnake()
        self.drawApples()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)
    def appleCollosion(self):
        apple = self.find_withtag("apple")
        c = self.coords(apple)
        snake = self.find_withtag("snake")
        last = len(snake)-1
        c1 = self.coords(snake[last])
        over = self.find_overlapping(c[0], c[1], c[2], c[3])
        if over[0] != apple[0]:
            self.delete(apple[0])
            self.score +=1
            self.drawApples()
            self.create_rectangle(c1[0]- Cons.DOT_SIZE, c1[1], c1[2]-Cons.DOT_SIZE, c1[3], fill="white", tag="snake")
    def onCollosion(self):
        self.appleCollosion()
        if self.moveX > 400 or self.moveX < 0 or self.moveY > 400 or self.moveY < 0:
            self.gameOver()
    def gameOver(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() /2, self.winfo_height()/2,
            text="Game Over with score {0}".format(self.score), fill="white")
        self.create_text(self.winfo_width() /2, self.winfo_height()/2 +20,
            text="Replay", fill="white")
    def player(self):
        self.score = 0
    def drawApples(self):
        self.appleX = random.randrange(200)
        self.appleY = random.randrange(200)
        self.create_rectangle(self.appleX, self.appleY, self.appleX+10, self.appleY+10, fill="green", tag="apple")
    def drawSnake(self):
        for i in range(self.score + 2):
            self.create_rectangle(self.moveX- i*Cons.DOT_SIZE, self.moveY, self.moveX-(i-1)*Cons.DOT_SIZE, self.moveY+Cons.DOT_SIZE, fill="white", tag="snake")
    def moveSnake(self):
        head = self.find_withtag("snake")
        self.moveX += self.toMoveX
        self.moveY += self.toMoveY
        z = len(head)
        
        while z > 0:
            c1 = self.coords(head[z-2])
            c0 = self.coords(head[z-1])
            self.move(head[z-1], c1[0]-c0[0], c1[1]-c0[1])
            z-=1
        self.move(head[z], self.toMoveX, self.toMoveY)
    def onKeyPressed(self, e):
        key = e.keysym
        UP_CURSOR_KEY = "Up"
        if key == UP_CURSOR_KEY:
            self.toMoveX = 0
            self.toMoveY = -Cons.STEP_SIZE
        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY:
            self.toMoveX = 0
            self.toMoveY = Cons.STEP_SIZE
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY:
            self.toMoveX = Cons.STEP_SIZE
            self.toMoveY = 0
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY:
            self.toMoveX = -Cons.STEP_SIZE
            self.toMoveY = 0
    def onTimer(self):
        self.onCollosion()
        if self.isInGame:
            self.onCollosion()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()

class Game(Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Snake')
        self.board = Board()
        self.pack()      

def main():
    root = Tk()
    g = Game()
    root.mainloop()

if __name__ == '__main__':
    main()