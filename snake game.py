import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title('snake game by Diimmqt')
wn.bgcolor('green')
wn.setup (width=600, height = 600)
wn.tracer(0)

#createhead for snake
wn.mainloop ()

head =turtle.Turtle()
head.speed(0)
head.shape ('square')
head.color('black')
head.penup()
head.goto(0.0)
head.direction="stop"

while True:
    wn.update()

    move()

    time.sleep=(delay)

wn.mainloop()
