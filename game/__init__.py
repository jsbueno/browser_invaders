from browser import document, html, timer

import time 

SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None
SHIPSIZE = 30

SHIPCOLOR = "#0fd"

def init():
    global SCREEN, CTX
    document.body.append(html.H1("Space Invaders - a Python adventure"))
    SCREEN = html.CANVAS(width=640, height=480)
    SCREEN.style = {"background": "black"}
    document.body.append(SCREEN)
    CTX = SCREEN.getContext("2d");

class Game:
    def __init__(self):
        self.pos = [320, 240]
        self.speed = 5

    def main(self):
        SCREEN.width = WIDTH
        
        CTX.fillStyle = SHIPCOLOR;
        CTX.fillRect(self.pos[0], self.pos[1], SHIPSIZE, SHIPSIZE)
        self.pos[0] += self.speed
        if self.pos[0] > WIDTH - SHIPSIZE:
            self.speed = - self.speed
            self.pos[0] = WIDTH - SHIPSIZE
        elif self.pos[0] < 0:
            self.speed = -self.speed
            self.pos[0] = 0
        
        timer.set_timeout(self.main, 30)

init()
# menu()
game = Game()
game.main()
