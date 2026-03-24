"""Ülesanne 2
Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri ja iga
rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse."""


def create_poem_file(filename: str):
    """Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale,
    perekonna- ja eesnimi tühikuga eraldatult)."""
    content = """Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(content)

def poem_rows_as_list(filename: str) -> list[str]:
    listed_poem = []
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            listed_poem.append(line.strip())
    return listed_poem


def poem_with_rows_and_count(filename: str) -> None:
    listed_poem = poem_rows_as_list(filename)
    for i, line in enumerate(listed_poem):
        print(f"{i + 1}. {line} ({len(line)})")


if __name__ == '__main__':
    filename = "luuletused.txt"
    create_poem_file(filename)
    poem_with_rows_and_count(filename)