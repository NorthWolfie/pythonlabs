class Unit:

    def __init__(self, hp, am):
        self.health = hp
        self.armor = am

    def getHP(self):
        print(self.health)


class Building(Unit):

    def create_unit(self):
        pass


class MainBuilding(Building):
    pass


class Person(Unit):

    def __init__(self, hp, am, att, spd):
        super().__init__(hp, am)
        self.attack = att
        self.speed = spd

    def Move(self):
        return self.speed

    def MakeDMG(self):
        return self.attack

    def getResist(self, dmg):
        res_dmg = dmg - dmg / 100 * self.armor
        return res_dmg


class Infantry(Person):

    def __init__(self):
        super().__init__(10, 5, 1, 1)

    def takeDefence(self):
        self.armor += 5

    def OutOfDefence(self):
        self.armor -= 5


class ShieldInfantry(Infantry):

    def __init__(self):
        super().__init__()
        self.armor = 8

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

    def takeDefence(self):
        super().takeDefence()
        self.attack -= 0.3

    def OutOfDefence(self):
        super().OutOfDefence()
        self.attack += 0.3


class Archer(Person):

    def __init__(self):
        super().__init__(10, 2, 1, 1)
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

    def MultiShooting(self):
        self.rangeDMG *= 1.5
        self.quiver = 0


class Crossbowman(Archer):

    def __init__(self):
        super().__init__()
        self.range = 5
        self.rangeDMG = 2.5


class Cavalry(Person):

    def __init__(self):
        super().__init__(15, 5, 1.5, 3)


class LightCavalry(Cavalry):

    def __init__(self):
        super().__init__()
        self.speed = 4


class HeavyCavalry(Cavalry):

    def __init__(self, hp, am, att, spd):
        super().__init__()
        self.speed = 2

    def Charge(self):
        self.attack *= 1.3
        self.armor *= 0.7
