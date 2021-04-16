# main du projet Chivalery
import pygame
# from Game.Menu.Application import *
from Game.Model.Player import Player
from Game.Model.Fight import Fight
from Game.Model.Enemy import Enemy
from Game.Model.Knight import Knight
import requests

response = requests.get("http://names.drycodes.com/1?nameOptions=boy_names")


kninghtList = []
Ks = [Knight() for i in range(5)]
for k in Ks:
    kninghtList.append(k)
id = 1
name = (response.text[2:-2]).replace('_', ' ')
rank = 3
level = 2
money = 120
xp = 300
teachingBonus = 32

p = Player(id, name, rank, level, money, xp, teachingBonus, kninghtList)

id = 1
gold = 123
f = Fight(id, gold, xp, None, p)
print("start")
f.Start()


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
