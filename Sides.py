class Side:
    pass


class Terrorist(Side):
    @staticmethod
    def str():
        return "Terrorist"


class CounterTerrorist(Side):
    @staticmethod
    def str():
        return "Counter Terrorist"
