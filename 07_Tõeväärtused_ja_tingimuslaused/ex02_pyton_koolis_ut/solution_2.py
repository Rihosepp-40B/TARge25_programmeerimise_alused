"""Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile
nimelise tervituse koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega."""


def greet_by_name(name: str) -> str:
    return f"Tervist {name}!"


def verify_age(age: int) -> str:
    if 7 <= age <= 18:
        return "Oled 7-18 aastat vana"
    return "Sa ei ole 7-18 aastat vana"


if __name__ == '__main__':
    name = input("Tere, mis on sinu nimi? ")
    age = int(input("Kui vana sa oled? "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")