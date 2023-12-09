import random
import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

MOVE_SPEED = [2, 3, 3, 2, 2]
BULLET_SPEED = [4, 5, 5, 6, 6]
BULLET_DAMAGE = [1, 1, 2, 2, 3]
SHOT_DELAY = [60, 50, 40, 40, 30]


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
font_menu = pygame.font.Font(None, 50)
font_menu_select = pygame.font.Font(None, 60)
font_big = pygame.font.Font(None, 70)
font_title = pygame.font.Font(None, 140)
# images

img_brick = pygame.image.load('images/block_brick.png')
img_armor = pygame.image.load('images/block_armor.png')
img_bushes = pygame.image.load('images/block_bushes.png')
img_water = pygame.image.load('images/block_water.png')
img_ice = pygame.image.load('images/block_ice.png')

img_shield_1 = pygame.image.load('images/shield.png')

img_bonuses = [
    # pygame.image.load('images/bonus_bomb.png'),
    pygame.image.load('images/bonus_helmet.png'),
    # pygame.image.load('images/bonus_shovel.png'),
    pygame.image.load('images/bonus_star.png'),
    pygame.image.load('images/bonus_tank.png'),
    # pygame.image.load('images/bonus_time.png')
    ]
img_bangs = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png')
    ]
img_tanks = [
    pygame.image.load('images/tank1.png'),
    pygame.image.load('images/tank2.png'),
    pygame.image.load('images/tank3.png'),
    pygame.image.load('images/tank4.png'),
    pygame.image.load('images/tank8.png')
    ]
# sounds
snd_shot = pygame.mixer.Sound('sounds/shot.wav')
snd_destroy = pygame.mixer.Sound('sounds/destroy.wav')
snd_dead = pygame.mixer.Sound('sounds/dead.wav')
snd_move = pygame.mixer.Sound('sounds/move.wav')
snd_live = pygame.mixer.Sound('sounds/live.wav')
snd_star = pygame.mixer.Sound('sounds/star.wav')
snd_start = pygame.mixer.Sound('sounds/level_start.mp3')

# interface block
class Interface:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = font.render(str(obj.rank+1), 1, 'black')
                rect = text.get_rect(center=(5 + i * 70 + 11, 5 + 11))
                window.blit(text, rect)

                text = font.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 15))
                window.blit(text, rect)
                i += 1


# objects block
class Tank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'
        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.shotTimer = 0
        self.hp = 5

        self.bulletSpeed = 4
        self.bulletDamage = 1
        self.moveSpeed = 2
        self.shotDelay = 60

        self.helmet = 0
        self.img_h = img_shield_1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.rank = 0
        self.image = pygame.transform.rotate(img_tanks[self.rank], (-self.direct * 90))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        #snd_move.play()
        self.image = pygame.transform.rotate(img_tanks[self.rank], (-self.direct * 90))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)

        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]

        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self \
                    and (obj.type == 'block'
                         or obj.type == 'arm_block'
                         or obj.type == 'water'
                         or obj.type == 'tank') \
                    and self.rect.colliderect(obj.rect)\
                    or self.rect.x > WIDTH-32 or self.rect.y > HEIGHT-32 or self.rect.y < 32 or self.rect.x < 0:
                self.rect.topleft = oldX, oldY
            oldX2, oldY2 = self.rect.topleft
            if obj.type == 'ice' and self.rect.colliderect(obj.rect):
                if keys[self.keyLEFT]:
                    self.rect.x -= self.moveSpeed + 1
                    self.direct = 3
                elif keys[self.keyRIGHT]:
                    self.rect.x += self.moveSpeed + 1
                    self.direct = 1
                elif keys[self.keyUP]:
                    self.rect.y -= self.moveSpeed + 1
                    self.direct = 0
                elif keys[self.keyDOWN]:
                    self.rect.y += self.moveSpeed + 1
                    self.direct = 2

                for obj in objects:
                    if obj != self \
                            and (obj.type == 'block'
                                 or obj.type == 'arm_block'
                                 or obj.type == 'water'
                                 or obj.type == 'tank') \
                            and self.rect.colliderect(obj.rect)\
                            or self.rect.x > WIDTH-32 or self.rect.y > HEIGHT-32 or self.rect.y < 32 or self.rect.x < 0:
                        self.rect.topleft = oldX2, oldY2

        if keys[self.keySHOT] and self.shotTimer == 0:
            snd_shot.play()
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)

            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)
        if self.helmet > 0:
            window.blit(self.image, self.rect)
            window.blit(self.img_h, self.rect)

    def damage(self, value):
        if self.helmet > 0:
            self.helmet -= 1
        else:
            self.hp -= value
            if self.hp <= 0:
                objects.remove(self)
                snd_dead.play()
                print(self.color, 'dead')


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent \
                        and obj.type != 'bonus' \
                        and obj.type != 'bang' \
                        and obj.type != 'bushes' \
                        and obj.type != 'water' \
                        and obj.type != 'ice' \
                        and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    snd_destroy.play()
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)


