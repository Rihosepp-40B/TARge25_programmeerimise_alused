"""Zoo."""


class Animal:
    """Animal class."""

    def __init__(self, name: str, species: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param species: animal specie
        """
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self):
        """Return animal data."""
        return f"({self.name}, {self.species}, {self.age})"