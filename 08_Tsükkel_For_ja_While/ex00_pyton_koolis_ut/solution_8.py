"""Ülesanne 8
On selge, et auto kiiruse tõstmine vähendab sõidule kuluvat aega ehk ma jõuame varem sihtpunkti. Kui palju me aga ajas
võidame? Koostage programm, mis küsib käivitamisel läbitava vahemaa pikkust (kilomeetrites, see kehtib kogu programmitöö
aja), seejärel aga küsib kasutajalt korduvalt kiirust (km/h) ning väljastab selle põhjal korrektse lausega sõiduks
kuluva aja ja erinevuse eelmisest tulemusest. Kui kasutaja uut kiirust ei sisesta, vaid vajutab lihtsalt
sisestusklahvile, siis katkestatakse tsükkel ja tänatakse kasutajat."""


def calculate_time_for_distance(distance_km, speed_km_h) -> float:
    time = distance_km / speed_km_h
    return time


def infinite_time_for_distance():
    distance = ""
    exit = "Tänan, et kasutasid programmi, jätkamiseks tuleb sisestada numbriline väärtus."
    while distance == "":
        distance = input("Kui pikka vahemaad (km) läbime? ")
        if not distance.isnumeric():
            print(exit)
            break
        else:
            last_time = 0
            count = 0
            while True:
                speed = input("Sisesta kiirus (km/h) millega vahemaad läbida: ")
                if not speed.isnumeric():
                    print(exit)
                    break
                time = calculate_time_for_distance(float(distance),float(speed))
                if count == 0:
                    erinevus = ""
                else:
                    difference_from_last = last_time - time
                    if difference_from_last > 0.0:
                        erinevus = f" See kiirus on vahemaa läbimiseks eelmisest {difference_from_last} tundi kiirem."
                    elif difference_from_last < 0.0:
                        erinevus = f" See kiirus on vahemaa läbimiseks eelmisest {abs(difference_from_last)} tundi aeglasem."
                    else:
                        erinevus = ""
                print(f"Kiirusega {speed} km/h kulub vahemaa {distance} km läbimiseks {time} tundi.{erinevus}")
                last_time = time
                count += 1


if __name__ == '__main__':
    infinite_time_for_distance()