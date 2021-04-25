import pygame
import pygame_menu
from pygame_menu import Menu
from ..Config.config import *
from ..Components.MenuButton import *
from .PlayerMenu import *


class Jeu:
    """ Simulacre de l'interface du jeu """

    def __init__(self, application, *groupes):

        
        font = pygame.font.SysFont('Harrington', 24, bold=True, italic=False)

        self.couleurs = dict(
            normal=(202, 111, 30),
            survol=(235, 152, 78),
        )

        # noms des menus et commandes associées
        items = (
            ('Nouvelle', application.startGui()),
            ('continuer', application.ContinueTheLast),
            ('charger', application.loadParts)
        )
        x = LARGEUR_FENETRE - (LARGEUR_FENETRE/8)
        y = HAUTEUR_FENETRE / 3
        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes:
                groupe.add(mb)





    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur):
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche:
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else:
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else:
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)



    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer

