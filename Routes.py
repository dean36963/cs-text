from Route import Route
from Locations import *


class TSpawnToAViaLong(Route):
    @staticmethod
    def locations():
        return [
            TerroristSpawn,
            LongDoubleDoors,
            ALong,
            ASite
        ]


class TSpawnToAViaShort(Route):
    @staticmethod
    def locations():
        return [
            TerroristSpawn,
            TMid,
            Catwalk,
            AShort,
            ASite
        ]


class TSpawnToBViaTunnels(Route):
    @staticmethod
    def locations():
        return [
            TerroristSpawn,
            TerroristSideTunnels,
            UpperTunnels,
            BSite
        ]

class CTSpawnToA(Route):
    @staticmethod
    def locations():
        return [
            CTSpawn,
            ASite
        ]

class CTSpawnToB(Route):
    @staticmethod
    def locations():
        return [
            CTSpawn,
            CTMid,
            BDoor,
            BSite
        ]

class AToB(Route):
    @staticmethod
    def locations():
        return [
            ASite,
            CTSpawn,
            CTMid,
            BWindow,
            BSite
        ]

class BToA(Route):
    @staticmethod
    def locations():
        return [
            BSite,
            BDoor,
            CTMid,
            CTSpawn,
            ASite
        ]

def get_t_route_from_first_move(location):
    if location == TerroristSideTunnels:
        return TSpawnToBViaTunnels()
    if location == TMid:
        return TSpawnToAViaShort()
    if location == LongDoubleDoors:
        return TSpawnToAViaLong()