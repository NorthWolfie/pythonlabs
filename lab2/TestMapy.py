import unittest
from MapClass import BasicMap
from UnitClass import Infantry


class TestMapy(unittest.TestCase):

    def setUp(self):
        self.map = BasicMap(10)
        self.map.CreateMap()

    def test_UnitPos(self):
        unit1 = Infantry()
        self.map.AddUnit(unit1, 1, "")
        self.assertEqual(unit1.Position[0], 0)
        self.assertEqual(unit1.Position[1], 0)

    def test_NotStackUnit(self):
        unit1 = Infantry()
        self.map.AddUnit(unit1, 1, "")
        unit2 = Infantry()
        self.map.AddUnit(unit2, 1, "")
        self.assertEqual(unit2.Position[0], 0)
        self.assertEqual(unit2.Position[1], 1)


if __name__ == "__main__":
    unittest.main()
