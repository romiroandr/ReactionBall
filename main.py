import random
import pygame
import sys

from ball import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 500)

fps = 60
clock = pygame.time.Clock()
sc = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

pygame.display.set_caption("game")
pygame.display.set_icon(pygame.image.load('iconka.jpg'))
mp = pygame.mixer.Sound("ballllllklll.mp3")
gg = pygame.mixer.Sound("fon.mp3")
bg_surf = pygame.image.load("fon.jpg").convert()
shrift=pygame.font.SysFont('arial',20 )
text=shrift.render("""Добро пожаловать в игру, чтобы продолжить нажмити пробел""",1, (0,0,0))

pygame.mixer.music.load("lalalala.mp3")
pygame.mixer.music.play(-1)

balls_names = ["redball.png", "orangeball.png", "green ball.png", "white_ball.png", "blueball.png"]

bad_balls = []

balls = pygame.sprite.Group()
zastavka = pygame.image.load("ava.png").convert_alpha()
isza=True

def create_ball(group):
    x = random.randint(20, pygame.display.get_window_size()[0] - 20)
    speed = random.randint(1, 5)

    i = random.choice(balls_names)
    img = pygame.image.load(i).convert_alpha()
    if i != "white_ball.png":
        img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (100, 100))

    ball_cur = Ball(x, speed, img, group)
    return ball_cur





def burst_ball(press_coord, is_pressed):
    for i in balls:
        if i.rect.collidepoint(press_coord) and is_pressed:
            i.kill()
            if i.image in bad_balls:
                gg.play()
            else:
                mp.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT and not isza:
            create_ball(balls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                isza = False
                create_ball(balls)
    if isza:
        sc.blit(zastavka,(0,0))
        sc.blit(text,(10,290))
    else:
        sc.blit(bg_surf, (0, 0))

        balls.draw(sc)

        balls.update(pygame.display.get_window_size()[1])
        mouse_coord = pygame.mouse.get_pos()
        left_btn_pressed = pygame.mouse.get_pressed()[0]
        burst_ball(mouse_coord, left_btn_pressed)

    pygame.display.update()
    clock.tick(fps)
