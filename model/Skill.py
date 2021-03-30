class Skill:
    def __init__(self, id, label, type, target, power):
        self.__id = id
        self.__label = label
        self.__type = type
        self.__target = target
        self.__power = power

    # Getter
    def get_id(self):
        return self.__id

    def get_label(self):
        return self.__label

    def get_type(self):
        return self.__type

    def get_target(self):
        return self.__target

    def get_power(self):
        return self.__power

    # Setter
    def get_id(self, id):
        self.__id = id

    def get_label(self, label):
        self.__label = label

    def get_type(self, type):
        self.__type = type

    def get_target(self, target):
        self.__target = target

    def get_power(self, power):
        self.__power = power

    # Functions
    def print(self):
        print(
            "id :", self.__id, "\n",
            "label :", self.__label, "\n",
            "type :", self.__type, "\n",
            "target :", self.__target, "\n",
            "power :", self.__power, "\n")
