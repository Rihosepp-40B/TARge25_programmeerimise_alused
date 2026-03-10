"""Koosta programm telefoniraamatu loomiseks.

1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""


import csv


def print_phonebook(filename):
    read_phonebook(filename)
    pass


def read_phonebook(filename):
    with open(filename, "r") as f:
        pass


def add_to_phonebook(filename):
    with open(filename, "a") as f:
        pass


def create_phonebook(filename):
    first_row = ("Name", "Phone_nr")
    with open(filename, "w", newline="") as f:
        csv_writer = csv.writer(filename, delimiter=",")
        csv_writer.writerow(first_row)
        while True:
            name = input("Sisesta nimi: ")
            if name == "":
                break
            phone_nr = input(f"Sisesta {name} telefoni number: ")
            csv_writer.writerow([name, phone_nr])


if __name__ == "__main__":
    filename = input("Siesta failinimi: ")
    create_phonebook(filename)