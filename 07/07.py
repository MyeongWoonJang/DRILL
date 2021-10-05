from pico2d import *
from random import randint
import math

open_canvas()
sheet = load_image('./Lecture07_Linear_Movement/animation_sheet.png')
hand = load_image('./Lecture07_Linear_Movement/hand_arrow.png')
ground = load_image('./Lecture07_Linear_Movement/KPU_GROUND.png')

# ---------------------------------------------

hand_x, hand_y = 0, 0
ch_x, ch_y = 400, 300
radian = 0
row = 1
pi = 3.141592
frame = 0

running = True

def init():
    global hand_x
    global hand_y
    global pi
    global row
    global radian

    hand_x, hand_y = randint(0, 800), randint(0, 600)

    if hand_x > ch_x:
        row = 1
    else:
        row = 0

    if math.fabs(hand_x - ch_x) < 4:
        if hand_y > ch_y:
            radian = pi / 2
        else:
            radian = -(pi / 2)
    else:
        radian = math.atan((hand_y - ch_y) / (hand_x - ch_x))
        if hand_x < ch_x:
            radian += pi


def move():
    global ch_x
    global ch_y
    ch_x += 10 * math.cos(radian)
    ch_y += 10 * math.sin(radian)


init()
while running:
    clear_canvas()

    if math.fabs(ch_x - hand_x) < 8 and math.fabs(ch_y - hand_y) < 8:
        init()
    move()

    ground.draw(400, 300)
    hand.draw(hand_x, hand_y)
    sheet.clip_draw(frame * 100, 100 * row, 100, 100, ch_x, ch_y)
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

# ---------------------------------------------

close_canvas()
