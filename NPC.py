from Character import Character
from Actions import *
from Sides import *


class NPC(Character):
    def get_action(self, info=None):
        if self.side == Terrorist:
            return self.get_t_action(self, info)
        else:
            return self.get_ct_action(self,info)

    def get_t_action(self, info):
        """
        First terrorist to move randomly decides a route.
        Then it starts moving in the direction of that route.
        Subsequent terrorists lookup the route based on the first movement.
        They then also move in that route.
        :param info:
        :return:
        """
        return Wait

    def get_ct_action(self, info):
        """
        Chooses A or B randomly. A route is picked accordingly.
        They then stay there until an enemy is sighted by any member of the team.
        They can choose to jump from A to B.
        :param info:
        :return:
        """
        return Wait