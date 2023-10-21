import unittest
from weapon import Weapon

class TestWeapon(unittest.TestCase):
    def test_initialization(self):
        weapon = Weapon(10, 50)
        self.assertEqual(weapon.ammunitions, 10)
        self.assertEqual(weapon.range, 50)