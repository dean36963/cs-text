"""Information filtered to a specific person"""
from Locations import location_from_locationname


class RoundInfo:
    def __init__(self,
                 player,
                 turns_til_explosion,
                 players,
                 turns_left):
        self._player = player
        self.turns_til_explosion = turns_til_explosion
        self._players = players
        self.turns_left = turns_left

    def team_mates(self):
        teammates = []
        for player in self._players:
            if player == self._player:
                continue
            if player.side != self._player.side:
                continue
            teammates.append(player)
        return teammates

    def num_enemy(self):
        num_enemy = 0
        for player in self._players:
            if player.side != self._player.side:
                num_enemy += 1
        return num_enemy

    def enemies_in_sight(self):
        seen_enemies_by_location = {}
        visible_locations = []
        for location_name in self._player.location.next_to():
            visible_locations.append(location_from_locationname(location_name))
        visible_locations.append(self._player.location)
        for player in self._players:
            if player.side == self._player.side:
                continue
            if player.location in visible_locations:
                if player.location in seen_enemies_by_location:
                    enemies = seen_enemies_by_location[player.location]
                    enemies.append(player)
                    seen_enemies_by_location[player.location] = enemies
                else:
                    seen_enemies_by_location[player.location] = [player]
        return seen_enemies_by_location