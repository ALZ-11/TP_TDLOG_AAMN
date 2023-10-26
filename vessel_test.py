import unittest
from vessel import *

class TestVessel(unittest.TestCase):
    def test_initialization(self):
        weapon = Weapon(10, 50)
        coordinates = (1, 2, 3)
        max_hits = 5
        vessel = Vessel(coordinates, max_hits, weapon)
        self.assertEqual(vessel.coordinates, coordinates)
        self.assertEqual(vessel.max_hits, max_hits)
        self.assertEqual(vessel.weapon, weapon)
    def test_get_coordinates_not_destroyed(self):
        coordinates = (1, 2, 3)
        vessel = Vessel(coordinates, 5, Weapon(10, 50))
        self.assertEqual(vessel.get_coordinates(), coordinates)
    def test_get_coordinates_is_destroyed(self):
        coordinates = (1, 2, 3)
        vessel = Vessel(coordinates, 0, Weapon(10, 50))
        with self.assertRaises(DestroyedError):
            vessel.get_coordinates()
    def test_go_to_not_destroyed(self):
        initial_coordinates = (1, 2, 3)
        new_coordinates = (4, 5, 6)
        vessel = Vessel(initial_coordinates, 5, Weapon(10, 50))
        vessel.go_to(new_coordinates)
        self.assertEqual(vessel.coordinates, new_coordinates)
    def test_go_to_is_destroyed(self):
        initial_coordinates = (1, 2, 3)
        new_coordinates = (4, 5, 6)
        vessel = Vessel(initial_coordinates, 0, Weapon(10, 50))
        with self.assertRaises(DestroyedError):
            vessel.go_to(new_coordinates)
    def test_fire_at_not_destroyed_within_range(self):
        weapon = Weapon(10, 50)
        vessel = Vessel((1, 2, 3), 5, weapon)
        self.assertIsNone(vessel.fire_at(2, 3, 0))
        self.assertEqual(weapon.ammunitions, 9)
    def test_fire_at_is_destroyed(self):
        weapon = Weapon(10, 50)
        vessel = Vessel((1, 2, 3), 0, weapon)
        with self.assertRaises(DestroyedError):
            vessel.fire_at(1, 1, 1)
    def test_fire_at_out_of_range(self):
        weapon = Weapon(10, 1)
        vessel = Vessel((0, 0, 0), 5, weapon)
        with self.assertRaises(OutOfRangeError):
            vessel.fire_at(1, 1, 1)
        self.assertEqual(weapon.ammunitions, 9)