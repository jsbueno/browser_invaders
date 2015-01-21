

from browser import document, html, timer

import time 

SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None
SHIPSIZE = 30

SHIPCOLOR = "#0fd"
SHOTCOLOR = "#d00"

K_LEFT = 37
K_RIGHT = 39
K_UP = 38
K_DOWN = 40
K_SPACE = 32
K_ESCAPE = 27

def init():
    global SCREEN, CTX
    document.body.append(html.H1("Space Invaders - a Python adventure"))
    SCREEN = html.CANVAS(width=640, height=480)
    SCREEN.style = {"background": "black"}
    document.body.append(SCREEN)
    CTX = SCREEN.getContext("2d")



class Shot:
    def __init__(self, pos):
        self.pos = [pos[0] - SHIPSIZE / 8, pos[1] - SHIPSIZE]
        self.speed = -10
        self.update_rect()

    def update_screen(self):
        CTX.fillStyle = SHOTCOLOR
        # call with *self.rect not working with Brython 3.0.2
        CTX.fillRect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def update(self):
        self.update_screen()
        self.pos[1] += self.speed
        if self.pos[1] <= 0:
            return False
        self.update_rect()
        return True

    def update_rect(self):
        self.rect = (self.pos[0], self.pos[1], SHIPSIZE / 4, SHIPSIZE)

class Game:
    def __init__(self):
        document.body.onkeydown = self.keypress
        self.pos = [(WIDTH - SHIPSIZE) / 2, HEIGHT - SHIPSIZE]
        self.speed = 0

        self.aceleration = 0
        self.max_speed = 15
        self.shots = []

    def update_screen(self):
        SCREEN.width = WIDTH

        CTX.fillStyle = SHIPCOLOR
        CTX.fillRect(self.pos[0], self.pos[1], SHIPSIZE, SHIPSIZE)

    def movement(self):
        self.speed += self.aceleration

        self.speed *= 0.9

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < -self.max_speed:
            self.speed = - self.max_speed

        self.aceleration += 1 if self.aceleration < 0 else (-1 if self.aceleration > 0 else 0)

        self.pos[0] += self.speed
        if self.pos[0] > WIDTH - SHIPSIZE:
            self.aceleration = self.speed = 0
            self.pos[0] = WIDTH - SHIPSIZE
        elif self.pos[0] < 0:
            self.aceleration = self.speed = 0
            self.pos[0] = 0

    def main(self):
        self.update_screen()
        self.movement()

        finished = []
        for i, shot in enumerate(self.shots):
            if not shot.update():
                finished.append(i)

        for i in reversed(finished):
            del self.shots[i]

        timer.set_timeout(self.main, 30)

    def keypress(self, event):
        if event.keyCode == K_RIGHT:
            self.aceleration += 10
        elif event.keyCode == K_LEFT:
            self.aceleration -= 10
        elif event.keyCode == K_UP:
            self.speed = 0
            self.aceleration = 0
        elif event.keyCode == K_SPACE:
            self.shots.append(Shot((self.pos[0] + SHIPSIZE / 2, self.pos[1])))

        # print(event, event.keyCode)

init()
# menu()
game = Game()
game.main()
