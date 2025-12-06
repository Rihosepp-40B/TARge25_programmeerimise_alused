"""Küsi elektrihind senti/kilovatt-tunni kohta. Tagasta elektrihind eurot/megavatt-tunni kohta"""


def elektrihind(price_in_s_kwh: float) -> float:
    price_in_eur_mwh = price_in_s_kwh / 100 * 1000
    return price_in_eur_mwh


if __name__ == '__main__':
    given_price_s_kwh = input("Sisesta elektrihind sentides kilovatt-tunni kohta: ")
    converted_price = elektrihind(float(given_price_s_kwh))
    print(f"{given_price_s_kwh} s/kWh on {converted_price} €/MWh")