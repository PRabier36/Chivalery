import pygame
from ..Config.config import *
from .Jeu import *
from .Menu import *

class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WinTitle)
        font = pygame.font.SysFont('Harrington', 24, bold=True, italic=False)
        self.fond = background

        self.fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def GoToPlayerCreationMenu(self):
        # création du joueur
        self._initialiser()
        self.ecran = PlayerMenu(Player(10, "jean-claude", 0, 0, 10, 0, 0, 0), self, self.groupeGlobal)


    def ContinueTheLast(self):
        pass

    def loadParts(self):
        pass

    def GetBack(self):
        pass

    def _initialiser(self):
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def parametre(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def credits(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)



    def quitter(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return

        self.fenetre.blit(self.fond, (0, 0))
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()
