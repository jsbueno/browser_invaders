from browser import document, html, timer

SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None

def init():
    global SCREEN, CTX
    document.body.append(html.H1("Space Invaders - a Python adventure"))
    SCREEN = html.CANVAS(width=640, height=480)
    SCREEN.style = {"background": "black"}
    document.body.append(SCREEN)
    CTX = SCREEN.getContext("2d");




init()
# menu()
#main()
