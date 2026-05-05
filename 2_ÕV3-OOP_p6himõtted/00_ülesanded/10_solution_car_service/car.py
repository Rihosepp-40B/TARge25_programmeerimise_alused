"""Car to be inserted into service."""

class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Car class constructor.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size

    def is_priority_repair(self):
        """Return true if color + make characters length is exactly 13"""
        return len(self.color) + len(self.make) == 13

    def __eq__(self, other):
        """Override how two objects are compared"""
        if isinstance(other, Car):
            return self.make == other.make and self.color == other.color
        return False
