import time
import threading

from Game.Model.Knight import Knight


class Fight:

    def __init__(self, id=None, gold=None, xp=None, enemies=None, player=None):
        self.__id = id
        self.__gold = gold
        self.__xp = xp
        self.__enemies = enemies
        self.__player = player
        self.__enemiesIsDead = False
        self.__attackSpeed = []

    def get_EnemiesIsDead(self):
        return self.__enemiesIsDead

    def testInitiative(self):
        for knight in self.__player.get_knightList():
            knightInit = (15 - (knight.get_agility() / 2)) / 3
            mylist = [knight, knightInit]
            self.__attackSpeed.append(mylist)
        for aS in self.__attackSpeed:
            print(aS[0].get_name())
            print(aS[1])

    def attack(self, Knight):
        print(Knight.get_name() + " attack")
        while self.get_EnemiesIsDead() == False:
            knightAttackSpeed = (15 - (Knight.get_agility() / 2)) / 3
            time.sleep(knightAttackSpeed)
            print(Knight.get_name()+" attack")

    def timer(self, Timer):
        for i in range(Timer):
            print(i)
            time.sleep(1)
        self.__enemiesIsDead = True

    def Start(self):
        tinit = threading.Thread(target=self.testInitiative)
        tinit.start()
        tinit.join()
        threadList = []
        # t0 = threading.Thread(target=self.timer, args=(15))
        # t0.start()
        for knight in self.__player.get_knightList():
            t = threading.Thread(target=self.attack, args=(knight))
            threadList.append(t)
        for t in threadList:
            t.start()
        for t in threadList:
            t.join()
        print("fin du combat")
        return
