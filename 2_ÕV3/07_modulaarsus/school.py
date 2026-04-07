"""School class which stores information about courses and students."""

from typing import List
from student import Student
from course import Course


class School:
    """School class, do not change."""

    def __init__(self, name):
        self.__students: List[Student] = []
        self.__courses: List[Course] = []
        self.__name = name

    def add_course(self, course: Course):
        self.__courses.append(course)

    def add_student(self, student: Student):
        self.__students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        if student in self.__students and course in self.__courses:
            pass

    def get_students(self) -> list[Student]:
        return self.__students[:]

    def get_courses(self) -> list[Course]:
        return self.__courses[:]

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        return sorted(self.__students, key=lambda student: student.average_grade)