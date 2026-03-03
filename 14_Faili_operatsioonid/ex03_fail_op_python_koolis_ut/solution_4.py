"""Ülesanne 4
Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt uut rida lisada ning seejärel
lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""


from solution_2 import create_poem_file, poem_rows_as_list


def add_new_line(poem_as_list: list[str]) -> None:
    poem_line = input("Sisesta rida, mille järgi soovid uut rida lisada: ")
    if poem_line in poem_as_list:
        row = poem_as_list.index(poem_line)
        line_to_append = input("Sisesta rida, mida soovid luuletusse lisada: ")
        return poem_as_list.insert(row + 1, line_to_append)
    else:
        print("Soovitud rida ei leitud!")


def rewrite_poem_file(filename: str, lines: list[str]) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        row = 0
        for line in lines:
            if row == 0:
                f.writelines(line)
                row += 1
            else:
                f.writelines(f"\n{line}")


if __name__ == '__main__':
    filename = "luuletused.txt"
    create_poem_file(filename)
    poem_as_list = poem_rows_as_list(filename)
    add_new_line(poem_as_list)
    rewrite_poem_file(filename, poem_as_list)