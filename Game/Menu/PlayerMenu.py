import sys

import pygame
import pygame_menu
from pygame_menu import Menu
from ..Config.config import *
from ..Model.Player import *

user_text = ''

class PlayerMenu:

    def __init__(self, *groupes):
        self._fenetre = screen
        self.fond = background
        font = pygame.font.SysFont('Harrington', 24, bold=True, italic=False)

        self.couleurs = dict(
            normal=(202, 111, 30),
            survol=(235, 152, 78),
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            text_surface = font.render(user_text, True, (255, 255, 255))
            screen.blit(text_surface, (0,0))




    def update(self, events):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return

    def startGame(self):
        pass

    def cancelAndBack(self):
        pass

    def createPlayer(self):
        pass
