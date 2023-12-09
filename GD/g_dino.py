import pygame
from random import randint, choice

pygame.init()

WIDTH, HEIGHT = 1000, 400
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# images
img_main = pygame.image.load('images/sprites.png').convert_alpha()
img_dino_stand = [img_main.subsurface(1514, 2, 88, 94),
                  img_main.subsurface(1602, 2, 88, 94)]
img_dino_sid = [img_main.subsurface(1866, 36, 118, 60),
                img_main.subsurface(1984, 36, 118, 60)]
img_dino_lose = [img_main.subsurface(1690, 2, 88, 94)]
img_cactus = [  img_main.subsurface(446, 2, 34, 70),
                img_main.subsurface(480, 2, 68, 70),
                img_main.subsurface(512, 2, 102, 70),
                img_main.subsurface(512, 2, 68, 70),
                img_main.subsurface(652, 2, 50, 100),
                img_main.subsurface(752, 2, 98, 100),
                img_main.subsurface(850, 2, 102, 100)]
img_pter = [img_main.subsurface(260, 0, 92, 82),
            img_main.subsurface(352, 0, 92, 82)]
img_g_over = img_main.subsurface(2, 2, 72, 64)
# sounds
snd_jump = pygame.mixer.Sound('sounds/jump.wav')
snd_level_up = pygame.mixer.Sound('sounds/levelup.wav')
snd_game_over = pygame.mixer.Sound('sounds/gameover.wav')


font_score = pygame.font.Font(None, 30)

img_ground = img_main.subsurface(2, 104, 2400, 26)

py, sy = 380, 0
is_stand = False
frame = 0
speed = 10
scores = 0
level = 0

backgrounds = [pygame.Rect(0, HEIGHT - 50, 2400, 26)]
objects = []
timer = 0
best_score = 0


class Enemy:
    def __init__(self):
        objects.append(self)

        if randint(0, 4) == 0 and scores > 350:# or 1:
            self.image = img_pter
            self.speed = 3
            py = HEIGHT - 30 - randint(0, 2) * 40
        else:
            self.image = [choice(img_cactus)]
            self.speed = 0
            py = HEIGHT - 20

        self.rect = self.image[0].get_rect(bottomleft=(WIDTH, py))
        self.frame = 0

    def update(self):
        global speed, timer, sy

        self.rect.x -= speed + self.speed
        self.frame = (self.frame + 0.1) % len(self.image)

        if self.rect.colliderect(dino_rect) and speed != 0:
            #print('bang')
            snd_game_over.play()
            speed = 0
            timer = 60
            sy = - 10

        if self.rect.right < 0:
            objects.remove(self)

    def draw(self):
        window.blit(self.image[int(self.frame)], self.rect)

#def game():


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    #game()
    keys = pygame.key.get_pressed()
    b1, b2, b3 = pygame.mouse.get_pressed()
    press_jump = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]
    press_sit = keys[pygame.K_RCTRL] or keys[pygame.K_s] or keys[pygame.K_DOWN]

    if (press_jump or press_sit) and speed == 0 and timer == 0:
        py, sy = 380, 0
        is_stand = False
        frame = 0
        speed = 10
        scores = 0
        objects = []

    if press_jump and is_stand and speed > 0:
        snd_jump.play()
        sy = -22

    if is_stand:
        frame = (frame + speed / 35) % 2

    py += sy
    sy = (sy + 1) * 0.97

    is_stand = False

    if py > HEIGHT - 20:
        py, sy, is_stand = HEIGHT - 20, 0, True

    if speed == 0:
        dino_image = img_dino_lose[0]
        if scores >= best_score:
            best_score = scores
    elif press_sit:
        dino_image = img_dino_sid[int(frame)]
    else:
        dino_image = img_dino_stand[int(frame)]

    dw, dh = dino_image.get_width(), dino_image.get_height()
    dino_rect = pygame.Rect(150, py - dh, dw, dh)

    for i in range(len(backgrounds)-1, -1, -1):
        bg = backgrounds[i]
        bg.x -= speed

        if bg.right < 0:      # bg.right < 0 and backgrounds.pop(i)
            backgrounds.pop(i)

    if backgrounds[-1].right < WIDTH:
        backgrounds.append(pygame.Rect(backgrounds[-1].right, HEIGHT - 50, 2400, 26))

    for i in objects:
        i.update()

    if timer > 0:
        timer -= 1
    elif speed > 0:
        timer = randint(100, 150)
        Enemy()

    scores += speed / 50

    if speed > 0:
        speed = 10 + scores // 100

    if scores // 100 > level:
        level += 1
        snd_level_up.play()

    window.fill('white')

    for bg in backgrounds:
        window.blit(img_ground, bg)

    for i in objects:
        i.draw()

    window.blit(dino_image, dino_rect)

    text = font_score.render('SCORE: ' + str(int(scores)), 1, 'gray40')
    window.blit(text, (WIDTH-150, 10))

    record = font_score.render('BEST SCORE: ' + str(int(best_score)), 1, 'gray40')
    window.blit(record, (50, 10))

    if speed == 0 and timer == 0:
        rect = img_g_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(img_g_over, rect)

    ####

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()