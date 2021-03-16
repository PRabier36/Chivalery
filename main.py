#main du projet Chivalery
import pygame
from pygame.locals import *
from Game.Config.config import *
from Game.Menu.menu import Menu

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
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        self._initialiser()
        self.ecran = Menu(self,self.groupeGlobal)

    def quitter(self):
        self.statut = False

    def partie(self):
        self._initialiser()
        self.ecran = Partie(self, self.fenetre, self.groupeGlobal)


    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
            elif event.type = KEYDOWN:
                if event.key == K_ESCAPE:
                    self.menu()

        self.fenetre.blit(self.background_image,(0,0))
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()
app = Application()
app.menu()
clock = pygame.time.Clock()
direction = None


    while app.statut:
        app.update()
        clock.tick(120)
        fps = clock.get_fps()
        print(fps)
    pygame.quit()