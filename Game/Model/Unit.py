class Unit:

    def __init__(self, id, name, level, classe, affinityOff, affinityDef, affinitySupp, strength, agility, constitution,
                 mana, mastery, luck, state="alive", hp=None, pos="unknow"):
        self.__id = id
        self.__name = name
        self.__strength = strength
        self.__agility = agility
        self.__constitution = constitution
        self.__mana = mana
        self.__mastery = mastery
        self.__luck = luck
        self.__state = state
        self.__hp = hp
        self.__pos = pos

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





