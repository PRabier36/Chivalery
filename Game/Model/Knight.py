from Game.Model.KnightClasse import KnightClasse
from Game.Model.Unit import Unit
from Game.Model.Level import Level
import random
import requests
import time

api_url = "http://localhost:3000"

allLvl = Level()


class Knight(Unit):

    # self.__id = id  # int
    # self.__name = name  # string
    # self.__level = level  # int
    # self.__Knight_class = classe  # class KnightClasse
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
            response = requests.get("http://names.drycodes.com/1?nameOptions=boy_names&separator=space")
            self.__name = (response.text[2:-2])
            self.create()

    # Getter
    def get_level(self):
        return self.__level

    def get_classe(self):
        return self.__Knight_class

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
        self.__Knight_class = classe

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

    def get_state(self):
        return self.__state

    def get_hp(self):
        return self.__hp

    def get_pos(self):
        return self.__pos

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

    def set_state(self, state):
        self.__state = state

    def set_hp(self, hp):
        self.__hp = hp

    def set_pos(self, pos):
        self.__pos = pos

    # Functions

    def print(self):
        print(
            # "id :", self.__id, "\n",
            "name :", self.__name, "\n",
            "level :", self.__level, "\n",
            "exp :", self.__exp, "\n",
            "classe :\n"
            "   label :", self.__Knight_class.get_label(), "\n",
            "   speciality :", self.__Knight_class.get_speciality(), "\n",
            "   modifierAttack :", self.__Knight_class.get_modifierAttack(), "\n",
            "   modifierDefense :", self.__Knight_class.get_modifierDefense(), "\n",
            "   modifierSpeciality :", self.__Knight_class.get_modifierSpeciality(), "\n",
            "Affinity : \n"
            "    Off :", self.__affinityOff, "\n",
            "    Def :", self.__affinityDef, "\n",
            "    Supp :", self.__affinitySupp, "\n"
                                               "Stats : ",
            "    Strength :", self.__strength, "\n",
            "    Agility :", self.__agility, "\n",
            "    Constitution :", self.__constitution, "\n",
            "    Mana :", self.__mana, "\n",
            "    Mastery :", self.__mastery, "\n")

    def getKnightById(self, id):
        response = requests.request("GET", api_url + "/knights/" + id)
        knight = response.json()

        self.__id = knight["_id"]
        self.__level = knight["level"]
        self.__exp = knight["exp"]
        self.__Knight_class = KnightClasse(knight["Knight_class"]["_id"], knight["Knight_class"]["label"],
                                     knight["Knight_class"]["speciality"], knight["Knight_class"]["modifierAttack"],
                                     knight["Knight_class"]["modifierDefense"],
                                     knight["Knight_class"]["modifierSpeciality"])
        self.__strength = knight["strength"]
        self.__agility = knight["agility"]
        self.__constitution = knight["constitution"]
        self.__mana = knight["mana"]
        self.__mastery = knight["mastery"]
        self.__state = knight["state"]
        self.__pos = knight["pos"]
        return self

    def attack(self, Fight):
        print(self.get_name() + " attack")
        while Fight.get_EnemiesIsDead() == False:
            knightAttackSpeed = (15 - (self.get_agility() / 2)) / 3
            time.sleep(knightAttackSpeed)
            print(self.get_name() + " attack")

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
        # self.__id = 1  # int
        self.__level = 1  # int
        self.__exp = 0
        Kclass = KnightClasse(0, 0, 0, 0, 0, 0, 0)
        Kclass.newKnight()
        self.__Knight_class = Kclass  # class KnightClasse

        self.generateAffinity()

        self.__strength = self.generateCapacityScore()
        self.__agility = self.generateCapacityScore()
        self.__constitution = self.generateCapacityScore()
        self.__mana = self.generateCapacityScore()
        self.__mastery = self.generateCapacityScore()
        self.__state = "alive"
        self.__pos = "unknow"

        payload = "{\r\n    \"name\": \"" + self.__name + "\",\r\n    \"level\": \"" + str(
            self.__level) + "\",\r\n    \"exp\": \"" + str(self.__exp) + "\",\r\n    \"affinityOff\": \"" + str(
            self.__affinityOff) + "\",\r\n    \"affinityDef\": \"" + str(
            self.__affinityDef) + "\",\r\n    \"affinitySupp\": \"" + str(
            self.__affinitySupp) + "\",\r\n    \"strength\": \"" + str(
            self.__strength) + "\",\r\n    \"agility\": \"" + str(
            self.__agility) + "\",\r\n    \"constitution\": \"" + str(
            self.__constitution) + "\",\r\n    \"mana\": \"" + str(self.__mana) + "\",\r\n    \"mastery\": \"" + str(
            self.__mastery) + "\",\r\n    \"state\": \"" + str(self.__state) + "\",\r\n    \"pos\": \"" + str(
            self.__pos) + "\"\r\n}"
        headers = {}
        requests.request("POST", api_url + "/knights", headers=headers, data=payload)
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
        while self.__exp >= allLvl.getExpLvlByLvl(self.__level):
            self.KnightLvlUp()
