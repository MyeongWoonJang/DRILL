import random
import turtle

move_px = 50

def restart():
    turtle.reset()

def upmove():
    turtle.setheading(90)
    turtle.forward(move_px)

def leftmove():
    turtle.setheading(180)
    turtle.forward(move_px)

def rightmove():
    turtle.setheading(0)
    turtle.forward(move_px)

def downmove():
    turtle.setheading(270)
    turtle.forward(move_px)

turtle.onkey(upmove, 'w')
turtle.onkey(leftmove, 'a')
turtle.onkey(downmove, 's')
turtle.onkey(rightmove, 'd')
turtle.onkey(restart, 'Escape')

turtle.listen()
