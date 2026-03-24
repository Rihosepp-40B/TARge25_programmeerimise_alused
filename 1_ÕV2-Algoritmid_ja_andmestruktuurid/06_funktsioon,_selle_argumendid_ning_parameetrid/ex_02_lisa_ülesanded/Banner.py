"""Küsi reklaamlauste ja mitu korda seda kuvada. Kuva reklaamlause, kus kõik tähed on suured tähed"""


def banner() ->str:
    return slogan.upper()


if __name__ == '__main__':
    slogan = input("Kirjuta oma reklaamlause? ")
    repeat_count = int(input("Mitu korda tahad reklaamlauset kuvada? "))
    print(f"{banner()}\n" * repeat_count)