"""All the possible things characters can do, with what the player should type"""
from Locations import location_from_locationname


class Action:
    def __init__(self, option, player):
        valid_options = self.options(player)
        if valid_options and option not in valid_options:
            raise Exception("Invalid option for this action")
        self.option = option

    def option(self):
        return self.option

    @staticmethod
    def aliases():
        raise NotImplementedError("Implement this")

    @staticmethod
    def options(player):
        raise NotImplementedError("Implement this")

    @staticmethod
    @property
    def option_prompt():
        raise NotImplementedError("Implement this")


class Wait(Action):
    @staticmethod
    def aliases():
        return [
            "wait",
            "camp",
            "overwatch"
        ]

    @staticmethod
    def options(player):
        return []

    @staticmethod
    def option_prompt():
        return ""


class Move(Action):
    @staticmethod
    def aliases():
        return [
            "move",
            "go",
            "walk",
            "run"
        ]

    @staticmethod
    def options(player):
        options = []
        for location in player.location.next_to():
            options.append(location_from_locationname(location))
        return options

    @staticmethod
    def option_prompt():
        return "Where do you want to move?"


class Shoot(Action):
    @staticmethod
    def aliases():
        return [
            "shoot",
            "fire"
        ]

    @staticmethod
    def options(player):
        options = []
        for location in player.location.next_to():
            options.append(location_from_locationname(location))
        return options

    @staticmethod
    def option_prompt():
        return "Where do you want to shoot?"


class Defuse(Action):
    @staticmethod
    def aliases():
        return [
            "diffuse",
            "disarm"
        ]

    @staticmethod
    def options(player):
        return []

    @staticmethod
    def option_prompt():
        return ""


def all_actions():
    return [
        Move,
        Wait,
        Shoot,
        Defuse
    ]


def action_from_alias(alias):
    for action in all_actions():
        if alias in action.aliases():
            return action
