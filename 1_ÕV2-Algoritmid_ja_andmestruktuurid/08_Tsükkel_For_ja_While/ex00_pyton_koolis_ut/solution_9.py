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


def get_multiplayer_info() -> list:
    players = []
    how_many_players = input("Mitu mängijat mängib? ")
    players_playing = 0
    if not how_many_players.isdigit():
        players_playing += 1
    else:
        players_playing += int(how_many_players)
    if players_playing > 1:
        for i in range(players_playing):
            players += [input(f"Mängija {i + 1}. Sisesta enda nimi: ")]
    else:
        players += ["Nimetu"]
    return players


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
    players = get_multiplayer_info()
    number_of_throws = int(input("Mitu korda täringut viskame? "))
    players_results = []
    for i, player in enumerate(players):
        count = 0
        player_result_sum = 0
        while count < number_of_throws:
            throw_result = get_dice_throw_result()
            display_graphics(throw_result)
            player_result_sum += throw_result
            count += 1
        print(f"Mängija {i + 1}. {player} sinu visete summa kokku on {player_result_sum}")
        players_results.append(player_result_sum)


if __name__ == '__main__':
    throw_dice()


    """print("     ────────────")
    print("   /   ()  ()   /│")
    print("  /     ()     / │")
    print(" /   ()  ()   /  │")
    print("┌────────────┐   │")
    print("│            │  /")
    print("│            │ /")
    print("│            │/")
    print("└────────────┘")"""