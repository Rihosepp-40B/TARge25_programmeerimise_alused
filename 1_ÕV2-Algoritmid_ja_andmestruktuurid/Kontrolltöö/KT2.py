"""Koosta programm telefoniraamatu loomiseks.

1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""


import csv

filename = ""
contact_dict = {}
cancel_write = "Viimase kontakti sisestamine katkestatud: Sisestati tühjus!"


def find_data_in_phonebook(filename: str) -> None:
    """Küsi kasutajalt sisendit ning otsi kasutusel olevast failist. Kuva
    ekraanile väärtus koos paarilisega."""
    find = input("Sisesta nimi või number mida soovid otsida: ").lower().capitalize()
    data = read_phonebook(filename)
    reverse_data = reverse_dict(data)
    if check_value(data, find)[0] or check_value(data, find)[1] is True:
        try:
            print(f"'{find}' telefoninumber on '{data[find]}'")
            input("Jätkamiseks vajuta ENTER")
        except KeyError:
            print(f"'{find}' telefoninumbri omanik on '{reverse_data[find]}'")
            input("Jätkamiseks vajuta ENTER")
        finally:
            main_menu()
    else:
        not_found_add(filename, find)


def not_found_add(filename: str, find: str) -> None:
    """Otsitava väärtuse mitte leidmisel failist, küsi kas kasutaja tahab
    lisada uut kontakti faili."""
    print(f"Otsitavat väärtust '{find}' ei ole failis '{filename}'")
    if input(f"Kas soovid '{find}' lisada kontaktiks? (y/ ) ").lower() == "y":
        expand_phonebook(filename)
    else:
        main_menu()


def ask_name_logic(contact_dict: dict) -> str:
    """Küsi kasutajalt isiku nime sisendit. Võrdle sisendit failis olevate
    andmetega. Korduvate andmete korral küsi kas kasutaja tahab vahetada välja
    failis olevaid andmeid. Tagasta isiku nimi.
    """
    no_name = ""
    name = input("Sisesta nimi: ")
    if name == no_name:
        print(cancel_write)
        name = no_name
    if check_value(contact_dict, name)[0] is True:
        print("See nimi on juba telefoniraamatus!")
        if input(f"Kas soovid '{name}' andmed välja vahetada? (y/ ) ").lower() != "y":
            if input("Kas soovid sisestada uut isikut? (y/ )").lower() != "y":
                return no_name
            name = ask_name_logic(contact_dict)
        name = name
    return name


def ask_nr_logic(contact_dict: dict, name: str) -> str:
    """Küsi kasutajalt sisestatud isiku telefoninumbrit. Võrdle sisendit
    failis olevaga Korduva telefoni numbri korral, kuva ekraanile teada, et
    number on kasutusel.
    Tagasta isikuga seotud telefoni number"""
    no_nr = ""
    phone_nr = input(f"Sisesta {name} telefoninumber: ")
    if phone_nr == "":
        print(cancel_write)
        return no_nr
    if check_value(contact_dict, phone_nr)[1] is True:
        print("See number on juba telefoniraamatus!")
        return no_nr
    return phone_nr


def expand_phonebook(filename: str) -> None:
    """Kontrolli, et ei oleks korduvaid sisendeid ja tühje sisendeid.
    Laienda failis olevat telefoniraamatud loodud sõnastiku jagu.
    """
    contact_dict = read_phonebook(filename)
    contact_dict_expand = {}
    while True:
        name = ask_name_logic(contact_dict)
        if name == "":
            break
        phone_nr = ask_nr_logic(contact_dict, name)
        if phone_nr == "":
            break
        contact_dict[name] = phone_nr
        contact_dict_expand[name] = phone_nr
    add_to_phonebook(filename, contact_dict_expand)
    main_menu()


def create_phonebook(filename: str) -> None:
    """Kontrolli, et ei oleks korduvaid sisendeid ja tühje sisendeid.
    Loo uus telefoniraamat"""
    write_phonebook(filename)
    while True:
        name = ask_name_logic(contact_dict)
        if name == "":
            break
        phone_nr = ask_nr_logic(contact_dict, name)
        if phone_nr == "":
            break
        contact_dict[name] = phone_nr
    add_to_phonebook(filename, contact_dict)
    main_menu()


def write_phonebook(filename: str) -> None:
    """Kirjuta ülekirjutatud ja alles loodud faili päis."""
    with open(filename, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow(("Name", "Phone_nr"))


def add_to_phonebook(filename: str, contact_dict: dict) -> None:
    """Lisa failile uus rida sõnastikust"""
    with open(filename, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",")
        for name, phone_nr in contact_dict.items():
            csv_writer.writerow([name.lower().capitalize(), phone_nr])


def print_phonebook(filename: str) -> None:
    """Kuva faili sisu ekraanile. Enne edasi liikumist küsi kasutajalt
    valmisolekut jätkamiseks"""
    contact_dict = read_phonebook(filename)
    for names, nr in contact_dict.items():
        print(f"|{names:^12}|{nr:^16}|")
    done = ""
    while done.lower() != "y":
        done = input("Kas jätkame uue toiminguga? (y/ ) ")
    else:
        main_menu()


def read_phonebook(filename: str) -> dict:
    """Loe faili sisu. Kui nimetatud faili ei ole, siis loo fail."""
    phonebook_name_nr = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f, delimiter=",")
            for name, nr in csv_reader:
                phonebook_name_nr[name] = nr
    except FileNotFoundError:
        write_phonebook(filename)
        read_phonebook(filename)
    return phonebook_name_nr


def reverse_dict(contact_dict: dict) -> dict:
    """Pööra sõnastiku andmed ümber (key muutub value'ks)
    Tagasta uus sõnastik"""
    reverse_dict_result = {}
    for name, phone_nr in contact_dict.items():
        reverse_dict_result[phone_nr] = name
    return reverse_dict_result


def check_value(contact_dict: dict, search_value: str) -> tuple[bool, bool]:
    """Võrdle sõnastiku otsitava väärtusega. Otsi väärtust nii võtmete kui väärtuste seast.
    Tagasta tõene või väär, väärtuse leidmise kohta sõnastikus."""
    check_dict = contact_dict
    reverse_check_dict = reverse_dict(contact_dict)
    key = search_value.lower().capitalize()
    return key in check_dict, key in reverse_check_dict


def name_file() -> None:
    """Küsi kasutaja sisendit kasutatava faili nime kohta.
    Faili nime määramisel kuva ekraanile kinnitus sõnum.
    Muuda faili globaalselt"""
    global filename
    filename = input("Sisesta telefoniraamatu faili nimi: ")
    if filename == "":
        print("Jätsid faili nime tühjaks!")
        main_menu()
    print(f"Kasutatakse fail nimega '{filename}'.")


def action_selection(action_nr, actions) -> None:
    """Vali funktsioon pea menus tehtud valiku põhjal.
    Käivita funktsioonid.
    Õige valiku puhul sulge programm."""
    try:
        if int(action_nr) == 5:
            raise SystemExit
        elif int(action_nr) == 4:
            name_file()
            main_menu()
        else:
            if filename == "":
                name_file()
            actions[action_nr][1](filename)
    except (KeyError, ValueError):
        print("Tegevuse valikut ei tehtud sobiva väärtusega!")
        main_menu()


def main_menu() -> None:
    """Kuva ekraanile toimngute menuu ja küsi kasutaja sisendit, millist funktsiooni
    soovitakse käivitada"""
    actions = {"0": ("Otsi kontakti telefoniraamatu failist.", find_data_in_phonebook),
               "1": ("Kuva telefoniraamatu faili sisu.", print_phonebook),
               "2": ("Lisa telefoniraamatu failile andmeid.", expand_phonebook),
               "3": ("Kirjuta uus telefoniraamat.",create_phonebook),
               "4": ("Nimeta kasutatav fail.", name_file),
               "5": ("Sulge programm.",)}
    for action, text in actions.items():
        print(f"{action:^3} | {text[0]}")
    action_nr = input("Tegevuse valikuks kirjuta sobiv number ülemisest valikust: ")
    action_selection(action_nr, actions)


if __name__ == "__main__":
    main_menu()