# main du projet Chivalery
import pygame
from Game.Menu.Application import *

pygame.init()


app = Application()
app.menu()

clock = pygame.time.Clock()

while app.statut:
    app.update()
    clock.tick(30)

pygame.quit()
