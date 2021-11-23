
import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from bird import Bird

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []


def collide(a, b):
    a_xmin, a_ymin, a_xmax, a_ymax = a.get_bb()
    b_xmin, b_ymin, b_xmax, b_ymax = b.get_bb()

    if a_xmin > b_xmax: return False
    if b_xmin > a_xmax: return False
    if a_ymin > b_ymax: return False
    if b_ymin > a_ymax: return False
    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    for _ in range(5):
        game_world.add_object(Bird(), 1)

    global balls
    balls = [Ball() for _ in range(10)] + [BigBall() for _ in range(10)]
    game_world.add_objects(balls, 1)

    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)

    for ball in balls:
        if collide(grass, ball):
            ball.stop()

    delay(1.5)

    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






