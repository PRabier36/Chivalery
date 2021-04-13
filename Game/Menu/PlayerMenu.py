import sys
import tkinter
import pygame
import pygame_menu
from pygame_menu import Menu
from ..Components.InputBox import *
from ..Config.config import *
from ..Model.Player import *


class PlayerMenu:

    def __init__(self, player, application, *groupes):
        font = pygame.font.SysFont('Harrington', 24, bold=True)
        x = LARGEUR_FENETRE - (LARGEUR_FENETRE / 8)
        y = HAUTEUR_FENETRE / 3
        self._myscreen = screen
        clock = pygame.time.Clock()
        input_box1 = InputBox(self._myscreen, 100, 100, 140, 32)
        input_box2 = InputBox(self._myscreen, 100, 300, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)

            pg.display.flip()
            clock.tick(30)






    def update(self, events):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    PlayerMenu.user_text = PlayerMenu.user_text[0:-1]
                PlayerMenu.user_text += event.unicode

    def startGame(self):
        pass

    def cancelAndBack(self):
        pass

    def createPlayer(self):
        pass


class FormInput:

    def __init__(self, x, y, Fwidth, Fheight, font, label, cmd):
        super().__init__()

        self.myscren = screen

        self.rect = self.myscren.get_rect()
        self.rect.center = (x, y)

        self.text = font.render(label, True, (0, 0, 0))
        self.rectText = self.text.get_rect()
        self.rectText.center = (100, 25)

    def dessiner(self, couleur):
        self.myscren.fill(couleur)
        self.myscren.blit(self.texte, self.rectTexte)

