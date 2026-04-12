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


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if len(self.animals) >= self.max_number_of_animals:
            return False
        if animal in self.animals:
            return False
        if any(a.name == animal.name and a.species == animal.species for a in self.animals):  # __eq__ asemel any, sest
            # eq võrdleb sisu järgi kas on tegu sama objektiga. Any võrdleb kas sama sisu on olemas.
            return False
        return True

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        return animal in self.animals

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal):
            self.animals.remove(animal)

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda animal: animal.age)

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.animals, key=lambda animal: animal.name)


if __name__ == '__main__':
    zoo1 = Zoo("Zoo1", 4)
    animal1 = Animal("Ahv", "Ahv", 12)
    animal2 = Animal("Pärdik", "Pärdik", 4)
    animal3 = Animal("Baboon", "Ahv", 8)
    print(animal1.name)

    print(zoo1.max_number_of_animals)
    print(zoo1.get_all_animals())
    print(zoo1.get_animals_by_age())
    print(zoo1.get_animals_sorted_alphabetically())

    zoo1.add_animal(animal1)
    zoo1.add_animal(animal2)
    zoo1.add_animal(animal3)
    print(zoo1.get_all_animals())
    print(zoo1.get_animals_by_age())
    print(zoo1.get_animals_sorted_alphabetically())
    animal4 = Animal("Baboon", "Ahv", 5)
    zoo1.add_animal(animal4)
    print(zoo1.get_all_animals())
    print(zoo1.get_animals_by_age())
    print(zoo1.get_animals_sorted_alphabetically())