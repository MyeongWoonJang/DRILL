import random
from pico2d import *
import game_world
import game_framework

# 새의 크기 가로 50cm 세로 50cm로 하면 적절하겠다 생각했으나 boy에 비해 좀 작아보임
# 과감하게 2m로 결정
# 새의 비행 속도 80km / hour : 새니까 빠르긴 빨라야 하는데 애니메이션 시트 보니까 느려보임
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm, boy와 같아야 함
BIRD_SPEED_KMPH = 80.0  # Km / Hour
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)
BIRD_WIDTH_METER = 2.0
BIRD_HEIGHT_METER = 2.0
BIRD_WIDTH_PIXEL = BIRD_WIDTH_METER * PIXEL_PER_METER       # 픽셀 단위로 환산
BIRD_HEIGHT_PIXEL = BIRD_HEIGHT_METER * PIXEL_PER_METER     # 픽셀 단위로 환산

# 날갯짓 속도
# 1초에 2번 정도면 적당할 것 같은데 새가 생긴 게 좀 둔해보임
TIME_PER_ACTION = 0.6
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14      # 애니메이션 시트가 총 14프레임

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.speed = random.randint(int(BIRD_WIDTH_PIXEL), int(1600 - BIRD_WIDTH_PIXEL)), 500, BIRD_SPEED_PPS
        if random.randint(0, 1) == 1:
            self.dir = 1
        else:
            self.dir = -1
        self.frame = 0

    def update(self):
        self.x += self.dir * self.speed * game_framework.frame_time      # 속도 * 시간 = 변위
        if self.x < BIRD_WIDTH_PIXEL / 2.0 or self.x > 1600.0 - BIRD_WIDTH_PIXEL / 2.0:
            self.dir *= -1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    def draw(self):
        # 100 x 100
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x, self.y, BIRD_WIDTH_PIXEL, BIRD_HEIGHT_PIXEL)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, BIRD_WIDTH_PIXEL, BIRD_HEIGHT_PIXEL)
