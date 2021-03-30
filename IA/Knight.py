# combat
from model.Knight import Knight
from model.KnightClasse import KnightClasse


def fight():
    id = 1
    name = "Arthur"+str(id)
    level = 1
    classe = KnightClasse(1, "ecu", 0, 0, 0, 0, [])
    affinityOff = 0
    affinityDef = 0
    affinitySupp = 0
    strength = 3
    agility = 3
    constitution = 2
    mana = 0
    mastery = 1
    luck = 2

    knight1 = Knight(id, name, level, classe, affinityOff, affinityDef, affinitySupp, strength, agility, constitution, mana, mastery, luck)
    id = 2
    knight2 = Knight(id, name, level, classe, affinityOff, affinityDef, affinitySupp, strength, agility, constitution, mana, mastery, luck)
    army = [knight1, knight2]
    for knight in army:
        knight.print()
    return 0

# def
