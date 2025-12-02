def eelarve(guests: int) ->int:
    return guests * sum_per_guest + place_price


if __name__ == '__main__':
    place_price = int(input("Mis on koha rendi hind? "))
    sum_per_guest = int(input("Mis on lisanduv hind inimese kohta? "))
    invited_guests = int(input("Mitu inimest on kutsutud? "))
    confirmed_guests = int(input("Mitu inimest on lubanud tulla? "))
    min_budget = eelarve(confirmed_guests)
    max_budget = eelarve(invited_guests)
    print(f"Maksimaalne eelarve on {max_budget}")
    print(f"Minimaalne eelarve on {min_budget}")

