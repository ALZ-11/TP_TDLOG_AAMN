import unittest
from weapon import Weapon, NoAmmoError

class TestWeapon(unittest.TestCase):
    def test_initialization(self):
        weapon = Weapon(10, 50)
        self.assertEqual(weapon.ammunitions, 10)
        self.assertEqual(weapon.range, 50)
    def test_fire_at_with_ammo(self):
        weapon = Weapon(ammunitions=10, range=50)
        self.assertIsNone(weapon.fire_at(1, 2, 3))
    def test_fire_at_without_ammo(self):
        weapon = Weapon(ammunitions=0, range=50)
        with self.assertRaises(NoAmmoError):
            weapon.fire_at(1, 2, 3)