import math

def solve_quadratic_equation(a, b, c):
    """
    Solving quadratic equation
    ax^2 + bx + c = 0
    :param a: ax^2
    :param b: bx
    :param c: c
    :return: (x1, x2) tuple
    """
    disc = b**2 - 4 * a * c
    if disc == 0:
        return -b / (2 * a),
    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)
    return x1, x2