class Level:
    def __init__(self):
        self.__expLvl = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]



    # Getter
    def get_expLvl(self):
        return self.__expLvl

    # Setter
    def set_level(self, expLvl):
        self.__expLvl = expLvl

    # Prototypes
    def getExpLvlByLvl(self, lvl):
        i = 0
        for exp in self.__expLvl:
            if i == lvl:
                return exp
            i += 1
