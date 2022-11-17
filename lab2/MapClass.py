import os
import random
from UnitClass import Infantry, ShieldInfantry, HeavyInfantry, Archer, Bowman, Crossbowman, Cavalry, LightCavalry, \
    HeavyCavalry
from random import randint


def MakeItFill(size):
    a = [[randint(0, 1) for j in range(size)] for i in range(size)]
    return a


def CheckBoder(index, size):
    if index < 0:
        index = 0
    elif index > size:
        index = size
    return index


class BasicMap:
    Resource = list()

    MAX_Mountains = 1
    CurrentM = 0

    MAX_Hills = 4
    CurrentH = 0

    MAX_Swamp = 4
    CurrentS = 0

    MAX_Wood = 7
    CurrentW = 0

    MAX_Stone = 7
    CurrentSt = 0

    MAX_Gold = 6
    CurrentG = 0

    def __init__(self, size):
        # self.updown = "--"
        self.CurrentMap = ""
        self.Size = size
        self.line = ""
        self.PrevMap = MakeItFill(size)
        f = Field()
        s = Swamp()
        m = Mountain()
        h = Hill()
        w = Wood()
        st = Stone()
        g = Gold()
        I = Infantry()
        SI = ShieldInfantry()
        HI = HeavyInfantry()
        A = Archer()
        BN = Bowman()
        CN = Crossbowman()
        C = Cavalry()
        LC = LightCavalry()
        HC = HeavyCavalry()
        # self.MAX_Ress()
        self.Items = {1: f, 2: s, 3: m, 4: h, 5: w, 6: st, 7: g, 8: I, 9: SI, 10: HI, 11: A, 12: BN, 13: CN, 14: C,
                      15: LC, 16: HC}

    """
    def MAXRes(self):
        self.MAX_Mountains /= 100 * self.Size
        self.MAX_Hills /= 100 * self.Size
        self.MAX_Swamp /= 100 * self.Size
        self.MAX_Wood /= 100 * self.Size
        self.MAX_Stone /= 100 * self.Size
        self.MAX_Gold /= 100 * self.Size
    """

    def ArrayToString(self):
        i = 0
        while i != self.Size:
            j = 0
            while j < self.Size:
                key = 0
                for key in self.Items.keys():
                    if self.PrevMap[i][j] == key:
                        break
                if i == j == 1:
                    self.line += " " + "\033[35mB" + " "
                else:
                    self.line += " " + self.Items[key].Color + self.Items[key].Short + " "
                j += 1
            self.CurrentS = self.CurrentM = self.CurrentH = self.CurrentW = self.CurrentSt = self.CurrentG = 0
            i += 1
            print("\033[37m|" + self.line + "\033[37m|")
            self.line = ""

    def CreateMap(self):
        flag = True
        prev = 0
        index = 0
        i = 0
        while i != self.Size:
            j = 0
            while j < self.Size:
                while flag:
                    index = random.randint(1, 7)
                    if index == 2 and prev != 2 and self.MAX_Swamp > self.CurrentS:
                        self.CurrentS += 1
                        flag = False
                    elif index == 3 and prev != 3 and self.MAX_Mountains > self.CurrentM:
                        self.CurrentM += 1
                        flag = False
                    elif index == 4 and prev != 4 and self.MAX_Hills > self.CurrentH:
                        self.CurrentH += 1
                        flag = False
                    elif index == 5 and prev != 5 and self.MAX_Wood > self.CurrentW:
                        self.CurrentW += 1
                        flag = False
                        wood = Wood()
                        BasicMap.Resource.append(wood)
                    elif index == 6 and prev != 6 and self.MAX_Stone > self.CurrentSt:
                        self.CurrentSt += 1
                        flag = False
                        stone = Stone()
                        BasicMap.Resource.append(stone)
                    elif index == 7 and prev != 7 and self.MAX_Gold > self.CurrentG:
                        self.CurrentG += 1
                        flag = False
                        gold = Gold()
                        BasicMap.Resource.append(gold)
                    else:
                        index = 1
                        flag = False
                    prev = index
                    self.PrevMap[i][j] = prev
                flag = True
                if i == j == 1:
                    self.line += " " + "\033[35mB" + " "
                else:
                    self.line += " " + self.Items[index].Color + self.Items[index].Short + " "
                j += 1
            self.CurrentS = self.CurrentM = self.CurrentH = self.CurrentW = self.CurrentSt = self.CurrentG = 0
            print("\033[37m|" + self.line + "\033[37m|")
            self.line = ""
            i += 1

    def AddUnit(self, un, step, direction):
        x = un.Position[0]
        y = un.Position[1]
        flag = False
        while un.Position[1] < self.Size and un.Position[0] < self.Size and self.PrevMap[un.Position[0]][un.Position[1]] >= 8:
            if direction == "l":
                un.Position[1] -= step
            elif direction == "r" or direction == "":
                un.Position[1] += step
            elif direction == "u":
                un.Position[0] -= step
            elif direction == "d":
                un.Position[0] += step
            un.Position[0] = CheckBoder(un.Position[0], self.Size)
            un.Position[1] = CheckBoder(un.Position[1], self.Size)
            if not flag:
                step = 1
        if un.PrevSymbol != "":
            self.PrevMap[x][y] = un.PrevSymbol
            if un.PrevSymbol in range(1, 4):
                for key, value in self.Items.items():
                    if un.PrevSymbol == key:
                        un.attack -= value.attack
                        un.speed -= value.speed
                        break
        un.PrevSymbol = self.PrevMap[un.Position[0]][un.Position[1]]
        if un.PrevSymbol in range(1, 4):
            for key, value in self.Items.items():
                if un.PrevSymbol == key:
                    un.attack += value.attack
                    un.speed += value.speed
                    if un.attack <= 0:
                        un.attack = 1
                    if un.speed <= 0:
                        un.speed = 1
                    break
        for key, value in self.Items.items():
            if un.Short == value.Short:
                self.PrevMap[un.Position[0]][un.Position[1]] = key
                break

    def AddResourses(self, un):
        if un.PrevSymbol == 5:
            for i in range(len(BasicMap.Resource)):
                if type(BasicMap.Resource[i]) == Wood:
                    return BasicMap.Resource[i].MakeValue()
        elif un.PrevSymbol == 6:
            for i in range(len(BasicMap.Resource)):
                if type(BasicMap.Resource[i]) == Stone:
                    return BasicMap.Resource[i].MakeValue()
        elif un.PrevSymbol == 7:
            for i in range(len(BasicMap.Resource)):
                if type(BasicMap.Resource[i]) == Gold:
                    return BasicMap.Resource[i].MakeValue()


