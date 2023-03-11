from DATA.variables import *
import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
