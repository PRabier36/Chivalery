class KnightClasse:
    def __init__(self, id=None, label=None, speciality=None, modifierAttack=None, modifierDefense=None, modifierSpeciality=None, listSkill=None):
        self.__id = id
        self.__label = label
        self.__speciality = speciality
        self.__modifierAttack = modifierAttack
        self.__modifierDefense = modifierDefense
        self.__modifierSpeciality = modifierSpeciality
        self.__listSkill = listSkill

    # Getter
    def get_id(self):
        return self.__id

    def get_label(self):
        return self.__label

    def get_speciality(self):
        return self.__speciality

    def get_modifierAttack(self):
        return self.__modifierAttack

    def get_modifierDefense(self):
        return self.__modifierDefense

    def get_modifierSpeciality(self):
        return self.__modifierSpeciality

    def get_listSkill(self):
        return self.__listSkill

    # Setter
    def set_id(self, id):
        self.__id = id

    def set_label(self, label):
        self.__label = label

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def set_modifierAttack(self, modifierAttack):
        self.__modifierAttack = modifierAttack

    def set_modifierDefense(self, modifierDefense):
        self.__modifierDefense = modifierDefense

    def set_modifierSpeciality(self, modifierSpeciality):
        self.__modifierSpeciality = modifierSpeciality

    def set_listSkill(self, listSkill):
        self.__listSkill = listSkill

    # Functions
    def print(self):
        print(
            "id :", self.__id, "\n",
            "label :", self.__label, "\n",
            "speciality :", self.__speciality, "\n",
            "modifierAttack :", self.__modifierAttack, "\n",
            "modifierDefense :", self.__modifierDefense, "\n",
            "modifierSpeciality :", self.__modifierSpeciality, "\n")

    def newKnight(self):
        self.__id = 1
        self.__label = "Ecuyer"
        self.__speciality = 1
        self.__modifierAttack = 1
        self.__modifierDefense = 1
        self.__modifierSpeciality = 1
        self.__listSkill = []
