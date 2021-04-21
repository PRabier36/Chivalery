from Game.Model.Knight import Knight


class Player:

    def __init__(self, id, name, rank=1, level=1, money=45, xp=0, teachingBonus=0, kninghtList=[]):
        self.__id = id
        self.__name = name
        self.__rank = rank
        self.__level = level
        self.__money = money
        self.__xp = xp
        self.__teachingBonus = teachingBonus
        self.__knigntList = kninghtList



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
        return self.__knigntList

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
        self.__knigntList = knigthList

    def add_money(self, money):
        self.__money += money;

    def add_xp(self, xp):
        self.__xp += xp;

    def print(self):
        print("    "+self.__name)
        print("    rank : " + str(self.__rank))
        print("    level : " + str(self.__level))
        print("    money : " + str(self.__money) + " Gold")
        print("    xp : " + str(self.__xp))
        print("    Nb Knights : " + str(len(self.__knigntList)))

    def print_knights(self):
        print("Knights :\n")
        i = 1
        if len(self.__knigntList) == 0:
            print("No knight")
        else:
            for knight in self.__knigntList:
                print(str(i)+":\n")
                knight.print()
                i += 1

    def add_knight(self, knight):
        self.__knigntList.append(knight)

    def create_new_knight(self):
        k = Knight()
        self.__knigntList.append(k)
        return k

    def revive(self):
        for knight in self.__knigntList:
            knight.set_state("alive")
