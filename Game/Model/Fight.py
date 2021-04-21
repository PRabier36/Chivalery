import time
import threading
import random
from typing import List, Any, Tuple

from Game.Model.Knight import Knight
from Game.Model.Map import Map
from Game.Model.enemy import Enemy
from Game.Model.Unit import Unit


class Fight:

    def __init__(self, id=None, gold=None, xp=None, enemies=None, player=None):
        self.__id = id
        self.__gold = gold
        self.__xp = xp
        self.__enemies = enemies
        self.__enemies_dead = []
        self.__player = player
        self.__state = "ongoing"
        self.__attackSpeed = []
        self.__map = Map()

    def testInitiative(self):
        for knight in self.__player.get_knightList():
            knightInit = (15 - (knight.get_agility() / 2)) / 3
            mylist = [knight, knightInit]
            self.__attackSpeed.append(mylist)
        for aS in self.__attackSpeed:
            print(aS[0].get_name())
            print(aS[1])

    def test_hp(self, unit):
        unit.set_hp(int(unit.get_constitution() * 10))

    def attack(self, offensive_unit, target_zone, damage):
        if target_zone == "back":
            list_target = self.__map.get_back()
        elif target_zone == "front":
            list_target = self.__map.get_front()
        elif target_zone == "e_front":
            list_target = self.__map.get_e_front()
        elif target_zone == "e_back":
            list_target = self.__map.get_e_back()
        else:
            return "error"
        if len(list_target) == 0:
            return "error"
        r = random.randint(0, (len(list_target) - 1))
        target = list_target[r]
        target.set_hp(target.get_hp() - damage)
        print(offensive_unit.get_name() + " attack and do " + str(damage) + " damage to " + target.get_name() + "(" + str(target.get_hp()) + ")")
        if target.get_hp() <= 0:
            target.set_state("ko")
            print(target.get_name() + " is " + target.get_state())
            self.__map.remove_unit_from_pos(target, target_zone)
            target.set_pos("out")

    def turn_knight(self, Knight):
        self.test_hp(Knight)
        print(Knight.get_name() + " hp " + str(Knight.get_hp()))

        if Knight.get_pos() == "unknow":
            Knight.set_pos("front")

        knight_attack_speed = (15 - (Knight.get_agility() / 2)) / 3

        front_attack = int((Knight.get_strength() + Knight.get_constitution())/2)
        back_attack = int((Knight.get_strength() + Knight.get_agility())/2)

        time.sleep(3)

        while self.__state == "ongoing" and Knight.get_state() == "alive":
            if Knight.get_pos() == "front":
                self.attack(Knight, "e_front", front_attack)
            if Knight.get_pos() == "back":
                self.attack(Knight, "e_front", back_attack)
            time.sleep(knight_attack_speed)


    def turn_enemy(self, Enemy):
        self.test_hp(Enemy)
        print(Enemy.get_name() + " hp " + str(Enemy.get_hp()))

        if Enemy.get_pos() == "unknow":
            Enemy.set_pos("e_front")

        Enemy_attack_speed = (15 - (Enemy.get_agility() / 2)) / 3

        front_attack = int((Enemy.get_strength() + Enemy.get_constitution())/2)
        back_attack = int((Enemy.get_strength() + Enemy.get_agility())/2)

        time.sleep(3)

        while self.__state == "ongoing" and Enemy.get_state() == "alive":
            if Enemy.get_pos() == "front":
                self.attack(Enemy, "front", front_attack)
            if Enemy.get_pos() == "back":
                self.attack(Enemy, "front", back_attack)
            time.sleep(Enemy_attack_speed)
        self.__gold += Enemy.get_goldDrop()
        self.__xp += Enemy.get_xpDrop()

    def timer(self, Timer):
        for i in range(-3, Timer, 1):
            print(i)
            self.verif_map_pos()
            if self.__state != "ongoing":
                break
            time.sleep(1)
        if self.__state == "ongoing":
            self.__state = "draw"

    def verif_map_pos(self):
        del self.__map
        self.__map = Map()
        for knight in self.__player.get_knightList():
            if knight.get_pos() == "back":
                self.__map.add_back(knight)
            if knight.get_pos() == "front":
                self.__map.add_front(knight)
        for enemy in self.__enemies:
            if enemy.get_pos() == "back":
                self.__map.add_e_back(enemy)
            if enemy.get_pos() == "front":
                self.__map.add_e_front(enemy)
        self.__map.print()

    def verifStateKnights(self):
        while self.__state == "ongoing":
            k_alive = False
            for knight in self.__player.get_knightList():
                if knight.get_state() == "alive":
                    k_alive = True
                    break
                if self.__state:
                    break
            if not k_alive:
                self.__state = "defeat"

    def verifStateEnemies(self):
        while self.__state == "ongoing":
            e_alive = False
            for enemy in self.__enemies:
                if enemy.get_state() == "alive":
                    e_alive = True
                    break
                if self.__state:
                    break
            if e_alive == False:
                self.__state = "victory"
        return

    def Start(self):
        t_init = threading.Thread(target=self.testInitiative)
        t_init.start()
        t_init.join()
        t0 = threading.Thread(target=self.timer, args=(60,))
        t0.start()

        t1 = threading.Thread(target=self.verifStateKnights)
        t2 = threading.Thread(target=self.verifStateEnemies)
        # t3 = threading.Thread(target=self.verif_map_pos)
        # t0, t1, t2, t3.start()
        t0, t1, t2.start()

        thread_list = []

        for knight in self.__player.get_knightList():
            t = threading.Thread(target=self.turn_knight, args=(knight,))
            thread_list.append(t)
        for enemy in self.__enemies:
            t = threading.Thread(target=self.turn_enemy, args=(enemy,))
            thread_list.append(t)
        for t in thread_list:
            t.start()
        # t0, t1, t2, t3.join()
        t0, t1, t2.join()
        for t in thread_list:
            t.join()
        print(self.__state)
        print("fin du combat")
        if self.__state == "victory":
            self.victory()
        elif self.__state == "draw":
            self.draw()
        else:
            self.defeat()
        return

    def victory(self):
        self.__player.add_money(self.__gold)
        self.__player.add_xp(self.__xp/2)
        for knight in self.__player.get_knightList():
            knight.addExp(self.__xp)
        print("Gains :\n"
              "     Player:\n"
              "         " + str(self.__gold) + "\n"
              "         " + str(self.__xp/2) + "\n"
              "     Player:\n"
              "         " + str(self.__xp) + "\n"
              "")

    def draw(self):
        self.__player.add_money(self.__gold/2)
        self.__player.add_xp(self.__xp/4)
        for knight in self.__player.get_knightList():
            knight.addExp(self.__xp/2)
        print("Gains :\n"
              "     Player:\n"
              "         " + (self.__gold/2) + "\n"
              "         " + str(self.__xp/4) + "\n"
              "     Player:\n"
              "         " + str(self.__xp/2) + "\n"
              "")

    def defeat(self):
        return