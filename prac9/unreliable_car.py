import random
from car import Car

class UnreliableCar(Car):
    """A Car that may not drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, based on Car, with reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0  # Failed to drive