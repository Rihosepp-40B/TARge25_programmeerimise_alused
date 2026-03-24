"""Ülesanne 3
Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon)."""
from unittest import result

from pyexpat.errors import messages

from solution_2 import create_poem_file # , poem_rows_as_list

# see siis import'iga listiga
# def get_poem_row(poem_list:list) -> str:
#     row_nr = int(input(f"Luuletuses on {len(poem_list)} rida, millist soovid näha? "))
#     print(f"{poem_list[row_nr-1]}")

# for tsükklis käivitub else, siis kui tsükkel saab tehtud.

def print_line_from_file(linenumber: int, filename: str) -> None:
    message = f"Luuletuse {linenumber}. rida: "
    with open(filename, "r", encoding="UTF-8") as f:
        for index, line in enumerate(f):
            if(index + 1) == linenumber:
                print(message + line)
                break
            else:
                print("Viga! Sisesta nullist suurem täisarv")


if __name__ == '__main__':
    filename = "luuletused.txt"
    create_poem_file(filename)
    # poem_list = poem_rows_as_list(filename)
    # get_poem_row(poem_list)

    # siit ilma listita
    user_input = input("Mitmendat luuletuse rida soovid näha? ")
    if user_input.isdigit() and int(user_input) > 0:
        print_line_from_file(int(user_input), filename)
    else:
        print("Viga! Sisesta täisarv")