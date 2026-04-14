"""Zoo."""


from animal import Animal
from zoo import Zoo


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