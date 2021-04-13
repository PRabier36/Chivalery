import sys
import tkinter
import pygame
import pygame_menu
from pygame_menu import Menu
from ..Components.InputBox import *
from ..Config.config import *
from ..Model.Player import *
from ..Components.TextBox import *

KEY_REPEAT_SETTING = (200, 70)


class PlayerMenu:

    def __init__(self, application, *groupes):
        window = screen
        font = pygame.font.SysFont('Harrington', 24, bold=True, italic=False)
        text = ""

        text_surf = font.render(text, True, (0, 0, 0))
        window.blit(text_surf, text_surf.get_rect(center=window.get_rect().center))
        pygame.display.flip()

    def update(self, events):
        events = pygame.event.get()
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        input_active = True
        clock = pygame.time.Clock()
        for event in events:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitter()
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode


