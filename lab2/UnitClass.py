def getResist(armor, dmg):
    res_dmg = dmg - dmg / 100 * armor
    return res_dmg


class Unit:

    def __init__(self, hp, am):
        self.health = hp
        self.armor = am

    def getHP(self):
        print(self.health)


class Building(Unit):

    def create_unit(self):
        pass


class Person(Unit):

    def __init__(self, hp, am, att, spd):
        super().__init__(hp, am)
        self.attack = att
        self.speed = spd

    def move(self):
        pass

    def MakeDMG(self):
        pass


class Infantry(Person):

    def takeDefence(self):
        self.am += 5;


class ShieldInfantry(Infantry):

    def takeDefence(self):
        super().takeDefence()
        self.attack += 5;


class HeavyInfantry(Infantry):

    def takeDefence(self):
        super().takeDefence()
        self.attack -= 5;


class Archer(Person):

    def __init__(self, hp, am, att, spd, qv):
        super().__init__(hp, am, att, spd)
        self.quiver = qv

    def isQuiverEmpty(self):
        if self.quiver > 0:
            return True
        else:
            return False


class Bowman(Archer):

    def MultiShooting(self):
        self.attack *= 1.2


class Crossbowman(Archer):
    pass


class Cavalry(Person):
    def __init__(self, hp, am, att, spd):
        super().__init__(hp, am, att, spd)


class LightCavalry(Cavalry):
    def __init__(self, hp, am, att, spd):
        super().__init__(hp, am, att, spd)


class HeavyCavalry(Cavalry):
    def __init__(self, hp, am, att, spd):
        super().__init__(hp, am, att, spd)

    def Charge(self):
        self.attack *= 1.3
        self.armor *= 0.7
