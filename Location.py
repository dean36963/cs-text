
class LocationName:
    @staticmethod
    def name():
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")


class Location:
    @staticmethod
    def next_to(self):
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    @staticmethod
    def location_name(self):
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")
