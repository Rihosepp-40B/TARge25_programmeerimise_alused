"""Show highest grade."""


def show_highest_grade(grade1: int, grade2: int) -> None:
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"
    1, 2 => "Highest grade: 1"
    """
    print(f"Highest grade: {max(grade1, grade2)}")


if __name__ == '__main__':
    show_highest_grade(3, 2)