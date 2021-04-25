import os
import time
import threading
import random
from typing import List, Any, Tuple

from Game.Model.Knight import Knight
from Game.Model.Map import Map
from Game.Model.enemy import Enemy
from Game.Model.Unit import Unit


class Fight:

    def __init__(self, name, gold=None, xp=None, time=15, enemies=None, player=None):
        self.__name = name
        self.__gold = gold
        self.__xp = xp
        self.__time = time
        self.__enemies = enemies
        self.__player = player
        self.__enemies_dead = []
        self.__state = "ongoing"
        self.__attackSpeed = []
        self.__map = Map()
        self.__logs = ""


    def print(self):
        r = str(self.__name)+"\n"+ \
            "       Time : "+str(self.__time)+" \n" \
            "       Loot: "+str(self.__gold)+" gold, "+str(self.__xp)+" xp\n" \
            "       Enemy(ies) : "
        len_enemies = len(self.__enemies)
        i = 0
        for e in self.__enemies:
            r += e.get_name()
            if i < len_enemies:
                r += ", "
        return r

    def testInitiative(self):
        for knight in self.__player.get_knightList():
            knightInit = (15 - (knight.get_agility() / 2)) / 3
            mylist = [knight, knightInit]
            self.__attackSpeed.append(mylist)
        for aS in self.__attackSpeed:
            self.__logs += str(aS[0].get_name())+"\n"
            self.__logs += str(aS[1])+"\n"

    def test_hp(self):
        for knight in self.__player.get_knightList():
            knight.set_hp(int(knight.get_constitution() * 10))
        for enemy in self.__enemies:
            enemy.set_hp(int(enemy.get_constitution() * 10))

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
        self.__logs += (offensive_unit.get_name() + " attack and do " + str(damage) + " damage to " + target.get_name() + "(" + str(target.get_hp()) + ")")+"\n"
        if target.get_hp() <= 0:
            target.set_state("ko")
            self.__logs += (target.get_name() + " is " + target.get_state())+"\n"
            self.__map.remove_unit_from_pos(target, target_zone)
            target.set_pos("out")

    def turn_knight(self, Knight):
        self.__logs += (Knight.get_name() + " hp " + str(Knight.get_hp()))+"\n"

        if Knight.get_pos() == "unknow":
            Knight.set_pos("front")

        knight_attack_speed = (15 - (Knight.get_agility() / 2)) / 3

        front_attack = int(((Knight.get_strength() + Knight.get_constitution())/2) +
                           Knight.get_classe().get_modifierAttack())
        back_attack = int(((Knight.get_strength() + Knight.get_agility())/2) +
                          Knight.get_classe().get_modifierAttack())

        time.sleep(3)

        while self.__state == "ongoing" and Knight.get_state() == "alive":
            if Knight.get_pos() == "front":
                self.attack(Knight, "e_front", front_attack)
            if Knight.get_pos() == "back":
                self.attack(Knight, "e_front", back_attack)
            time.sleep(knight_attack_speed)


    def turn_enemy(self, Enemy):
        self.__logs += (Enemy.get_name() + " hp " + str(Enemy.get_hp()))+"\n"

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

    def timer(self):
        for i in range(-3, self.__time, 1):
            os.system('cls')
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
        print(self.__logs)

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
        self.testInitiative()
        self.test_hp()
        t0 = threading.Thread(target=self.timer)
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
        time.sleep(3)
        os.system('cls')
        if self.__state == "victory":
            self.victory()
        elif self.__state == "draw":
            self.draw()
        else:
            self.defeat()
        self.__player.revive()
        return

    def loot(self, gp, xp):
        self.__player.add_money(gp)
        self.__player.add_xp(xp/2)
        for knight in self.__player.get_knightList():
            knight.addExp(xp)
        print("Gains :\n"
              "     Player:\n"
              "         " + str(gp) + "\n"
              "         " + str(xp/2) + "\n"
              "     Knight:\n"
              "         " + str(xp) + "\n"
              "")

        input("Enter for continue...")


    def victory(self):
        gp = int(self.__gold)
        xp = int(self.__xp)
        self.loot(gp, xp)

    def draw(self):
        gp = int(self.__gold)
        xp = int(self.__xp)
        self.loot(gp/2, xp/2)

    def defeat(self):
        self.loot(0, 0)
