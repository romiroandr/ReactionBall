import random
import pygame

from ball import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)


fps = 60
clock = pygame.time.Clock()
sc = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

pygame.display.set_caption("game")
pygame.display.set_icon(pygame.image.load('iconka.jpg'))

bg_surf = pygame.image.load("fon.jpg").convert()

balls_names = ["dangerous.jpg", "green ball.png", "purple ball.jpg", "white_ball.png", "yellow ball.png"]
balls_surf = []
for i in balls_names:
    img = pygame.image.load(i).convert_alpha()
    if i != "white_ball.png":
        img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img,(100,100))
    balls_surf.append(img)

balls = pygame.sprite.Group()

def create_ball(group):
    x = random.randint(20, pygame.display.get_window_size()[0]-20)
    speed=random.randint(1,5)
    img = random.choice(balls_surf)
    img.set_colorkey((255,255,255))

    return Ball(x, speed, img, group)

create_ball(balls)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            create_ball(balls)



    sc.blit(bg_surf, (0, 0))

    balls.draw(sc)
    pygame.display.update()
    clock.tick(fps)

    balls.update(pygame.display.get_window_size()[1])