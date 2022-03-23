import pygame.sprite


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group, isDan = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.dange = isDan
        self.add(group)

    def getDange(self):
        return self.dange

    def update(self, *args):
        if self.rect.y > args[0]:
            self.kill()
        else:
            self.rect.y += self.speed
