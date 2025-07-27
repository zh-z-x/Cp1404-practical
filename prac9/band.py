class Band:
    """Band class holding a list of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician object to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Call play() on each musician and return their combined result as string."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)


if __name__ == "__main__":
    from musician import Musician
    from guitar import Guitar

    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add(nuno)
    band.add(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add(kevin)

    print(band)
    print(band.play())
