from Location import Location
import LocationNames


class TerroristSpawn(Location):
    @staticmethod
    def location_name():
        return LocationNames.TerroristSpawn

    @staticmethod
    def next_to():
        return [
            LocationNames.LongDoubleDoors,
            LocationNames.TerroristSideTunnels,
            LocationNames.TMid
        ]


class TerroristSideTunnels(Location):
    @staticmethod
    def location_name():
        return LocationNames.TerroristSideTunnels

    @staticmethod
    def next_to():
        return [
            LocationNames.TerroristSpawn,
            LocationNames.UpperTunnels
        ]


class UpperTunnels(Location):
    @staticmethod
    def location_name():
        return LocationNames.UpperTunnels

    @staticmethod
    def next_to():
        return [
            LocationNames.TerroristSideTunnels,
            LocationNames.LowerTunnels,
            LocationNames.BSite
        ]


class LowerTunnels(Location):
    @staticmethod
    def location_name():
        return LocationNames.LowerTunnels

    @staticmethod
    def next_to():
        return [
            LocationNames.UpperTunnels,
            LocationNames.LowerMid
        ]


class BSite(Location):
    @staticmethod
    def location_name():
        return LocationNames.BSite

    @staticmethod
    def next_to():
        return [
            LocationNames.UpperTunnels,
            LocationNames.BWindow,
            LocationNames.BDoor
        ]


class BDoor(Location):

    @staticmethod
    def location_name():
        return LocationNames.BDoor

    @staticmethod
    def next_to():
        return [
            LocationNames.CTMid,
            LocationNames.BSite
        ]


class BWindow(Location):
    @staticmethod
    def location_name():
        return LocationNames.BWindow

    @staticmethod
    def next_to():
        return [
            LocationNames.CTMid,
            LocationNames.BSite
        ]


class CTMid(Location):
    @staticmethod
    def location_name():
        return LocationNames.CTMid

    @staticmethod
    def next_to():
        return [
            LocationNames.LowerMid,
            LocationNames.BWindow,
            LocationNames.BDoor,
            LocationNames.CTSpawn
        ]


class CTSpawn(Location):
    @staticmethod
    def location_name():
        return LocationNames.CTSpawn

    @staticmethod
    def next_to():
        return [
            LocationNames.CTMid,
            LocationNames.ASite
        ]


class ASite(Location):
    @staticmethod
    def location_name():
        return LocationNames.ASite

    @staticmethod
    def next_to():
        return [
            LocationNames.AShort,
            LocationNames.CTSpawn,
            LocationNames.ALong
        ]


class AShort(Location):
    @staticmethod
    def location_name():
        return LocationNames.AShort

    @staticmethod
    def next_to():
        return [
            LocationNames.CTSpawn,
            LocationNames.Catwalk,
            LocationNames.ASite
        ]


class ALong(Location):
    @staticmethod
    def location_name():
        return LocationNames.ALong

    @staticmethod
    def next_to():
        return [
            LocationNames.ASite,
            LocationNames.Pit,
            LocationNames.LongDoubleDoors
        ]


class Pit(Location):
    @staticmethod
    def location_name():
        return LocationNames.Pit

    @staticmethod
    def next_to():
        return [
            LocationNames.LongDoubleDoors,
            LocationNames.ALong
        ]


class LongDoubleDoors(Location):
    @staticmethod
    def location_name():
        return LocationNames.LongDoubleDoors

    @staticmethod
    def next_to():
        return [
            LocationNames.Pit,
            LocationNames.ALong,
            LocationNames.TMid,
            LocationNames.TerroristSpawn
        ]


class TMid(Location):
    @staticmethod
    def location_name():
        return LocationNames.TMid

    @staticmethod
    def next_to():
        return [
            LocationNames.TerroristSpawn,
            LocationNames.LongDoubleDoors,
            LocationNames.Catwalk,
            LocationNames.LowerMid
        ]


class Catwalk(Location):
    @staticmethod
    def location_name():
        return LocationNames.Catwalk

    @staticmethod
    def next_to():
        return [
            LocationNames.AShort,
            LocationNames.LowerMid,
            LocationNames.TMid
        ]


class LowerMid(Location):
    @staticmethod
    def location_name():
        return LocationNames.LowerMid

    @staticmethod
    def next_to():
        return [
            LocationNames.CTMid,
            LocationNames.LowerTunnels,
            LocationNames.Catwalk,
            LocationNames.TMid
        ]


def all_locations():
    return [
        TerroristSpawn,
        TerroristSideTunnels,
        UpperTunnels,
        LowerTunnels,
        BSite,
        BDoor,
        BWindow,
        CTMid,
        CTSpawn,
        ASite,
        AShort,
        ALong,
        Pit,
        LongDoubleDoors,
        TMid,
        Catwalk,
        LowerMid
    ]


def location_from_locationname(name):
    for location in all_locations():
        if location.location_name() == name:
            return location
