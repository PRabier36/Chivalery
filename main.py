# main du projet Chivalery

# import pygame
# from Game.Menu.Application import *
#
# pygame.init()
#
#
# app = Application()
# app.menu()
#
# clock = pygame.time.Clock()
#
# while app.statut:
#     app.update()
#     clock.tick(30)
#
# pygame.quit()

from Game.Model.Knight import Knight
from Game.Model.KnightClasse import KnightClasse

KnightClasse_id = 1
KnightClasse_label = "ecu"
KnightClasse_speciality = ""
KnightClasse_modifierAttack = 0
KnightClasse_modifierDefense = 0
KnightClasse_modifierSpeciality = 0
KnightClasse_listSkill = []

k1 = Knight(0, "arthur", "0")

k1.print()