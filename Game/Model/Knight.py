from Game.Model.KnightClasse import KnightClasse
from Game.Model.Unit import Unit
from Game.Model.Level import Level
import random
import requests
import time


allLvl = Level()

class Knight(Unit):

    # self.__id = id  # int
    # self.__name = name  # string
    # self.__level = level  # int
    # self.__classe = classe  # class KnightClasse
    # self.__affinityOff = affinityOff  # int 3-24 total affinity 30
    # self.__affinityDef = affinityDef  # int 3-24 total
    # self.__affinitySupp = affinitySupp  # int 3-24 total
    # self.__strength = strength  # int
    # self.__agility = agility  # int
    # self.__constitution = constitution  # int
    # self.__mana = mana  # int
    # self.__mastery = mastery  # int
    # self.__luck = luck  # int

    def __init__(self, id=None):
        if id:
            self.getKnightById(id)
        else:
            response = requests.get("http://names.drycodes.com/1?nameOptions=boy_names")
            self.__name = response.text[2:-2]
            self.create()



    # Getter
    def get_level(self):
        return self.__level

    def get_classe(self):
        return self.__classe

    def get_affinityOff(self):
        return self.__affinityOff

    def get_affinityDef(self):
        return self.__affinityDef

    def get_affinitySupp(self):
        return self.__affinitySupp

    def get_exp(self):
        return self.__exp

    # Setter
    def set_level(self, level):
        self.__level = level

    def set_classe(self, classe):
        self.__classe = classe

    def set_affinityOff(self, affinityOff):
        self.__affinityOff = affinityOff

    def set_affinityDef(self, affinityDef):
        self.__affinityDef = affinityDef

    def set_affinitySupp(self, affinitySupp):
        self.__affinitySupp = affinitySupp

    def set_Exp(self, exp):
        self.__exp = exp

    # Unit
    # Getter
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_strength(self):
        return self.__strength

    def get_agility(self):
        return self.__agility

    def get_constitution(self):
        return self.__constitution

    def get_mana(self):
        return self.__mana

    def get_mastery(self):
        return self.__mastery

    def get_luck(self):
        return self.__luck

    # Setter
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_strength(self, strength):
        self.__strength = strength

    def set_agility(self, agility):
        self.__agility = agility

    def set_constitution(self, constitution):
        self.__constitution = constitution

    def set_mana(self, mana):
        self.__mana = mana

    def set_mastery(self, mastery):
        self.__mastery = mastery

    def set_luck(self, luck):
        self.__luck = luck




    # Functions

    def print(self):
        print(
            "id :", self.__id, "\n",
            "name :", self.__name, "\n",
            "level :", self.__level, "\n",
            "exp :", self.__exp, "\n",
            "classe :\n"
            "   id :", self.__classe.get_id(), "\n",
            "   label :", self.__classe.get_label(), "\n",
            "   speciality :", self.__classe.get_speciality(), "\n",
            "   modifierAttack :", self.__classe.get_modifierAttack(), "\n",
            "   modifierDefense :", self.__classe.get_modifierDefense(), "\n",
            "   modifierSpeciality :", self.__classe.get_modifierSpeciality(), "\n",
            "affinityOff :", self.__affinityOff, "\n",
            "affinityDef :", self.__affinityDef, "\n",
            "affinitySupp :", self.__affinitySupp, "\n",
            "strength :", self.__strength, "\n",
            "agility :", self.__agility, "\n",
            "constitution :", self.__constitution, "\n",
            "mana :", self.__mana, "\n",
            "mastery :", self.__mastery, "\n")

    def attack(self, Fight):
        print(self.get_name() + " attack")
        while Fight.get_EnemiesIsDead() == False:
            knightAttackSpeed = (15 - (self.get_agility() / 2)) / 3
            time.sleep(knightAttackSpeed)
            print(self.get_name()+" attack")

    def generateAffinity(self):
        i = 30
        temp = random.randint(3, 24)
        self.__affinityOff = temp  # int 3-24 total affinity 30
        i -= temp
        temp = random.randint(3, (i - 3))
        self.__affinityDef = temp  # int 3-24 total
        i -= temp
        self.__affinitySupp = i  # int 3-24 total

    def generateCapacityScore(self):
        d6list = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        find = 7
        min = 0
        i = 0
        for d in d6list:
            if d < find:
                min = i
                find = d
            i += 1
        d6list.pop(min)
        result = 0
        for d in d6list:
            result += d
        return result

    def create(self):
        self.__id = 1  # int
        self.__level = 1  # int
        self.__exp = 0
        Kclass = KnightClasse(0,0,0,0,0,0,0)
        Kclass.newKnight()
        self.__classe = Kclass  # class KnightClasse

        self.generateAffinity()

        self.__strength = self.generateCapacityScore()  # int
        self.__agility = self.generateCapacityScore()  # int
        self.__constitution = self.generateCapacityScore()  # int
        self.__mana = self.generateCapacityScore()  # int
        self.__mastery = self.generateCapacityScore()  # int
        return self

    def affinityOffHigh(self):
        return self.__affinityOff > self.__affinityDef and self.__affinityOff > self.__affinitySupp

    def affinityDefHigh(self):
        return self.__affinityDef > self.__affinityOff and self.__affinityDef > self.__affinitySupp

    def KnightLvlUp(self):
        self.__level += 1
        self.__constitution += 1
        if self.affinityOffHigh():
            self.__strength += 1
            self.__agility += 1
        elif self.affinityDefHigh():
            self.__agility += 1
            self.__constitution += 1
        else:
            self.__mastery += 1
            self.__mana += 1

    def addExp(self, exp):
        self.__exp += exp
        while  self.__exp >= allLvl.getExpLvlByLvl(self.__level):
            self.KnightLvlUp()
