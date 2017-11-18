from Locations import ASite, BSite
from NPC import NPC
from Player import Player
from random import randint
from Sides import *
from Actions import *
from RoundInfo import RoundInfo


class RoundController:

    def __init__(self, player_is_terrorist):
        self.players = []
        self.time_left = 15
        # -1 for not yet set
        # Set to 10 when armed, and goes down each round
        # set to 99 when defused
        self.time_til_bomb = -1
        self.ct_rounds = 0
        self.t_rounds = 0
        self.player_is_terrorist = player_is_terrorist
        self.bomb_location = None

    def start(self):
        self.players = []
        self.time_left = 15
        self.time_til_bomb = -1
        self.ct_rounds = 0
        self.t_rounds = 0
        self.bomb_location = None
        if self.player_is_terrorist:
            self.players.append(Player(Terrorist))
            self.players.append(NPC(CounterTerrorist))
        else:
            self.players.append(Player(CounterTerrorist))
            self.players.append(NPC(Terrorist))

        for i in range(1, 5):
            self.players.append(NPC(CounterTerrorist))
            self.players.append(NPC(Terrorist))
        t_with_bomb = randint(1, 5)
        t_index = 0
        for player in self.players:
            if player.side != Terrorist:
                continue
            t_index += 1
            if t_index == t_with_bomb:
                player.give_bomb()

    def side_winning_round(self, no_print=False):
        ct_players = []
        t_players = []
        for player in self.players:
            if player.side == CounterTerrorist:
                ct_players.append(player)
            else:
                t_players.append(player)
        if len(ct_players) == 0:
            if not no_print:
                print("Terrorists eliminated Counter Terrorists")
            # CT eliminated in time
            return Terrorist
        if len(t_players) == 0 and \
            self.time_til_bomb == -1:
            if not no_print:
                print("Counter terrorists eliminated Terrorists.")
            # Bomb was never set and T eliminated
            return CounterTerrorist
        if self.time_til_bomb == 99:
            # Bomb was defused
            if not no_print:
                print("Bomb was defused.")
            return CounterTerrorist
        if self.time_til_bomb == 0:
            # Bomb exploded
            if not no_print:
                print("Bomb detonated.")
            return Terrorist
        if self.time_left == 0 and \
            self.time_til_bomb -1:
            if not no_print:
                print("Time up.")
            # Bomb not set, time up
            return CounterTerrorist
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
                    info = RoundInfo(player, self.time_til_bomb, self.players, self.time_left, self.bomb_location)
                    action = player.get_action(info)
                    if isinstance(action, Wait):
                        pass
                    if isinstance(action, Move):
                        player.set_next_move(action.option)
                    if isinstance(action, Plant):
                        if (player.location == ASite or player.location == BSite) \
                                and player.has_bomb:
                            print("The bomb has been planted.")
                            self.time_til_bomb = 7
                            self.time_left += 7
                            self.bomb_location = player.location()
                            player.has_bomb = False
                    if isinstance(action, Defuse):
                        if player.location().location_name() == self.bomb_location.location_name():
                            self.bomb_location = None
                            self.time_til_bomb = 99
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
                                        player_label = "{} side".format(player.side.str())
                                        if isinstance(player, Player):
                                            player_label = "You"
                                        target_label = "{} player".format(target.side.str())
                                        if isinstance(target, Player):
                                            target_label = "you"

                                        print("{} killed {}.".format(
                                            player_label,
                                            target_label
                                        ))
                                        players_died_this_round.append(target)
                                        if isinstance(target, Player):
                                            print("You got pwned.")
                                    elif isinstance(player, Player):
                                        print("You hit an enemy.")
                for dead_player in players_died_this_round:
                    if dead_player.has_bomb:
                        bomb_dropped_at = dead_player.location().__class__
                        for player in self.players:
                            if player.side == dead_player.side \
                                and player.is_alive() \
                                    and player.location().__class__ == bomb_dropped_at:
                                player.give_bomb()
                                break
                    self.players.remove(dead_player)
                for player in self.players:
                    player.do_move()

                if self.side_winning_round():
                    print("{} win round!".format(
                        self.side_winning_round(no_print=True).str()
                    ))
                    print("")
                    break
                self.time_left -= 1
                if 0 < self.time_til_bomb < 10:
                    self.time_til_bomb -= 1
            if self.side_winning_round(no_print=True) == Terrorist:
                self.t_rounds += 1
            else:
                self.ct_rounds += 1
        if self.ct_rounds > self.t_rounds:
            print("Counter terrorists win the game!")
        else:
            print("Terrorists win the game!")