class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'
        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.3
        if self.frame >= 3:
            objects.remove(self)

    def draw(self):
        image = img_bangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)


class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        window.blit(img_brick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)


class ArmourBlock(Block):
    def __init__(self, px, py, size):
        super().__init__(px, py, size)
        objects.append(self)
        self.type = 'arm_block'
        self.hp = 999

    def draw(self):
        window.blit(img_armor, self.rect)


class Bushes(Block):
    def __init__(self, px, py, size):
        super().__init__(px, py, size)
        objects.append(self)
        self.type = 'bushes'

    def draw(self):
        window.blit(img_bushes, self.rect)


class Water(Block):
    def __init__(self, px, py, size):
        super().__init__(px, py, size)
        objects.append(self)
        self.type = 'water'

    def draw(self):
        window.blit(img_water, self.rect)


class Ice(Block):
    def __init__(self, px, py, size):
        super().__init__(px, py, size)
        objects.append(self)
        self.type = 'ice'

    def draw(self):
        window.blit(img_ice, self.rect)


class Bonus:
    def __init__(self, px, py, bonus_n):
        objects.append(self)
        self.type = 'bonus'

        self.image = img_bonuses[bonus_n]
        self.rect = self.image.get_rect(center=(px, py))

        self.timer = 600
        self.bonus_n = bonus_n

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            objects.remove(self)

        for obj in objects:
            if obj.type == 'tank' and self.rect.colliderect(obj.rect):
                if self.bonus_n == 0: # hp+1
                    if obj.helmet == 0:
                        obj.helmet += 1
                        snd_live.play()
                        objects.remove(self)
                        break
                elif self.bonus_n == 1: # hp+1
                    obj.hp += 1
                    snd_live.play()
                    objects.remove(self)
                    break
                elif self.bonus_n == 2: # rank+1
                    if obj.rank < len(img_tanks) and obj.rank < 4:
                        obj.rank += 1
                        snd_star.play()
                        objects.remove(self)
                        break

    def draw(self):
        if self.timer % 30 < 15:
            window.blit(self.image, self.rect)


objects = []
bullets = []
Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('red', 675, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))
ui = Interface()

# block-build algorythm
for _ in range(200): # 200
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect):
                fined = True

        if not fined:
            break
    r = random.randint(0, 4)
    if r == 0:
        Block(x, y, TILE)
    elif r == 1:
        Bushes(x, y, TILE)
    elif r == 2:
        Water(x, y, TILE)
    elif r == 3:
        Ice(x, y, TILE)
    else:
        ArmourBlock(x, y, TILE)

bonus_timer = 100
timer = 0
y = 0


# game - RUN function
def game_run():

    window.fill('black')

    for obj in objects:
        obj.update()

    for obj in bullets:
        obj.update()

    ui.update()

    for obj in objects:
        if obj.type == 'water' or obj.type == 'ice':
            obj.draw()

    for obj in bullets:
        obj.draw()

    for obj in objects:
        if obj.type != 'water' and obj.type != 'ice':
            obj.draw()

    ui.draw()

    global bonus_timer
    if bonus_timer > 0:
        bonus_timer -= 1
    else:
        Bonus(randint(50, WIDTH - 50), randint(50, HEIGHT - 50), randint(0, len(img_bonuses)-1))
        bonus_timer = randint(240, 360)


# main cycle
snd_start.play()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    game_run()

    # start screen
    if timer < 260:
        y += 2
        pygame.draw.rect(window, 'black', (WIDTH // 2 - 300, HEIGHT // 2 - 200 + y, 600, 250))
        pygame.draw.rect(window, 'orange', (WIDTH // 2 - 300, HEIGHT // 2 - 200 + y, 600, 250), 3)
        text = font_title.render('Т А Н К И', 1, 'white')
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100 + y))
        window.blit(text, rect)
        text = font_big.render('ОДИН НА ОДИН', 1, 'white')
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20 + y))
        window.blit(text, rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
