"""Student class with student name and grades."""


class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        self.__name = name
        self.__id = 0

    def set_id(self, id: int):
        pass

    def get_grades(self) -> list[tuple[Course, int]]:
        pass

    def get_id(self) -> int:
        return self.__id

    def get_average_grade(self):
        pass

    def __repr__(self) -> str:
        pass