

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
     super().__init__(hp,am)
     self.attack = att
     self.speed = spd

    def move(self):
        pass

    def MakeDMG(self):
        pass

class Infantry(Person):

     def takeDefence(self):
         pass

class Archer(Person):

    def __init__(self, hp, am, att, spd, qv):
        super().__init__(hp,am,att,spd)
        self.quiver = qv

    def isquiverEmpty(self):
        if self.quiver > 0:
            return  True
        else:
            return False

class Cavalry(Person):
    pass

class ShieldInfantry(Infantry):
    pass

class HeavyInfantry(Infantry):
    pass

class Bowman(Archer):
    pass

class Crossbowman(Archer):
    pass

class LightCavalry(Cavalry):
    pass

class HeavyCavalry(Cavalry):
    pass