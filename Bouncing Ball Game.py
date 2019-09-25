from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle,color):
        self.canvas = canvas # NOT SURE - defines what canvas is
        self.paddle = paddle
        self.id =canvas.create_oval(10, 10, 25, 25, fill=color) # Creates ball
        self.canvas.move(self.id, 245, 100) # Moves the ball to starting position
        starts = [-2, -1, 1, 2] # List of possible starting speeds in the x direction
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3 # Starting y speed
        self.canvas_height = self.canvas.winfo_height() # Retrieves the height of the canvas
        self.canvas_width = self.canvas.winfo_width() # Retrieves the width
        self.hit_bottom = False # Boolean variable to check if balls hits the bottom

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        else:
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) # How the ball moves on the screen
        pos = self.canvas.coords(self.id) # Retrieves coordinates of the ball. It is a list of 4 numbers: the first pair are the top left coordinates of the ball; the latter are the bottom right of the ball
        if pos[1] <= 0: # If top, left side hits the top of the screen.
            self.y = 2
        if pos[3] >= self.canvas_height: # If the bottom, right side hits the bottom of the screen.
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0: # If left side hits the left of the screen
            self.x = 2
        if pos[2] >= self.canvas_width: # If the right side hits the right of the screen.
            self.x = -2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -3

    def turn_right(self, event):
        self.x = 3



tk = Tk()
tk.title('Bouncing Ball Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'purple')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)