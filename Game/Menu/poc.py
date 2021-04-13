# main du projet Chivalery
import pygame
import pygame_menu
from pygame_menu import Menu
from Game.Config.config import *

pygame.init()

background = pygame.image.load('./Game/Template/chivalry.jpg')

class Main:
    # def set_difficulty(value, difficulty):
    #     # Do the job here !
    #     pass
    def Playing_path():
        # Do the job here !
        pass

    def Setting_path():
        # Do the job here !
        pass

    def Credits_path():
        # PathGetter(path='Game.Menu.credits',mode=1,caption='Path Getter')
        pass

    screen.blit(background, (0, 0))
    menu = Menu( HAUTEUR_FENETRE, LARGEUR_FENETRE, '', theme=lowopacity)

    menu.add.button('Play', Playing_path)
    menu.add.button('Setting', Setting_path)
    menu.add.button('credits', Credits_path)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)

    from itertools import cycle
    couleurs = [(0, 48, i) for i in range(0, 256, 15)]
    couleurs.extend(sorted(couleurs[1:-1], reverse=True))
    self._couleurTexte = cycle(couleurs)


parametre = (
    ("id", player.get_id()),
    ("name", player.get_name()),
    ("Rank", player.get_rank()),
    ("level", player.get_level()),
    ("money", player.get_money()),
    ("xp", player.get_xp()),
    ("teachingBonus", player.get_teachingBonus()),
    ("kninghtList", player.get_knightList())
)
self._Myinput = []

for label, cmd in parametre:
    Fi = FormInput(
        x,
        y,
        200,
        50,
        font,
        label,
        cmd
    )
    self._Myinput.append(Fi)
    for groupe in groupes:
        groupe.add(Fi)