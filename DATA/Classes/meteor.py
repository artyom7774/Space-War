from DATA.variables import *
import pygame
import random


class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, group):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.add(group)

        self.speed = random.randint(2, 3)
        
        self.health = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > HEIGHT:
            self.kill()
