# drill 10


from pico2d import *
from random import randint

open_canvas()
small_ball_image = load_image('./Lecture09_Game_Obejects/ball21x21.png')
big_ball_image = load_image('./Lecture09_Game_Obejects/ball41x41.png')
grass = load_image('./Lecture09_Game_Obejects/grass.png')

class Ball:
    def __init__(self, x, y, speed, flag):
        self.x = x
        self.y = y
        self.speed = speed
        self.flag = flag
        self.still_drop = True

    def drop(self):
        if self.still_drop:
            self.y -= self.speed
            if self.y < 60:
                still_drop = False
                self.y = 60

    def draw(self):
        if self.flag == 0:
            small_ball_image.draw(self.x, self.y)
        else:
            big_ball_image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def game_init():
    global running
    global balls
    running = True
    balls = [Ball(randint(100, 700), 599, randint(5, 15), randint(0, 1)) for i in range(0, 20)]

def game_loop():
    global running
    global balls
    while running:
        handle_events()
        clear_canvas()
        grass.draw(400, 30)
        for ball in balls:
            ball.drop()
            ball.draw()

        update_canvas()
        delay(0.05)


game_init()
game_loop()