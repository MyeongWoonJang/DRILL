from pico2d import *
import math

open_canvas()

grass = load_image('./Lecture04_2D_Rendering/grass.png')
character = load_image('./Lecture04_2D_Rendering/character.png')

#---------------------------------------------

def render_all(x, y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def run_circle():
    cx, cy, r = 400, 300, 200
    for degree in range(-90, 270, 5):
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        render_all(x, y)

def run_rectangle():
    print('RECTANGLE')

    # bottom line
    for x in range(50, 750+1, 10):
        render_all(x, 90)

    # right line
    for y in range(90, 550+1, 10):
        render_all(750, y)

    # top line
    for x in range(750, 50-1, -10):
        render_all(x, 550)


     # left line
    for y in range(550, 90-1, -10):
        render_all(50, y)

while True:
    run_circle()
    run_rectangle()
    break

#---------------------------------------------

close_canvas()