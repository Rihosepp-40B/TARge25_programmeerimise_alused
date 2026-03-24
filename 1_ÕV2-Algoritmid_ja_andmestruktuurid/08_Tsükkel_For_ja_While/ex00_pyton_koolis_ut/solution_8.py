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
                        erinevus = f"\nSee kiirus on vahemaa läbimiseks eelmisest {difference_from_last} tundi kiirem."
                    elif difference_from_last < 0.0:
                        erinevus = f"\nSee kiirus on vahemaa läbimiseks eelmisest {abs(difference_from_last)} tundi aeglasem."
                    else:
                        erinevus = ""
                print(f"Kiirusega {speed} km/h kulub vahemaa {distance} km läbimiseks {time} tundi.{erinevus}\n")
                last_time = time
                count += 1


"""---------------------------------------------------------------------------------------------------------"""
""" Õpetaja versioon"""

def calculate_travel_time_in_seconds(distance: int, speed: int) -> float:
    time_in_hours = distance / speed
    return time_in_hours * 3600


def convert_to_hours_mins_secs(time_in_seconds: float) -> tuple[int, int, float]:
    hours = int(time_in_seconds // 3600)
    remaining_seconds = time_in_seconds % 3600
    minutes = int(remaining_seconds // 60)
    remaining_seconds = remaining_seconds % 60
    return hours, minutes, remaining_seconds


def format_time_string(hours: int, minutes: int, seconds: float) -> str:
    result_values = []
    if hours == 1:
        result_values += ["1 tund"]
    elif hours > 1:
        result_values += [f"{hours} tundi"]
    if minutes == 1:
        result_values += ["1 minut"]
    elif minutes > 1:
        result_values += [f"{minutes} minutit"]
    if round(seconds, 2) == 1:
        result_values += ["1 sekund"]
    elif round(seconds, 2) != 0:
        result_values += [f"{seconds:.2f} sekundit"]
    match(len(result_values)):
        case 1:
            return f"{result_values[0]}"
        case 2:
            return f"{result_values[0]} ja {result_values[1]}"
        case 3:
            return f"{result_values[0]}, {result_values[1]} ja {result_values[2]}"
        case _:
            return ", ".join(result_values)


def display_travel_time_difference(previous_travel_time: float, travel_time: float) -> None:
    hours, minutes, seconds = convert_to_hours_mins_secs(travel_time)
    time_string = format_time_string(hours, minutes, seconds)
    print(f"Sõidule kulub {time_string}")

    if previous_travel_time != -1:
        difference = previous_travel_time - travel_time
        hours, minutes, seconds = convert_to_hours_mins_secs(abs(difference))
        time_string = format_time_string(hours, minutes, seconds)
        if difference > 0:
            print(f"Jõuad kohale {time_string} varem")
        else:
            print(f"Jõuad kohale {time_string} hiljem")


def opetaja_versioon():
    distance = int(input("Sisesta läbitav vahemaa kilomeetites: "))
    speed_text = "1"
    previous_travel_time = -1
    while len(speed_text) > 0:
        speed_text = input("Sisesta sõidukiirus: ")
        if speed_text.isdigit():
            speed = int(speed_text)
            travel_time = calculate_travel_time_in_seconds(distance, speed)
            display_travel_time_difference(previous_travel_time, travel_time)
            previous_travel_time = travel_time


if __name__ == '__main__':
    #infinite_time_for_distance()
    opetaja_versioon()
