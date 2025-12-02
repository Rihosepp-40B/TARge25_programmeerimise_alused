def elektrihind(price_s_kw: float) -> float:
    price_in_eur = price_s_kw / 100
    return price_in_eur * 1000

if __name__ == '__main__':
    given_price_str = input("Sisesta elektrihind sentides kilovatt-tunni kohta: ")
    converted_price = elektrihind(float(given_price_str))
    print(f"{given_price_str} s/kWh on {converted_price} €/MWh")