class Items:

    def __init__(self, f, sht, clr):
        self.FullName = f
        self.Short = sht
        self.Color = clr


class Obstacles(Items):

    def __init__(self, f, sht, clr, att, spd):
        super().__init__(f, sht, clr)
        self.attack = att
        self.speed = spd


class Resource(Items):

    def __init__(self, f, sht, clr, val):
        super().__init__(f, sht, clr)
        self.Value = val

    def MakeValue(self):
        return self.Value


class Wood(Resource):

    def __init__(self):
        val = random.randint(1, 10)
        super().__init__("Wood", "W", "\033[1m\033[32m", val)


class Stone(Resource):

    def __init__(self):
        val = random.randint(1, 10)
        super().__init__("Stone", "S", "\033[1m\033[31m", val)


class Gold(Resource):

    def __init__(self):
        val = random.randint(10, 100)
        super().__init__("Gold", "G", "\033[1m\033[33m", val)


class Field(Obstacles):

    def __init__(self):
        super().__init__("Field", "_", "\033[1m\033[32m", 0, 0)


class Swamp(Obstacles):

    def __init__(self):
        super().__init__("Swamp", "~", "\033[1m\033[34m", 0, -1)


class Mountain(Obstacles):

    def __init__(self):
        super().__init__("Mountain", "^", "\033[1m\033[31m", 0, -10)


class Hill(Obstacles):

    def __init__(self):
        super().__init__("Hill", "*", "\033[1m\033[33m", -5, -1)
