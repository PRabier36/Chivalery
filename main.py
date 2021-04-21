# main du projet Chivalery
import pygame
# from Game.Menu.Application import *
from Game.Model.Player import Player
from Game.Model.Fight import Fight
from Game.Model.enemy import Enemy
from Game.Model.Knight import Knight
import requests

response = requests.get("http://names.drycodes.com/1?nameOptions=boy_names")


# Ks = [Knight() for i in range(1)]
Ks = [Knight() for i in range(5)]
# for k in Ks:
#     kninghtList.append(k)
id = 1
name = (response.text[2:-2]).replace('_', ' ')
rank = 3
level = 2
money = 120
xp = 300
teachingBonus = 32

p = Player(id, name, rank, level, money, xp, teachingBonus, Ks)

id = 1
gold = 123
e1 = Enemy(1, "g1", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
e2 = Enemy(2, "g2", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
e3 = Enemy(3, "g3", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
Es = [e1, e2, e3]
f = Fight(id, gold, xp, Es, p)
print("start")
f.Start()
p.print()

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
