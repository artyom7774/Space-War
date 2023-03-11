import pygame

FPS = 60
WIDTH = 900
HEIGHT = 600

WAYS = {
    "meteor": "DATA/Sprites/meteor.png",
    "bullet": "DATA/Sprites/bullet.png",
    "ship": "DATA/Sprites/ship.png"
}

speed = {
    "0": 30,
    "1": 20,
    "2": 15,
    "3": 12,
    "4": 10
}

meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group()
