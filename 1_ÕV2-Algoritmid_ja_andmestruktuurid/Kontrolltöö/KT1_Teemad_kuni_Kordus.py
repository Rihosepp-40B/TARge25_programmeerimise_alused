"""Kt 3.
1.       Küsi kasutaja vanust ja nime
2.       Tervita kasutajat nime pidi niimitu korda kui mitu aastat ta on täisealine olnud (Kordus)
3.       Kirjuta ekraanile nime lõpust 3 tähte."""


def ask_user_info() -> tuple[str, int]:
    """Küsi kasutajalt nime ja vanust. Väljasta nimi ja vanus
        name: isiku nimi
        age: isiku vanus
        return: väljasta nimi ja vanus"""
    name = input("Mis on sinu nimi? ")
    age = int(input("Mis on sinu vanus? "))
    return name, age


def greet_user_for_each_legal_year() -> None:
    """Võta sisend nimi ja vanus. Kalkuleeri mitu aastat on isik olnud täisealine. Iga täisea aasta kohta kuva
    ekraanile nimelne tervitus. Funktsiooni lõpus kuva ekraanile nime kolm viimast tähte
        name, age: sisendfunktsioon
        years_legal: vanus - miinimum täisiga
        greetings_count: läbitud korduste arv (algab 0)
        while korduste arv on väiksem kui täisealine oldud aastad
            print: Tere nimi
            greetings_count: korduse lisamine
        print: väljasta nime kolm viimast tähte
    """
    name, age = ask_user_info()
    years_legal = age - 18
    greetings_count = 0
    while greetings_count < years_legal:
        print(f"Tere {name}!")
        greetings_count += 1
    print(name[-3:])


if __name__ == "__main__":
    greet_user_for_each_legal_year()