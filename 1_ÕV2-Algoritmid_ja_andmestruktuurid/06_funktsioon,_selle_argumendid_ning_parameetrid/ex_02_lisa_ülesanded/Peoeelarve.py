"""Küsi vajalik info peoeelarve koostamiseks: kutsutud inimeste arv, osalev inimeste arv, peokoha hind, lisanduv hind
inimesekohta. Väljasta sisendite järgi maksimaalne ja minimaalne eelarve."""


def eelarve(guest_count: int) -> float:
    return venue_price + price_per_guest * guest_count

if __name__ == '__main__':
    venue_price = float(input("Kui palju maksab koha rent? "))
    price_per_guest = float(input("Kui palju on hind inimese kohta? "))
    invited_guests = int(input("Kui palju inimesi on kutsutud? "))
    coming_guests = int(input("Mitu inimest on oma tulekut kinnitanud? "))
    max_budget = eelarve(invited_guests)
    min_budget = eelarve(coming_guests)
    print(f"Maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")