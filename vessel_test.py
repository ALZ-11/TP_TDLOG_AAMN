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

class TestCruiser(unittest.TestCase):

    def test_cruiser_initialization(self):
        coordinates = (1, 2, 0) 
        cruiser = Cruiser(coordinates)
        self.assertEqual(cruiser.coordinates, coordinates)
        self.assertEqual(cruiser.max_hits, 6)
        self.assertIsInstance(cruiser.weapon, Lance_missiles_antiair)
    
    def test_cruiser_initialization_invalid_coordinates(self):
        coordinates = (1, 2, 1)  
        with self.assertRaises(OutOfCapabilityError):
            Cruiser(coordinates)

    def test_cruiser_go_to_valid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 0)
        cruiser = Cruiser(initial_coordinates)
        cruiser.go_to(new_coordinates)
        self.assertEqual(cruiser.coordinates, new_coordinates)

    def test_cruiser_go_to_invalid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 1)  
        cruiser = Cruiser(initial_coordinates)
        with self.assertRaises(OutOfCapabilityError):
            cruiser.go_to(new_coordinates)

class TestSubmarine(unittest.TestCase):

    def test_submarine_initialization(self):
        coordinates = (1, 2, -1)  
        submarine = Submarine(coordinates)
        self.assertEqual(submarine.coordinates, coordinates)
        self.assertEqual(submarine.max_hits, 2)
        self.assertIsInstance(submarine.weapon, Lance_tropilles)

    def test_submarine_initialization_invalid_coordinates(self):
        coordinates = (1, 2, 1)  
        with self.assertRaises(OutOfCapabilityError):
            Submarine(coordinates)

    def test_submarine_go_to_valid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 0)
        submarine = Submarine(initial_coordinates)
        submarine.go_to(new_coordinates)
        self.assertEqual(submarine.coordinates, new_coordinates)

    def test_submarine_go_to_invalid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 1)  
        submarine = Submarine(initial_coordinates)
        with self.assertRaises(OutOfCapabilityError):
            submarine.go_to(new_coordinates)

class TestFregate(unittest.TestCase):

    def test_fregate_initialization(self):
        coordinates = (1, 2, 0) 
        fregate = Fregate(coordinates)
        self.assertEqual(fregate.coordinates, coordinates)
        self.assertEqual(fregate.max_hits, 5)
        self.assertIsInstance(fregate.weapon, Lance_missiles_antisurface)

    def test_fregate_initialization_invalid_coordinates(self):
        coordinates = (1, 2, 1) 
        with self.assertRaises(OutOfCapabilityError):
            Fregate(coordinates)

    def test_fregate_go_to_valid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 0)
        fregate = Fregate(initial_coordinates)
        fregate.go_to(new_coordinates)
        self.assertEqual(fregate.coordinates, new_coordinates)

    def test_fregate_go_to_invalid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 1) 
        fregate = Fregate(initial_coordinates)
        with self.assertRaises(OutOfCapabilityError):
            fregate.go_to(new_coordinates)

class TestDestroyer(unittest.TestCase):

    def test_destroyer_initialization(self):
        coordinates = (1, 2, 0) 
        destroyer = Destroyer(coordinates)
        self.assertEqual(destroyer.coordinates, coordinates)
        self.assertEqual(destroyer.max_hits, 4)
        self.assertIsInstance(destroyer.weapon, Lance_tropilles)

    def test_destroyer_initialization_invalid_coordinates(self):
        coordinates = (1, 2, 1)  
        with self.assertRaises(OutOfCapabilityError):
            Destroyer(coordinates)

    def test_destroyer_go_to_valid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 0)
        destroyer = Destroyer(initial_coordinates)
        destroyer.go_to(new_coordinates)
        self.assertEqual(destroyer.coordinates, new_coordinates)

    def test_destroyer_go_to_invalid_coordinates(self):
        initial_coordinates = (1, 2, 0)
        new_coordinates = (4, 5, 1) 
        destroyer = Destroyer(initial_coordinates)
        with self.assertRaises(OutOfCapabilityError):
            destroyer.go_to(new_coordinates)

class TestAircraft(unittest.TestCase):

    def test_aircraft_initialization(self):
        coordinates = (1, 2, 1)
        aircraft = Aircraft(coordinates)
        self.assertEqual(aircraft.coordinates, coordinates)
        self.assertEqual(aircraft.max_hits, 1)
        self.assertIsInstance(aircraft.weapon, Lance_missiles_antisurface)

    def test_aircraft_initialization_invalid_coordinates(self):
        coordinates = (1, 2, 0) 
        with self.assertRaises(OutOfCapabilityError):
            Aircraft(coordinates)

    def test_aircraft_go_to_valid_coordinates(self):
        initial_coordinates = (1, 2, 1)
        new_coordinates = (4, 5, 1)
        aircraft = Aircraft(initial_coordinates)
        aircraft.go_to(new_coordinates)
        self.assertEqual(aircraft.coordinates, new_coordinates)

    def test_aircraft_go_to_invalid_coordinates(self):
        initial_coordinates = (1, 2, 1)
        new_coordinates = (4, 5, 0)
        aircraft = Aircraft(initial_coordinates)
        with self.assertRaises(OutOfCapabilityError):
            aircraft.go_to(new_coordinates)