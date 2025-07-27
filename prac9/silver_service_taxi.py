from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with fanciness and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi, set fanciness and adjust price_per_km."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate fare including flagfall charge."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return string including flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
