from Game.Model.Unit import Unit


class Enemy(Unit):

    def __init__(self, id, name, race, strength, agility, constitution, mana, mastery, luck, xpDrop, goldDrop):
        self.__id = id
        self.__name = name
        self.__race = race
        self.__strength = strength
        self.__agility = agility
        self.__constitution = constitution
        self.__mana = mana
        self.__mastery = mastery
        self.__luck = luck
        self.__xpDrop = xpDrop
        self.__goldDrop = goldDrop
