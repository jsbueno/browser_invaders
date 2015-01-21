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

def main():
    pos = [320, 240]
    #while True:
        CTX.fillStyle = "green";
        CTX.fillRect(pos[0], pos[1], SHIPSIZE, SHIPSIZE)
        time.sleep(100) # does not work, actually
        pos[0] += 1
        SCREEN.width = WIDTH

init()
# menu()
main()
