"""Ülesanne 1
Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale,
perekonna- ja eesnimi tühikuga eraldatult). Koosta programm, mis loeb failist andmed ja väljastab need
ekraanile tähestikulises järjekorras. Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi
(järjestamist). Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili tuttavad1.txt."""


def write_to_file(filename: str, values: list[str]):
    with open(filename, "w", encoding="utf-8") as f:
        for name in sorted_by_last_name:
            f.write(name + "\n")


def create_familiars_file(filename: str):
    """Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale,
    perekonna- ja eesnimi tühikuga eraldatult)."""
    familiars = [
        "Aadu Pirukas",
        "Eeva Mänd",
        "",
        "Sander Liiv",
        "Kaarel Kala",
        "Ken Põder",
        "Stiina Tamm"
    ]
    with open(filename, "w", encoding="utf-8") as f:  # see teeb iga rea lõppu rea vahetuse minul oli for tsükkel koos if'ga (Solution.py "write_lines_to_file"
        for line in familiars:
            f.write(line + "\n")


def get_names_from_file(filename: str) -> list:
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if len(name) > 0:
                result.append(name)
    return result


def sort_names(names: list[str]) -> list[str]:
    last_name__full_name_list = []  #[(name.split()[-1], name) for name in names: <- sellega võib asendada all kuni sorteeri
    for name in names:
        # võta nimest välja perekonna nimi (viimane)
        last_name = name.split()[-1]
        last_name__full_name_list += [(last_name, name)]
    # sorteeri
    sorted_names = sorted(last_name__full_name_list)
    # tagasta
    result = []
    for name in sorted_names:
        result_name = name[-1]
        result.append(result_name)
    return result
    return [item[-1] for item in sorted_names]


if __name__ == '__main__':
    filename = "tuttavad.txt"
    create_familiars_file(filename)
    names_from_file = get_names_from_file(filename)
    sorted_by_last_name = sort_names(names_from_file)
    for name in sorted_by_last_name:
        print(name)
    write_to_file("tuttavad1.txt", sorted_by_last_name)
