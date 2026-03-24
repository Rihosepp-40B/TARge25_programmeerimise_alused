"""Võta euro sentide järjendist arvud 1,2 ja 5 ning väljasta nende summa. Järjendit saab sisestada ka .txt failiga"""


def pronkskarva_summa() -> int:
    bronze_coins = [1, 2, 5]
    match_coins = filter(lambda x: x in bronze_coins, all_coins) #filtreeri loetelust väiksem loetelu (x)
    return sum(match_coins)


if __name__ == '__main__':
    coin_file_name = input("Sisesta oma mündi loetelu faili nimi (nt. mündid.txt): ")

    with open(coin_file_name, "r") as file:
        file_content = file.readlines()

    all_coins = [int(line.strip()) for line in file_content]
    print(f"Pronkskarva sentide (1, 2 ja 5) kogu summa on {pronkskarva_summa()} senti")