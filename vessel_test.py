import unittest
from vessel import *

class TestVessel(unittest.TestCase):
    def test_initialization(self):
        weapon = Weapon(ammunitions=10, range=50)
        coordinates = (1, 2, 3)
        max_hits = 5
        vessel = Vessel(coordinates, max_hits, weapon)

        self.assertEqual(vessel.coordinates, coordinates)
        self.assertEqual(vessel.max_hits, max_hits)
        self.assertEqual(vessel.weapon, weapon)