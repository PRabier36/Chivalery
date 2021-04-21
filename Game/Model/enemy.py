from Game.Model.Unit import Unit


class Enemy(Unit):

    def __init__(self, name, strength, agility, constitution, mana, mastery, luck, xpDrop, goldDrop, pos="front", state="alive", hp=0, race=None):
        self.__name = name
        self.__strength = strength
        self.__agility = agility
        self.__constitution = constitution
        self.__mana = mana
        self.__mastery = mastery
        self.__luck = luck
        self.__xpDrop = xpDrop
        self.__goldDrop = goldDrop
        self.__pos = pos
        self.__state = state
        self.__hp = hp
        self.__race = race



    # Getter

    def get_race(self):
        return self.__race

    def get_luck(self):
        return self.__luck

    def get_xpDrop(self):
        return self.__xpDrop

    def get_goldDrop(self):
        return self.__goldDrop


    # Setter
    def set_race(self, race):
        self.__race = race


    def set_luck(self, luck):
        self.__luck = luck


    def set_xpDrop(self, xpDrop):
        self.__xpDrop = xpDrop


    def set_goldDrop(self, goldDrop):
        self.__goldDrop = goldDrop


    # Unit
    # Getter
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

    def print(self):
        print("id : "+str(self.__id) +
              "name : "+str(self.__name) +
              "strength : "+str(self.__strength) +
              "agility : "+str(self.__agility) +
              "constitution : "+str(self.__constitution) +
              "mana : "+str(self.__mana) +
              "mastery : "+str(self.__mastery) +
              "luck : "+str(self.__luck) +
              "xp drop : "+str(self.__xpDrop) +
              "gold drop : "+str(self.__goldDrop))
        # print("race : "+str(self.__race))
        # print("state : "+str(self.__state))
        # print("pos : "+str(self.__pos))
        # print("hp : "+str(self.__hp))

