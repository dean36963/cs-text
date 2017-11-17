from NPC import NPC
from Player import Player
from random import randrange
from Sides import *
from Actions import *


class RoundController:

    def __init__(self):
        self.players = []
        self.bomb_set = False
        self.time_left = 15

    def start(self):
        player_is_terrorist = randrange(0,1)
        if player_is_terrorist:
            self.players.append(Player(Terrorist))
            self.players.append(NPC(CounterTerrorist))
        else:
            self.players.append(Player(CounterTerrorist))
            self.players.append(NPC(Terrorist))

        for i in range(1,5):
            self.players.append(NPC(CounterTerrorist))
            self.players.append(NPC(Terrorist))

    # I would set 15 rounds, but my God you'd be bored
    # Don't get me wrong, you'll still be bored...
    def loop(self, rounds=5):
        while self.players:
            for player in self.players:
                action = player.get_action(info=None)
                if isinstance(action, Move):
                    player.set_location(action.option)