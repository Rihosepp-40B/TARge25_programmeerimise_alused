"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Construct person with firstname, lastname and age."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Construct student with firstname, lastname and age."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    empty = Empty()

    p1 = Person()
    p1.firstname = "Aadu"
    p1.lastname = "Aavik"
    p1.age = 18

    p2 = Person()
    p2.firstname = "Taadu"
    p2.lastname = "Taavik"
    p2.age = 25

    p2 = Person()
    p2.firstname = "Peedu"
    p2.lastname = "Paadik"
    p2.age = 35

    s1 = Student("Aadu", "Aavik", 18)
    s2 = Student("Peedu", "Peedik", 22)
    s3 = Student("Teedu", "Taadik", 60)