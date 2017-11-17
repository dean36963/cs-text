from Character import Character
from Actions import *


class NPC(Character):
    def get_action(self, info=None):
        return Wait
