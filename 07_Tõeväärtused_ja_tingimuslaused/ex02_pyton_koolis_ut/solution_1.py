"""Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning
väljastab ekraanile ristküliku ümbermõõdu ja pindala."""


def calculate_rectangle():
    length = float(input("Sisesta ristküüliku pikkus: "))
    width = float(input("Sisesta ristküüliku laius: "))
    area = width * length
    circumference = 2 * (length + width)
    print(f"Antud risküüliku pindala on {area}")
    print(f"Antud risküüliku ümbermõõt on {circumference}")

if __name__ == '__main__':
    calculate_rectangle()