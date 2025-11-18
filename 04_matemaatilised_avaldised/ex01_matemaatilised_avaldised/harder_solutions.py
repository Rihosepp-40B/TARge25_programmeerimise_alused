"""Math exercises vol2."""
import math


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers


if __name__ == '__main__':
    time_converter_result = time_converter(3661)
    assert time_converter_result == "3661 sekundit on 1 tund(i) ja 1 minut(it)."

    student_helper_result = student_helper(30)
    assert student_helper_result == "Nurk: 30, siinus: 0.5, koosinus: 0.9."

    hey_result = greetings(4)
    assert hey_result == "HeyHeyHeyHey"

    numbers_result = adding_numbers(1, 2)
    print(numbers_result)
    assert numbers_result == "12"