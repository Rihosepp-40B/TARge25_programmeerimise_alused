"""School class which stores information about courses and students."""


from student import Student
from course import Course


class School:
    """School class, do not change."""

    def __init__(self, name):
        self.__student = []
        self.__course = []
        self.__name = name

    def add_course(self, course: Course):
        pass

    def add_student(self, student: Student):
        pass

    def add_student_grade(self, student: Student, course: Course, grade: int):
        pass

    def get_students(self) -> list[Student]:
        return self.__student

    def get_courses(self) -> list[Course]:
        return self.__course

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        pass