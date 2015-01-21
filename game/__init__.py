from browser import document, html, timer

import time 

SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None
SHIPSIZE = 30

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

    def main(self):
        
        SCREEN.width = WIDTH
        CTX.fillStyle = "green";
        CTX.fillRect(self.pos[0], self.pos[1], SHIPSIZE, SHIPSIZE)
        self.pos[0] += 1
        
        timer.set_timeout(self.main, 100)

init()
# menu()
game = Game()
game.main()
