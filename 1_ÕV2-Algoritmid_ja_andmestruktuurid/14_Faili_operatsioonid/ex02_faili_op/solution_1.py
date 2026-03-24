"""Ülesanne. Cooperi test
Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga. On määratud erinevad hindenormid meestele
ja naistele.
Koostada funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:
    Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
    Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
    Sõne „rahuldav“ muudel juhtudel
Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu
Koostada programm, mis küsib kasutajalt:
    failinime,
Programm peab:
    lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
    funktsiooniga arvutama hinded ja väljastama need ekraanile
    arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni ümardatud keskmised ning funktsiooni
    abil keskmised hinded.
Näide funktsiooni rakendamisest
# >>> hinda(1800,’N’)
’rahuldav, järgmisest hindest puudu 800 m’
# >>> hinda(1799,’N’)
’nõrk, järgmisest hindest puudu 1m’
# >>> hinda(2600,’N’)
’väga hea’
Näide programmi tööst
Faili cooper.txt sisu:
    1900 N
    1800 M
    2700 M
    2600 N
    1400 M
    3801 N
    1500 N
    1800 N

Programmi töö:
    Sisestage failinimi: cooper.txt
        N 1900 m, rahuldav, järgmisest hindest puudu 700 m
        M 1800 m, nõrk, järgmisest hindest puudu 200 m
        M 2700 m, rahuldav, järgmisest hindest puudu 100 m
        N 2600 m, väga hea
        M 1400 m, nõrk, järgmisest hindest puudu 600 m
        N 3801 m, väga hea
        N 1500 m, nõrk, järgmisest hindest puudu 300 m
        N 1800 m, rahuldav, järgmisest hindest puudu 800 m
        Keskmised:
        M 1967 m, nõrk, järgmisest hindest puudu 33 m
        N 2320 m, rahuldav, järgmisest hindest puudu 280 m"""
import csv


def get_result(dist: int, gender: str) -> str:
    d = int(dist)
    next_g = "järgmisest hindest puudu"
    high = (2800, 2600)
    low = (2000, 1800)
    gen = gender.upper()
    if gen == "M":
        select = 0
    else:
        select = 1
    if d >= high[select]:
        result = "väga hea"
    elif d < low[select]:
        result = f"nõrk, {next_g} {low[select] - d} m"
    else:
        result = f"rahuldav, {next_g} {high[select] - d} m"
    return f"{gen} {dist} m, {result}"


def average_dist(distance_list: list) -> int:
    average = round(sum(distance_list) / len(distance_list))
    return average


def give_grade_to_runner(filename: str):
    dist_list_m = []
    dist_list_w = []
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        for dist, gen in csv_reader:
            print(get_result(dist, gen))
            if gen.upper() == "M":
                dist_list_m.append(int(dist))
            else:
                dist_list_w.append(int(dist))
    print("\033[4mKeskmised:\033[0m")
    print(get_result(average_dist(dist_list_m), "M"))
    print(get_result(average_dist(dist_list_w), "N"))


if __name__ == '__main__':
    cooper = input("Siseta cooperi tulemuste faili nimi: ")
    give_grade_to_runner(cooper)