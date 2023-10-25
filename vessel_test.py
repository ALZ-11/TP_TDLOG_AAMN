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
    def test_get_coordinates(self):
        coordinates = (1, 2, 3)
        vessel = Vessel(coordinates, 5, Weapon(10, 50))
        self.assertEqual(vessel.get_coordinates(), coordinates)
    def test_go_to(self):
        initial_coordinates = (1, 2, 3)
        new_coordinates = (4, 5, 6)
        vessel = Vessel(initial_coordinates, 5, Weapon(10, 50))
        vessel.go_to(new_coordinates)
        self.assertEqual(vessel.coordinates, new_coordinates)