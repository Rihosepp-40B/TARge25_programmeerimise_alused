"""Ülesanne 6
Ristsõnade lahendamine on sageli keeruline: teame küll sõna pikkust ja mõnd tähte, kuid tervet sõna ära arvata ei
oska. Loo programm, mis abistaks ristsõna lahendajat: kasutajalt küsitakse sõna pikkust ning esimest ja viimast
tähte ning väljastatakse sõnastikus olevad kõikvõimalikud sellised sõnad. Sõnastiku (algvormide e. lemmade loendi)
võid leida näiteks siit: http://www.eki.ee/tarkvara/wordlist/. Arendusvõimalusi:

Kasutaja võib ette anda pikema sõna alguse ja lõpu.
Küsida võib keerulisemaid mustreid, näiteks küsimus stiilis "k-s-" otsib kõiki neljatähelisi sõnu, mille esimene
täht on "k", kolmas täht "s" (näiteks "kass", "kask", "kast", "kest", "kosk" jne)."""


def get_word(begin: str, end: str, length: int) -> list[str]:
    result = []
    with open("lemmad2013.txt", encoding="UTF-8") as f:
        for line in f:
            word = line.strip()
            if len(word) == length and \
                len(begin) == 0 or word.startswith(begin) and \
                    (len(end) == 0 or word.endswith(end)):
                result.append(word)
    return result


https://arhiiv.eki.ee/tarkvara/wordlist/

if __name__ == '__main__':
    beginning = input("Sisesta sõna alguse täht: ")
    ending = input("Sisesta sõna lõpu täht: ")
    length = input("Sisesta sõna pikkus: ")
