class NoAmmoError(Exception):
    def __init__(self, message="No ammo left. Cannot fire."):
        self.message = message
        super().__init__(self.message)

class Weapon:
    def __init__(self, ammunitions : int, range : int):
        self.ammunitions = ammunitions
        self.range = range
    def fire_at(self, x : int, y : int, z : int):
        try:
            assert self.ammunitions > 0
        except:
            raise NoAmmoError