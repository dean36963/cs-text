from Character import Character
from Actions import *
from Sides import *
from Routes import *
from Locations import TerroristSpawn
from random import randint


class NPC(Character):
    def __init__(self, side):
        Character.__init__(self, side)
        self.route = None

    def get_action(self, info):
        if self.side == Terrorist:
            return self.get_t_action(info)
        else:
            return self.get_ct_action(info)

    def get_t_action(self, info):
        """
        First terrorist to move randomly decides a route.
        Then it starts moving in the direction of that route.
        Subsequent terrorists lookup the route based on the first movement.
        They then also move in that route.
        :param info:
        :return:
        """
        if info.enemies_in_sight():
            return Shoot(list(info.enemies_in_sight().keys())[0], self)
        if not self.route:
            for team in info.team_mates():
                if team.location != TerroristSpawn:
                    # this teammate has moved, get route from this
                    self.route = get_t_route_from_first_move(team.location)
                    break
            # no team mate has yet moved, pick a route
            route_num = randint(1,3)
            if route_num == 1:
                self.route = TSpawnToAViaLong()
            elif route_num == 2:
                self.route = TSpawnToAViaShort()
            elif route_num == 3:
                self.route = TSpawnToBViaTunnels()
        if self.route:
            new_location = self.route.get_next_location(self.location)
            if new_location:
                return Move(new_location, self)
        if self.has_bomb:
            return Plant
        return Wait

    def get_ct_action(self, info):
        """
        Chooses A or B randomly. A route is picked accordingly.
        They then stay there until an enemy is sighted by any member of the team.
        They can choose to jump from A to B.
        :param info:
        :return:
        """
        route_num = randint(1,2)
        if route_num == 1:
            self.route = CTSpawnToA()
        else:
            self.route = CTSpawnToB()
        if info.enemies_in_sight():
            return Shoot(list(info.enemies_in_sight().keys())[0], self)
        if self.route:
            new_location = self.route.get_next_location(self.location)
            if new_location:
                return Move(new_location, self)
        # bomb stuff
        return Wait