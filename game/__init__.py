

from browser import document, html, timer

import time 

SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None
SHIPSIZE = 30

SHIPCOLOR = "#0fd"

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
    CTX = SCREEN.getContext("2d");

class Game:
    def __init__(self):
        self.pos = [(WIDTH - SHIPSIZE) / 2, HEIGHT - SHIPSIZE]
        self.speed = 0
        
        self.aceleration = 0
        self.max_speed = 15
        
        document.body.onkeydown = self.keypress

    def main(self):
        SCREEN.width = WIDTH
        
        CTX.fillStyle = SHIPCOLOR
        CTX.fillRect(self.pos[0], self.pos[1], SHIPSIZE, SHIPSIZE)
        
        self.speed += self.aceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < -self.max_speed:
            self.speed = - self.max_speed

        self.aceleration += 1 if self.aceleration < 0 else (-1 if self.aceleration > 0 else 0)
        
        self.pos[0] += self.speed
        if self.pos[0] > WIDTH - SHIPSIZE:
            self.speed = 0
            self.pos[0] = WIDTH - SHIPSIZE
        elif self.pos[0] < 0:
            self.speed = 0
            self.pos[0] = 0
        
        timer.set_timeout(self.main, 30)
    
    def keypress(self, event):
        if event.keyCode == K_RIGHT:
            self.aceleration += 10
        elif event.keyCode == K_LEFT:
            self.aceleration -= 10
            
        # print(event, event.keyCode)
        

init()
# menu()
game = Game()
game.main()
