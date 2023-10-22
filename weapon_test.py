import unittest
from weapon import Weapon, Lance_missiles_antisurface, OutOfRangeError, NoAmmoError

class TestWeapon(unittest.TestCase):
    def test_initialization(self):
        weapon = Weapon(10, 50)
        self.assertEqual(weapon.ammunitions, 10)
        self.assertEqual(weapon.range, 50)
    def test_fire_at_with_ammo(self):
        weapon = Weapon(10, 50)
        self.assertIsNone(weapon.fire_at(1, 2, 3))
    def test_fire_at_without_ammo(self):
        weapon = Weapon(0, 50)
        with self.assertRaises(NoAmmoError):
            weapon.fire_at(1, 2, 3)
            
class TestLanceMissilesAntiSurface(unittest.TestCase):
    def test_initialization(self):
        weapon = Lance_missiles_antisurface()
        self.assertEqual(weapon.ammunitions, 50)
        self.assertEqual(weapon.range, 100)

    def test_fire_at_within_range(self):
        weapon = Lance_missiles_antisurface()
        self.assertIsNone(weapon.fire_at(1, 2, 0))
        self.assertEqual(weapon.ammunitions, 49)  

    def test_fire_at_out_of_range(self):
        weapon = Lance_missiles_antisurface()
        with self.assertRaises(OutOfRangeError):
            weapon.fire_at(1, 2, 1)

    def test_fire_at_without_ammo(self):
        weapon = Lance_missiles_antisurface()
        for _ in range(50):
            self.assertIsNone(weapon.fire_at(1, 2, 0)) # consommer toute l'ammo
        with self.assertRaises(NoAmmoError):
            weapon.fire_at(1, 2, 0)

class TestLanceMissilesAntiAir(unittest.TestCase):
    def test_initialization(self):
        weapon = Lance_missiles_antisurface()
        self.assertEqual(weapon.ammunitions, 40)
        self.assertEqual(weapon.range, 20)

    def test_fire_at_within_range(self):
        weapon = Lance_missiles_antisurface()
        self.assertIsNone(weapon.fire_at(1, 2, 0))
        self.assertEqual(weapon.ammunitions, 39)  

    def test_fire_at_out_of_range(self):
        weapon = Lance_missiles_antisurface()
        with self.assertRaises(OutOfRangeError):
            weapon.fire_at(1, 2, 0)

    def test_fire_at_without_ammo(self):
        weapon = Lance_missiles_antisurface()
        for _ in range(40):
            self.assertIsNone(weapon.fire_at(1, 2, 1)) # consommer toute l'ammo
        with self.assertRaises(NoAmmoError):
            weapon.fire_at(1, 2, 1)