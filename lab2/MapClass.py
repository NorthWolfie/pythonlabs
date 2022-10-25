import random


class BasicMap:
    PrevMap = list()

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
        f = Field()
        s = Swamp()
        m = Mountain()
        h = Hill()
        w = Wood()
        st = Stone()
        g = Gold()
        # self.MAX_Ress()
        self.Items = {1: f, 2: s, 3: m, 4: h, 5: w, 6: st, 7: g}

    def MAXRes(self):
        self.MAX_Mountains *= (self.Size / 100)
        self.MAX_Hills *= (self.Size / 100)
        self.MAX_Swamp *= (self.Size / 100)
        self.MAX_Wood *= (self.Size / 100)
        self.MAX_Stone *= (self.Size / 100)
        self.MAX_Gold *= (self.Size / 100)

    def ArrayToString(self):
        i = 0
        while i != self.Size:
            j = 0
            while j < self.Size:
                index = 0
                for key, value in self.Items.items():
                    if self.PrevMap[i][j] == value:
                        index = key
                        break
                if i == j == 1:
                    self.line += " " + "\033[35mB" + " "
                else:
                    self.line += " " + self.Items[index].Color + self.Items[index].Short + " "
                self.PrevMap[i][j] = self.Items[index].Short
                j += 1
            self.CurrentS = self.CurrentM = self.CurrentH = self.CurrentW = self.CurrentSt = self.CurrentG = 0
            print("\033[37m|" + self.line + "\033[37m|")
            self.line = ""
            i += 1

    def CreateLine(self):
        pass

    def Create(self):
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
                    elif index == 6 and prev != 6 and self.MAX_Stone > self.CurrentSt:
                        self.CurrentSt += 1
                        flag = False
                    elif index == 7 and prev != 7 and self.MAX_Gold > self.CurrentG:
                        self.CurrentG += 1
                        flag = False
                    else:
                        index = 1
                        flag = False
                    prev = index
                flag = True
                if i == j == 1:
                    self.line += " " + "\033[35mB" + " "
                else:
                    self.line += " " + self.Items[index].Color + self.Items[index].Short + " "
                self.PrevMap[i][j] = self.Items[index].Short
                j += 1
            self.CurrentS = self.CurrentM = self.CurrentH = self.CurrentW = self.CurrentSt = self.CurrentG = 0
            print("\033[37m|" + self.line + "\033[37m|")
            self.line = ""
            i += 1


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
        super().__init__("Swamp", "~", "\033[1m\033[34m", 0, 1)


class Mountain(Obstacles):

    def __init__(self):
        super().__init__("Mountain", "^", "\033[1m\033[31m", 0, -10)


class Hill(Obstacles):

    def __init__(self):
        super().__init__("Hill", "*", "\033[1m\033[33m", -5, -1)
