"""Ülesanne 6. Salakiri
Vahel on vaja saata sõnumeid nii, et kõrvalised inimesed, kes teksti näevad, ei mõistaks selle sisu. Teksti
krüpteerimiseks on kasutatud erinevaid võtteid. Üks lihtsaimatest viisidest on asendada iga sümbol suvalise teise
sümboliga (näiteks kõik tähed "A" asendame tähega "K", tähed "B" tähega "R" jne).

Koosta programm, mis sisaldab sõnastikku koodidega ning mis suudab kasutaja poolt sisestatud teksti selle alusel
kodeerida ja dekodeerida salakirja. Leia mingi sobiv moodus, kuidas kasutaja saaks valida teksti krüpteerimise ja
dekrüpteerimise vahel.

Täiendusi:

Selliste tekstide "lahtimuukimiseks" on erinevaid võimalusi. Näiteks on igal keele oma tähtede esinemissagedus, seega
võime pikema teksti puhul loendada, mitu korda mingit asendussümbolit tekstis esineb, leida esinemissagedus kõigi
tähtede hulgas ning pakkuda sobivaid "õigeid" sümboleid selle asemel, näiteks kõige sagedamini esineb eesti keeles
a-täht (ca 12% kõigist tähtedest), sellele järgnevad tähed "e", "i", "s" jne, otsi internetist eesti keele tähtede
esinemissagedusi. Mõtle, kuidas saaks algoritmi täiendada, et teksti dekrüpteerimine oleks raskem."""


element_code = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
    "ü": 53,
    "Ü": 54,
    "õ": 55,
    "Õ": 56,
    "ö": 57,
    "Ö": 58,
    "ä": 59,
    "Ä": 60,
    "1": 61,
    "2": 62,
    "3": 63,
    "4": 64,
    "5": 65,
    "6": 66,
    "7": 67,
    "8": 68,
    "9": 69,
    "0": 70,
    ",": 71,
    ".": 72,
    "!": 73,
    "?": 74,
    ")": 75,
    "(": 76,
    "/": 77,
    "*": 78,
    "+": 79,
    "-": 80,
    "=": 81,
    "@": 82,
    "[": 83,
    "]": 84,
    "{": 85,
    "}": 86,
    "#": 87,
    "$": 88,
    "%": 89,
    "&": 90,
    "'": 91,
    ":": 92,
    ";": 93,
    "€": 94,
    "<": 95,
    ">": 96,
    " ": 97,
    "_": 98
}
def cypher_text(text: str) -> str:
    cypher_text = ""
    for char in text:
