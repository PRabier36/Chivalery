#main du projet Chivalery
import pygame
from pygame.locals import *
from Game.Config.config import *

GAMEVERSION = "0.0.1-initial"
WINDOW_TITLE = "Chivalery: Knight's School"

class Application:

    global version

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.background_image = pygame.image.load(Background_Img)
        self.fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
        # mettre ici init du groupe d'affichage

        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()