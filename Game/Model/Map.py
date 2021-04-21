class Map:

    def __init__(self, back=[], front=[], e_front=[], e_back=[]):
        self.__map = ["back", "front", "e_front", "e_back"]
        self.__back = back
        self.__front = front
        self.__e_front = e_front
        self.__e_back = e_back

    def get_back(self):
        return self.__back

    def get_front(self):
        return self.__front

    def get_e_front(self):
        return self.__e_front

    def get_e_back(self):
        return self.__e_back

    def set_back(self, back):
        self.__back = back

    def set_front(self, front):
        self.__front = front

    def set_e_front(self, e_front):
        self.__e_front = e_front

    def set_e_back(self, e_back):
        self.__e_back = e_back

    # Prototypes
    def remove_unit_from_pos(self, unit, pos):
        if pos == "back":
            self.__back.remove(unit)
        if pos == "front":
            self.__front.remove(unit)
        if pos == "e_front":
            self.__e_front.remove(unit)
        if pos == "e_back":
            self.__e_back.remove(unit)

    def add_unit_in_pos(self, unit, pos):
        if pos == "back":
            self.__back.append(unit)
        if pos == "front":
            self.__front.append(unit)
        if pos == "e_front":
            self.__e_front.append(unit)
        if pos == "e_back":
            self.__e_back.append(unit)

    def add_back(self, unit):
        self.__back.append(unit)

    def add_front(self, unit):
        self.__front.append(unit)

    def add_e_front(self, unit):
        self.__e_front.append(unit)

    def add_e_back(self, unit):
        self.__e_back.append(unit)

    def print_unit_name(self, unit):
        r = ""
        temp = unit.get_name().split(" ")[0]
        lp = len(temp)
        if lp > 10:
            lp = 10
        r += (temp[0:lp])
        lp += len(str(unit.get_hp()))+3
        r += " (" + str(unit.get_hp()) + ")"
        for i in range(20 - lp):
            r += " "
        r += "| "
        return r

    def print(self):
        line_max = 1
        nb_back = 0
        nb_front = 0
        nb_e_front = 0
        nb_e_back = 0
        for i in range(len(self.__back)):
            nb_back += 1
            if i + 1 > line_max:
                line_max = i + 1
        for i in range(len(self.__front)):
            nb_front += 1
            if i + 1 > line_max:
                line_max = i + 1
        for i in range(len(self.__e_front)):
            nb_e_front += 1
            if i + 1 > line_max:
                line_max = i + 1
        for i in range(len(self.__e_back)):
            nb_e_back += 1
            if i + 1 > line_max:
                line_max = i + 1
        p = ""
        for i in range(line_max):
            p += "|"
            if i < nb_back:
                p += self.print_unit_name(self.__back[i])
            else:
                for j in range(20):
                    p += " "
                p += "| "
            if i < nb_front:
                name = self.__front[i].get_name()
                p += self.print_unit_name(self.__front[i])
            else:
                for j in range(20):
                    p += " "
                p += "| "
            if i < nb_e_front:
                name = self.__e_front[i].get_name()
                p += self.print_unit_name(self.__e_front[i])
            else:
                for j in range(20):
                    p += " "
                p += "| "
            if i < nb_e_back:
                name = self.__e_back[i].get_name()
                p += self.print_unit_name(self.__e_back[i])
            else:
                for j in range(20):
                    p += " "
                p += "| "
            p += "\n"
        print(p)
        p = ""

    def __del__(self):
        self.__back.clear()
        self.__front.clear()
        self.__e_front.clear()
        self.__e_back.clear()
