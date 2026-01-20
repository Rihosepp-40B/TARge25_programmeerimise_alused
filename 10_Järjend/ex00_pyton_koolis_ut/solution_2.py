"""Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

1 Väljasta linnad eraldi ridadena.
2 Järjesta need tähestikulisse järjekorda.
3 Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
4 Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni
abil."""


euro_capitols = ["Tallinn", "Helsinki", "Stockholm", "Kopenhaagen","Riia",
                 "Berliin", "Pariis", "Vilnius", "Rooma", "Oslo"]


def print_list(elements: list) -> None:
    for element in elements:
        print(element, end=", ")
    print()


def sort_in_place(elements: list) -> None:
    elements.sort()


def add_capitols(euro_capitols: list[str], amount: str) -> None:
    for i in range(amount):
        euro_capitols.append(input(f"{i + 1}. Sisesta euroopa pealinn: "))


def print_list_numbered(elements: list):
    for i, element in enumerate(elements):
        print(f"{i + 1}. {element}")


def summarize(euro_capitols: list[str]):
    print(f"Meie järjendis on {len(euro_capitols)} Euroopa pealinna, kus linnade arv leitakse vastava funktsiooni abil.")


if __name__ == "__main__":
    print_list(euro_capitols)
    sort_in_place(euro_capitols)
    print_list(euro_capitols)
    add_capitols(euro_capitols, 2)
    sort_in_place(euro_capitols)
    print_list(euro_capitols)
    print_list_numbered(euro_capitols)
    summarize(euro_capitols)