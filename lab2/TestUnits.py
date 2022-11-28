import unittest
from UnitClass import Building, Infantry, Archer, Cavalry, Person


class TestUnits(unittest.TestCase):

    def setUp(self):
        self.build = Building(10, 1)
        self.inf = Infantry()
        self.arc = Archer()
        self.cav = Cavalry()

    def test_CreateInf(self):
        unit = self.build.Create_unit("1")
        self.assertEqual(type(unit), type(self.inf))

    def test_CreateArc(self):
        unit = self.build.Create_unit("2")
        self.assertEqual(type(unit), type(self.arc))

    def test_CreateCav(self):
        unit = self.build.Create_unit("3")
        self.assertEqual(type(unit), type(self.cav))

    def test_WrongCreate(self):
        unit = self.build.Create_unit(1)
        self.assertEqual(unit, None)

    def test_OutofRes(self):
        bd = Building(1, 5)
        bd.current_wood = 0
        self.assertEqual(bd.Create_unit(1), None)

    def test_deff(self):
        inf2 = Infantry()
        self.inf.takeDefence()
        self.assertGreaterEqual(self.inf.armor, inf2.armor)

    def test_outdeff(self):
        self.inf2 = Infantry()
        self.inf.OutOfDefence()
        self.assertLessEqual(self.inf.armor, self.inf2.armor)

    def test_Quiver(self):
        self.assertFalse(self.arc.isQuiverEmpty())

    def test_QuiverNull(self):
        self.arc.quiver = 0
        self.assertTrue(self.arc.isQuiverEmpty())


if __name__ == "__main__":
    unittest.main()
