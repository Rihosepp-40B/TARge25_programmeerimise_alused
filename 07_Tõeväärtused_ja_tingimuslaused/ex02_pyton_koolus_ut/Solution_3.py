"""Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse
tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5"""


def calculate(num1: float, num2: float, operation: str) -> str:
    if  operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "**":
        result = num1 ** num2
    else:
        return f"Tundmatu tehe {operation}"
    return f"{num1}{operation}{num2}={result}"


if __name__ == '__main__':
    num1 = float(input("Sisesta number millest tahad teist numbrit arvutada: "))
    num2 = float(input("Sisesta number millega tahad esimesest kalkuleerida: "))
    operation = input("Sisesta tehte märk: ")
    print(f"Tulemus: {calculate(num1, num2, operation)}")