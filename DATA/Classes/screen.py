from DATA.Classes.text import print_text
from DATA.variables import *
import pygame
import random


class Screen(object):
    def __init__(self):
        object.__init__(self)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__game_over = False
        self.score = 0

        pygame.display.set_caption("Spase wars")

    def draw(self, player):

        self.screen.fill(pygame.color.Color("blue"))

        meteors.update()
        meteors.draw(self.screen)

        bullets.update()
        bullets.draw(self.screen)

        player.update()
        self.screen.blit(player.image, (player.rect.x, player.rect.y))
        print_text(screen=self.screen, x=5, y=5, message=f"Score: {self.score}", font_size=32, font_color=(255, 255, 255))

        pygame.display.update()

    def logic(self, player):
        if pygame.sprite.groupcollide(meteors, bullets, True, True):
            self.score += 1

        if pygame.sprite.spritecollide(player, meteors, True):
            self.__game_over = True

    def get_game_over(self):
        return self.__game_over
