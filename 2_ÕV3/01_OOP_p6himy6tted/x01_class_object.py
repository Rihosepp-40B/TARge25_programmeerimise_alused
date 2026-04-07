"""Simple class."""


class Student:
    """Student name and has he finished."""

    def __init__(self, name, finished=False):
        """Return name and finished."""
        self.name = name
        self.finished = finished


student = Student("John")
print(student.name)  # John
print(student.finished)  # False
