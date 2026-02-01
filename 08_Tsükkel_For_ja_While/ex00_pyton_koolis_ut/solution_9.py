"""Ülesanne 9
Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku täringuviske tulemused. Et
ekraanipilt oleks realistlikum, esita tulemused graafiliselt, selleks kasuta nn. ASCII graafikat
(https://en.wikipedia.org/wiki/ASCII_art): imiteeri tekstisümbolite abil täringu külje kujutist. Täiendamiseks:

Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena."""

import random

def get_dice_throw_result():
    return random.randint(1,6)


def display_graphics(throw: int) -> None:
    top_row, bottom_row, double_eye_row, middle_single_row, top_single_row, bottom_single_row, empty_row =get_dice_2d_graphics()
    if throw % 2 == 1:
        middle = middle_single_row
    elif throw == 6:
        middle = double_eye_row
    else:
        middle = empty_row
    if throw > 3:
        top = double_eye_row
        bottom = double_eye_row
    elif throw > 1:
        top = top_single_row
        bottom = bottom_single_row
    else:
        top = empty_row
        bottom = empty_row
    print(f"{top_row}\n{top}\n{middle}\n{bottom}\n{bottom_row}")


def get_dice_2d_graphics() -> tuple:
    top_row = "┌──────────┐"
    bottom_row ="└──────────┘"
    double_eye_row = "│  ()  ()  │"
    middle_single_row = "│    ()    │"
    top_single_row = "│  ()      │"
    bottom_single_row = "│      ()  │"
    empty_row = "│          │"
    return top_row, bottom_row, double_eye_row, middle_single_row, top_single_row, bottom_single_row, empty_row


def throw_dice():
    number_of_throws = int(input("Mitu korda täringut viskame? "))
    count = 0
    while count < number_of_throws:
        throw_result = get_dice_throw_result()
        display_graphics(throw_result)
        count += 1


if __name__ == '__main__':
    print("     ────────────")
    print("   /   ()  ()   /│")
    print("  /     ()     / │")
    print(" /   ()  ()   /  │")
    print("┌────────────┐   │")
    print("│            │  /")
    print("│            │ /")
    print("│            │/")
    print("└────────────┘")