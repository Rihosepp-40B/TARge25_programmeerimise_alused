"""Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:

Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
>> 15
Liiga suur, proovi uuesti.
>> 7
Liiga väike, proovi uuesti.
>> 9
Liiga väike, proovi uuesti.
>> 11
Tubli, arvasid ära. Arv oli 11.
Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem."""

"""Täienda eelmist programmi selliselt, et kasutajal oleks arvu arvamiseks 5 korda, s. t. kui viie korra jooksul ära ei
arvata, ütleb arvuti, et kaotasid, ning teatab õige arvu. Täienda vastavalt ka plokkskeemi."""


from random import randint


def play_quessing_game():
    correct_answer = randint(1, 20)
    tries = 0
    while tries < 5:
        player_answer = int(input("Mõtlesin ühele täisarvule 1-20ni. Mis arv see on? "))
        tries += 1
        if player_answer > correct_answer:
            print("Liiga suur, proovi uuesti.")
            continue
        if player_answer < correct_answer:
            print("Liiga väike, proovi uuesti.")
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct_answer}.")
        break
    else:
        print(f"Katsed said otsa. Õige arv oli {correct_answer}.")


if __name__ == '__main__':
    play_quessing_game()