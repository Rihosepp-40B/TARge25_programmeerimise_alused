"""Sõne (string)
Järgnevates ülesannetes tutvume sõnega ning uurime lähemalt, mida sellega teha saab.

Sõne kasutatakse teksti
esitamiseks, selle kirja panemiseks kasutatakse ülakomasid ('see on
sõne') või jutumärke ("see on ka sõne").
Loe enne ülesannete lahendamist teema kohta lähemalt PyDocist.

1. Sõne-tüüpi muutujate deklareerimine
Loo muutuja first_name, mille väärtus on "James", ja last_name, mille väärtus on "Bond".
2. Sõnede kujundamine - names
Loo muutuja full_name, mille väärtuseks on sõne järgmisel kujul: "first_name last_name", kus first_name ja last_name
on eelmises ülesandes loodud muutujate väärtused. Kasuta selleks sõnede liitmist.
Loo muutuja self_description_sentence, mille väärtus on sõne järgmisel kujul: "My name is last_name, first_name
last_name.", kus first_name ja last_name on eelmises ülesandes loodud muutujate väärtused. Sõne kujundamiseks kasuta
f stringi.
3. Sõnede kujundamine - cake string
Loo muutuja cake = "vahukoormarjadtäidispõhi".

See on meie kook, mille kihid on vaja
printida ülevalt alla kindlas järjekorras: vahukoor, marjad, täidis,
põhi. Kasuta selleks vaid ühte print() funktsiooni.

Tulemus peaks välja nägema selline:

vahukoor
marjad
täidis
põhi

Vihje: \n kasutamisel prinditakse sõne teisele reale.

4. Sõnede tükeldamine
Harjutame sõnede tükeldamist ehk slice notation'i kasutamist.

Loo muutuja original_string = "Programming is fun!"

Seda sõne hakkame edaspidi tükeldama slice notation'i abil.

Loo muutuja backwards, mille väärtus on esialgne sõne tagurpidi (ehk "!nuf si gnimmargorP").

Loo muutuja every_other, mille väärtus on esialgsest sõnest iga järgmine täht ehk esimene, kolmas, viies jne.

Loo muutuja first_word_reversed, mille väärtus on esialgse sõne esimene sõna (ehk Programming) tagurpidi."""


first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."
cake = "vahukoormarjadtäidispõhi"
print(f"{cake[:8]}\n{cake[8:14]}\n{cake[14:20]}\n{cake[20:]}")
original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string[0:11][::-1]