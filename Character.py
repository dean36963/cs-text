from Sides import *
from Locations import TerroristSpawn, CTSpawn


class Character:
    def __init__(self, side):
        if not issubclass(side, Side):
            raise Exception("Not a valid side.")
        self.side = side
        if side == Terrorist:
            self.location = TerroristSpawn
        else:
            self.location = CTSpawn
        # TODO Weapons
        self.health = 100
        self.has_bomb = False
        self.next_move = None

    def set_next_move(self, new_location):
        self.next_move = new_location
    def do_move(self):
        if self.next_move:
            self.location = self.next_move
            self.next_move = None

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def is_dead(self):
        return not self.is_alive()

    def accuracy(self):
        # TODO depends on weapons, whether is waiting etc
        return 0.6

    def set_location(self, location):
        self.location = location

    def got_shot(self, weapon=None, headshot=False):
        damage = 50
        if headshot:
            damage += 20
        self.health -= damage

    def give_bomb(self):
        self.has_bomb = True

    def get_action(self, info=None):
        raise NotImplementedError("Subclasses must create behaviour.")
