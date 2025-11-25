"""Function examples."""


def func():
    """Print "I´m inside the function"."""
    print("I´m inside the function")


def my_name_is(name: str):
    """Print "My name is {name}"."""
    print(f"My name is {name}")


def sum_six(num: int):
    """Return sum of 6 and [num]."""
    return 6 + num


def sum_numbers(a: int, b: int):
    """Return sum of a and b."""
    return a + b


def usd_to_eur(usd: int):
    """Return US dollars in euros."""
    eur = 0.8
    return usd * eur


if __name__ == '__main__':
    func()
    my_name_is("Riho")
    print(sum_six(2))
    print(sum_numbers(1, 2))
    print(usd_to_eur(100))