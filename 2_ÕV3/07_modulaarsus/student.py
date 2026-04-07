"""Student class with student name and grades."""

from typing import List, Tuple
from course import Course

class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        self.name = name
        self.__id: int | None = None
        self.__grades: List[Tuple['Course', int]] = []

    def set_id(self, id: int):
        if self.__id is None:
            self.__id = id

    def get_grades(self) -> List[Tuple['Course', int]]:
        return self.__grades[:]

    def get_id(self) -> int:
        return self.__id

    def get_average_grade(self):
        if not self.__grades:
            return -1.0
        total = sum(grade for _, grade in self.__grades)
        return total / len(self.__grades)

    def __repr__(self) -> str:
        return self.name