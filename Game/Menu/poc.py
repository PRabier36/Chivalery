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




[
def __init__(self, player, application, *groupes):
        font = pygame.font.SysFont('Harrington', 24, bold=True)
        x = LARGEUR_FENETRE - (LARGEUR_FENETRE / 8)
        y = HAUTEUR_FENETRE / 3
        clock = pygame.time.Clock()
        input_box1 = InputBox(100, 100, x, y)
        input_box2 = InputBox(100, 300, x, y)
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
]