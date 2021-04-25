import json

import requests
import simplejson as simplejson

from Game.API.api import Api
from Game.Model.Knight import Knight
from Game.Model.KnightClasse import KnightClasse

api = Api()
api_url = "http://localhost:3001"


class Player:

    def __init__(self, id, name, rank=1, level=1, money=45, xp=0, teachingBonus=0, kninghtList=[]):
        self.__id = id
        self.__name = name
        self.__rank = rank
        self.__level = level
        self.__money = money
        self.__xp = xp
        self.__teachingBonus = teachingBonus
        self.__Knight_list = kninghtList
        if id is None:
            self.createPlayer()

    # getter
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_rank(self):
        return self.__rank

    def get_level(self):
        return self.__level

    def get_money(self):
        return self.__money

    def get_xp(self):
        return self.__xp

    def get_teachingBonus(self):
        return self.__teachingBonus

    def get_knightList(self):
        return self.__Knight_list

    # setter

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_rank(self, rank):
        self.__rank = rank

    def set_level(self, level):
        self.__level = level

    def set_money(self, money):
        self.__money = money

    def set_xp(self, xp):
        self.__xp = xp

    def set_teachingBonus(self, teachingBonus):
        self.__teachingBonus = teachingBonus

    def set_knightList(self, knigthList):
        self.__Knight_list = knigthList

    def add_money(self, money):
        self.__money += money;

    def add_xp(self, xp):
        self.__xp += xp;

    def print(self):
        print("    " + self.__name)
        print("    rank : " + str(self.__rank))
        print("    level : " + str(self.__level))
        print("    money : " + str(self.__money) + " Gold")
        print("    xp : " + str(self.__xp))
        print("    Nb Knights : " + str(len(self.__Knight_list)))

    def print_knights(self):
        print("Knights :\n")
        i = 1
        if len(self.__Knight_list) == 0:
            print("No knight")
        else:
            for knight in self.__Knight_list:
                print(str(i) + ":\n")
                knight.print()
                i += 1

    def add_knight(self, knight):
        self.__Knight_list.append(knight)

    def create_new_knight(self):
        k = Knight()
        address = "/players/" + self.__id + "/knights/" + k.get_id()
        api.request(address, "PUT")
        self.__Knight_list.append(k)
        return k

    def revive(self):
        self.print()
        for knight in self.__Knight_list:
            print(knight.get_state())
            state = knight.get_state()
            if state != "alive":
                knight.set_state(str("alive"))

    def add_from_list(self, list):
        k_list = []
        for knight in list:
            if len(knight) > 1:
                k = Knight()
                k.set_id = knight["_id"]
                k.set_level = knight["level"]
                k.set_exp = knight["exp"]
                k.set_classe(KnightClasse(knight["Knight_class"]["_id"], knight["Knight_class"]["label"],
                                          knight["Knight_class"]["speciality"],
                                          knight["Knight_class"]["modifierAttack"],
                                          knight["Knight_class"]["modifierDefense"],
                                          knight["Knight_class"]["modifierSpeciality"]))
                k.set_strength = knight["strength"]
                k.set_agility = knight["agility"]
                k.set_constitution = knight["constitution"]
                k.set_mana = knight["mana"]
                k.set_mastery = knight["mastery"]
                k.set_state = knight["state"]
                k.set_pos = knight["pos"]
                k_list.append(k)
        self.__Knight_list = k_list

    def createPlayer(self):
        payload = {"name": self.__name, "level": self.__level, "rank": self.__rank, "money": self.__money,
                   "xp": self.__xp, "teachingBonus": self.__teachingBonus}
        headers = {'Content-Type': 'application/json'}
        response = api.request("/players", "POST", headers, payload)
        p = response.json()
        self.__id = p["_id"]

    def save(self):
        payload = {
            "name": self.__name,
            "level": self.__level,
            "rank": self.__rank,
            "money": self.__money,
            "xp": self.__xp,
            "teachingBonus": self.__teachingBonus,
        }
        klist = []
        for knight in self.__Knight_list:
            k = {
                "name": knight.get_name(),
                "level": "" + str(knight.get_level()),
                "exp": "" + str(knight.get_exp()),
                "affinityOff": "" + str(knight.get_affinityOff()),
                "affinityDef": "" + str(knight.get_affinityDef()),
                "affinitySupp": "" + str(knight.get_affinitySupp()),
                "strength": "" + str(knight.get_strength()),
                "agility": "" + str(knight.get_agility()),
                "constitution": "" + str(knight.get_constitution()),
                "mana": "" + str(knight.get_mana()),
                "mastery": "" + str(knight.get_mastery()),
                "state": "" + str(knight.get_state()),
                "pos": "" + str(knight.get_pos()),
                "Knight_class": {
                    "label": "Ecuyer",
                    "speciality": 1,
                    "modifierAttack": 1,
                    "modifierDefense": 1,
                    "modifierSpeciality": "1",
                    "_id": "608592331e79e04388b0de2f"
                }
            }
            klist.append(k)

        payload["Knight_list"] = klist

        headers = {'Content-Type': 'application/json'}
        response = api.request("/players/"+self.__id, "PUT", headers, payload)
