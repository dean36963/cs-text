from NPC import NPC
from Player import Player
from random import randint
from Sides import *
from Actions import *
from RoundInfo import RoundInfo


class RoundController:

    def __init__(self):
        self.players = []
        self.time_left = 15
        # -1 for not yet set
        # Set to 10 when armed, and goes down each round
        # set to 99 when defused
        self.time_til_bomb = -1
        self.ct_rounds = 0
        self.t_rounds = 0

    def start(self):
        self.players = []
        self.time_left = 15
        self.time_til_bomb = -1
        self.ct_rounds = 0
        self.t_rounds = 0
        player_is_terrorist = randint(0, 1)
        if player_is_terrorist:
            self.players.append(Player(Terrorist))
            self.players.append(NPC(CounterTerrorist))
        else:
            self.players.append(Player(CounterTerrorist))
            self.players.append(NPC(Terrorist))

        for i in range(1, 5):
            self.players.append(NPC(CounterTerrorist))
            self.players.append(NPC(Terrorist))

    def side_winning_round(self):
        ct_players = []
        t_players = []
        for player in self.players:
            if player.side == CounterTerrorist:
                ct_players.append(player)
            else:
                t_players.append(player)
        if len(ct_players) == 0:
            # CT eliminated in time
            return Terrorist
        if len(t_players) == 0 and \
            self.time_til_bomb -1:
            # Bomb was never set and T eliminated
            return CounterTerrorist
        if self.time_til_bomb == 99:
            # Bomb was defused
            return CounterTerrorist
        if self.time_til_bomb == 0:
            # Bomb exploded
            return Terrorist
        return None

    # I would set 15 rounds, but my God you'd be bored
    # Don't get me wrong, you'll still be bored...
    def loop(self, rounds=5):
        for round_num in range(1, rounds+1):
            self.start()
            print("Round {} of {}".format(round_num, rounds))
            print("Score: {}:{} - {}:{}".format(
                CounterTerrorist.str(),
                self.ct_rounds,
                self.t_rounds,
                Terrorist.str()
            ))
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
                                            player.side.str(),
                                            target.side.str()
                                        ))
                                        players_died_this_round.append(target)
                                        if isinstance(target, Player):
                                            print("You got pwned.")
                                    elif isinstance(player, Player):
                                        print("You hit an enemy.")
                for dead_player in players_died_this_round:
                    self.players.remove(dead_player)
                self.time_left -= 1
                if self.side_winning_round():
                    print("{} win round!".format(
                        self.side_winning_round().str()
                    ))
                    print("")
                    break
            if self.side_winning_round() == Terrorist:
                self.t_rounds += 1
            else:
                self.ct_rounds += 1
