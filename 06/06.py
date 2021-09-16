from pico2d import *
import math

open_canvas()

grass = load_image('./Lecture04_2D_Rendering/grass.png')
character = load_image('./Lecture04_2D_Rendering/character.png')

#---------------------------------------------

dir = 0
run_px = 5
width = 800
height = 600
space = 200

def nextdir(dir):
    return (dir + 90) % 360

def out(me):
    return me.x > width - space or me.x < space or me.y > height - space * 2 or me.y < 90

class chara:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def run(self, px, deg):
        self.x += px * math.cos(math.radians(deg))
        self.y += px * math.sin(math.radians(deg))

    def draw(self):
        character.draw_now(self.x, self.y)

def rectmove(me):
    while True:
        global dir
        me.run(5, dir)
        if out(me):
            me.run(-5, dir)
            dir = nextdir(dir)
        clear_canvas_now()
        me.draw()
        grass.draw_now(400, 30)
        delay(0.01)

def circlemove(me):
    while True:
        global dir
        me.run(5, dir)
        dir = dir + 2
        clear_canvas_now()
        me.draw()
        grass.draw_now(400, 30)
        delay(0.01)

me = chara(400, 90)
me.draw()
grass.draw_now(400, 30)

print('''
l 입력 시 사각형 움직임
c 입력 시 원 움직임
''')

press = input()
# 오류 처리 생략
if press == 'l':
    rectmove(me)
elif press == 'c':
    circlemove(me)

#---------------------------------------------

close_canvas()