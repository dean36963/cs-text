from NPC import NPC
from Player import Player
from random import randint
from Sides import *
from Actions import *
from RoundInfo import RoundInfo


class RoundController:

    def __init__(self):
        self.players = []
        self.bomb_set = False
        self.time_left = 15

    def start(self):
        player_is_terrorist = randint(0,1)
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
            players_died_this_round = []
            for player in self.players:
                if player.is_dead():
                    continue
                info = RoundInfo(player, -1, self.players)
                action = player.get_action(info=info)
                if isinstance(action, Wait):
                    pass
                if isinstance(action, Move):
                    player.set_location(action.option)
                if isinstance(action, Shoot):
                    location = action.option
                    for target in self.players:
                        if target.is_dead():
                            continue
                        if target.side == player.side:
                            continue
                        if target.location == location:
                            if player.accuracy()*100 > randint(0,100):
                                target.got_shot()
                                if target.is_dead():
                                    print("{} side killed {} player.".format(
                                        player.side,
                                        target.side
                                    ))
                                    players_died_this_round.append(target)
                                    if isinstance(target, Player):
                                        print("You got pwned.")
            for dead_player in players_died_this_round:
                self.players.remove(dead_player)
