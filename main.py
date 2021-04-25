# main du projet Chivalery
import json
import redis
cache = redis.Redis(host='localhost', port=6379)

import pygame
# from Game.Menu.Application import *
from Game.Model.GUI import start_game
from Game.Model.Player import Player
from Game.Model.Fight import Fight
from Game.Model.enemy import Enemy
from Game.Model.Knight import Knight


# start_game()


# name = input("Your name ?: ")
# name = "King Arthur"
#
# p = Player(None, name)

# k = Knight()

# k_class = k.get_classe()
#
# json.dumps(k_class)
#
# k.set_classe("")
#
# print(k)

# print(json.dumps(k.__dict__))



# kninghtList = []
# Ks = [Knight() for i in range(1)]
# Ks = [Knight() for i in range(5)]
# for k in Ks:
#     cache.set(str("unit-" + k.get_id() + "-hp"), int(k.get_constitution() * 10))
#     # kninghtList.append(k)
#
# for k in Ks:
#     print(cache.get(str("unit-" + k.get_id() + "-hp")).decode('utf-8'))
#
# print("decr")
#
# for k in Ks:
#     cache.decr(str("unit-" + k.get_id() + "-hp"), 15)
#
# for k in Ks:
#     print(cache.get(str("unit-" + k.get_id() + "-hp")).decode('utf-8'))

# id = 1
# name = "daniel"
# rank = 3
# level = 2
# money = 120
# xp = 300
# teachingBonus = 32
#
# p = Player(id, name, rank, level, money, xp, teachingBonus, Ks)
#
# cache.set("knight-" + knight.get_id() + "")

# id = 1
# gold = 123
# e1 = Enemy(1, "Goblin1", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
# e2 = Enemy(2, "Goblin2", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
# e3 = Enemy(3, "Goblin3", None, 10, 15, 9, 3, 12, 10, 15, 50, "front")
# Es = [e1, e2, e3]
# f = Fight(id, gold, xp, Es, p)
# print("start")
# f.Start()
# p.print()





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
