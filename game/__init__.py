import random

from browser import document, html, timer, window


SIZE = WIDTH, HEIGHT = 640, 480
SCREEN = None
CTX = None
SHIPSIZE = 30

SHIPCOLOR = "#0fd"
SHOTCOLOR = "#d00"
ENEMYCOLOR = "#fff"

images = {}

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
    for image_name in "ship", "enemy_01", "enemy_02":
        images[image_name] = html.IMG(src="/images/{}.png".format(image_name))
        print("loaded {}.png".format(image_name))

def gameover():
    global game
    document.get(selector="h1")[0].text= "Game Over"


class GameObject:
    def __init__(self, pos=None):
        self.pos = pos
        self.width = SHIPSIZE
        self.height = SHIPSIZE
        self.update_rect()

        self.image_counter = 0
        self.image_index = 0
        # Put object animation image names in a "self.image_names" list 
        # and the starting image object in self.image

    def update(self):
        self.update_screen()

        self.image_counter += 1
        if hasattr(self, "image_names") and not self.image_counter % 40:
            self.image_index += 1
            if self.image_index >= len(self.image_names):
                self.image_index = 0
            self.image = images[self.image_names[self.image_index]]

    def update_screen(self):
        if hasattr(self, "image"):
            CTX.drawImage(self.image, self.pos[0], self.pos[1])
        else:
            CTX.fillStyle = self.color
            # call with *self.rect not working with Brython 3.0.2
            CTX.fillRect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def update_rect(self):
        self.rect = (self.pos[0], self.pos[1], self.width, self.height)

    def intersect(self, other):
        left = self.rect[0]
        right = left + self.rect[2]
        top = self.rect[1]
        botton = self.rect[1] + self.rect[3]
        if ( (left >= other.rect[0] and left <= other.rect[0] + other.rect[2] or
              right >= other.rect[0] and right <= other.rect[0] + other.rect[2] or
              left <= other.rect[0] and right >= other.rect[0]) and
            
              (top >= other.rect[1] and top <= other.rect[1] + other.rect[3] or
               botton >= other.rect[1] and botton <= other.rect[1] + other.rect[3] or
               top <= other.rect[1]  and botton >= other.rect[1])
         ):
            return True
        return False


class Shot(GameObject):
    def __init__(self, pos):
        pos = [pos[0] - SHIPSIZE / 8, pos[1] - SHIPSIZE]
        self.speed = -10
        self.color = SHOTCOLOR
        super(Shot, self).__init__(pos)
        self.width = SHIPSIZE / 4
        self.update_rect()


    def update(self):
        super(Shot, self).update()
        self.pos[1] += self.speed
        if self.pos[1] <= 0:
            return False
        self.update_rect()
        return True

    def hit_any_enemy(self, enemy_list):
        finished = []
        for i, enemy in enumerate(enemy_list):
            if self.intersect(enemy):
                finished.append(i)
                enemy.die()
        for i in reversed(finished):
            del enemy_list[i]


class Enemy(GameObject):
    def __init__(self, pos):
        self.speed = 5
        self.color = ENEMYCOLOR
        super(Enemy, self).__init__(pos)
        self.image = images["enemy_01"]
        self.image_names = ["enemy_01", "enemy_02"]


    def update(self):
        super(Enemy, self).update()
        self.pos[0] += self.speed
        if self.pos[0] + self.width > WIDTH or self.pos[0] < 0:
            self.speed = -self.speed
            self.pos[0] += self.speed
            self.pos[1] += SHIPSIZE * 2
        if self.pos[1] >= HEIGHT:
            gameover()
        self.update_rect()

    def die(self):
        print("Ouch")


class Ship(GameObject):
    def __init__(self, game):
        self.game = game
        pos = [(WIDTH - SHIPSIZE) / 2, HEIGHT - SHIPSIZE]

        super(Ship, self).__init__(pos)

        self.speed = 0

        self.aceleration = 0
        self.max_speed = 15

        self.image = images["ship"]
        document.body.onkeydown = self.keypress

    def update(self):
        super(Ship, self).update()

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

    def keypress(self, event):
        if event.keyCode == K_RIGHT:
            self.aceleration += 10
        elif event.keyCode == K_LEFT:
            self.aceleration -= 10
        elif event.keyCode == K_UP:
            self.speed = 0
            self.aceleration = 0
        elif event.keyCode == K_SPACE:
            self.game.shots.append(Shot((self.pos[0] + SHIPSIZE / 2, self.pos[1])))

class Game:
    def __init__(self):

        self.ship = Ship(self)
        self.shots = []
        self.enemies = [Enemy([20,20])]

    def clear_screen(self):
        SCREEN.width = WIDTH

    def main(self):
        self.clear_screen()
        self.ship.update()

        for enemy in self.enemies:
            enemy.update()

        finished = []

        for i, shot in enumerate(self.shots):
            if not shot.update():
                finished.append(i)
            shot.hit_any_enemy(self.enemies)

        for i in reversed(finished):
            del self.shots[i]

        timer.set_timeout(self.main, 30)





init()
# menu()
game = Game()
game.main()
