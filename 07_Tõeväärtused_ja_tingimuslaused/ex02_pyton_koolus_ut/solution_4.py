"""Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti
ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse
"haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel õppinud.

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh"""


def calculate_dog(num1: float, num2: float, operation: str) -> str:
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
        return f"URRRRR GRRRR"
    return f"{round(result)*"auh "}"


if __name__ == '__main__':
    num1 = float(input("Sisesta number millest tahad teist numbrit arvutada: "))
    num2 = float(input("Sisesta number millega tahad esimesest kalkuleerida: "))
    operation = input("Sisesta tehte märk: ")
    print(f"Tulemus: {calculate_dog(num1, num2, operation)}")