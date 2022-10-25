import MapClass
from MapClass import Wood, Stone, Gold
from MapClass import Swamp, Mountain, Hill, Field


class Unit:

    def __init__(self, hp, am):
        self.health = hp
        self.armor = am

    def getHP(self):
        print(self.health)


class Building(Unit):
    current_units = []

    def Create_unit(self, index):
        unit = Unit()
        if index == 1:
            unit = Infantry()
        elif index == 2:
            unit = Archer()
        elif index == 3:
            unit = Cavalry()
        self.current_units.append(unit)


class Person(Unit):

    def __init__(self, hp, am, att, spd, shrt, clr):
        super().__init__(hp, am)
        self.attack = att
        self.speed = spd
        self.Short = shrt
        self.Color = clr

    def Move(self):
        return self.speed

    def MakeDMG(self):
        return self.attack

    """
    def getResist(self, dmg):
        res_dmg = dmg - dmg / 100 * self.armor
        return res_dmg

    def getItem(self, short):

        if short == '~':
            ob = Swamp()
            self.attack -= ob.attack
            self.speed -= ob.speed
        elif short == '^':
            ob = Mountain()
            self.attack -= ob.attack
            self.speed += ob.speed
        elif short == '*':
            ob = Hill()
            self.attack -= ob.attack
            self.speed -= ob.speed

        if short == 'W':
            wood = Wood()
            return wood.Value
        elif short == 'S':
            wood = Stone()
            return wood.Value
        elif short == 'G':
            wood = Gold()
            return wood.Value
    """


class Worker(Person):
    pass


class Infantry(Person):

    def __init__(self):
        super().__init__(10, 5, 1, 1, "I", "\033[34m")

    def takeDefence(self):
        self.armor += 5

    def OutOfDefence(self):
        self.armor -= 5


class ShieldInfantry(Infantry):

    def __init__(self):
        super().__init__()
        self.armor = 8
        self.Short = "SI"

    def takeDefence(self):
        super().takeDefence()
        self.attack += 0.3

    def OutOfDefence(self):
        super().OutOfDefence()
        self.attack -= 0.3


class HeavyInfantry(Infantry):

    def __init__(self):
        super().__init__()
        self.armor = 3
        self.attack = 1.5
        self.Short = "HI"

    def takeDefence(self):
        super().takeDefence()
        self.attack -= 0.3

    def OutOfDefence(self):
        super().OutOfDefence()
        self.attack += 0.3


class Archer(Person):

    def __init__(self):
        super().__init__(10, 2, 1, 1, "A", "\033[31m")
        self.quiver = 5
        self.rangeDMG = 1
        self.range = 1.5

    def isQuiverEmpty(self):
        if self.quiver > 0:
            return False
        else:
            return True


class Bowman(Archer):

    def __init__(self):
        super().__init__()
        self.range = 3
        self.rangeDMG = 2
        self.Short = "BN"

    def MultiShooting(self):
        self.rangeDMG *= 1.5
        self.quiver = 0


class Crossbowman(Archer):

    def __init__(self):
        super().__init__()
        self.range = 5
        self.rangeDMG = 2.5
        self.Short = "CN"


class Cavalry(Person):

    def __init__(self):
        super().__init__(15, 5, 1.5, 3, "C", "\033[32m")


class LightCavalry(Cavalry):

    def __init__(self):
        super().__init__()
        self.speed = 4
        self.Short = "LC"


class HeavyCavalry(Cavalry):

    def __init__(self):
        super().__init__()
        self.speed = 2
        self.Short = "HC"

    def Charge(self):
        self.attack *= 1.3
        self.armor *= 0.7
