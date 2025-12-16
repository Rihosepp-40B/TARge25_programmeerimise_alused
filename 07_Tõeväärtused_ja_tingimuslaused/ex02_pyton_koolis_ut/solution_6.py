"""Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige) kordajad ning arvutab
nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandi lahendid. Nagu tead, võib lahendeid vastavalt
diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa."""
import math


def calculate_discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_quadrantic_equation(a, b, discriminant, useAddition):
    if useAddition:
        top = -b + math.sqrt(discriminant)
    else:
        top = -b - math.sqrt(discriminant)
    bottom = 2 * a
    return top / bottom


if __name__ == '__main__':
    print("Arvutame ruutvõrrandit!")
    a = float(input("Sisesta ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null.")
    else:
        b = float(input("Sisesta lineaarliige: "))
        c = float(input("Sisesta vabaliige: "))
        discriminant = calculate_discriminant(a, b, c)
        if discriminant < 0:
            print("Lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadrantic_equation(a, b, discriminant, True)
            print(f"Lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadrantic_equation(a, b, discriminant, True)
            solution2 = solve_quadrantic_equation(a, b, discriminant, False)
            print(f"Lahendid on kaks: {solution1} ka {solution2}")