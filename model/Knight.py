class Knight:

    def __init__(self, id, name, level, classe, affinityOff, affinityDef, affinitySupp, strength, agility, constitution,
                 mana, mastery, luck):
        self.__id = id
        self.__name = name
        self.__level = level
        self.__classe = classe
        self.__affinityOff = affinityOff
        self.__affinityDef = affinityDef
        self.__affinitySupp = affinitySupp
        self.__strength = strength
        self.__agility = agility
        self.__constitution = constitution
        self.__mana = mana
        self.__mastery = mastery
        self.__luck = luck

    # Getter
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

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
