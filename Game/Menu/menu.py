import pygame
from Game.Config.config import *

class Menu:
    """gestion du menu"""

    def __init__(self,application, *groupes):
        self.color = dict(
            normal=(0,200,0),
            hover=(0,200,200),
        )
        font = pygame.font.SysFont('Viner Hand Itc',24)
        items = (
            ()
        )