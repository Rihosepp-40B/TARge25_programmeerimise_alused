"""Eestis kasutatav isikukood koosneb üheteistkümnest numbrist. Tutvu isikukoodi struktuuriga
(https://et.wikipedia.org/wiki/Isikukood) ja kirjuta programm, mis analüüsib isikukoode ja väljastab võimalikult
rohkem infot selle kohta (sünnikuupäev, sugu jne). Isikukoodi käsitlege kui sümbolite kogumit ehk sõnet (kuigi see
koosneb numbritest), analüüsimiseks kasutage sõneoperatsioone (vt. käsiraamat). Kuna isikukoode on keeruline testimise
ajal korduvalt sisestada, on alguses mõistlik sisestada erinevad isikukoodid ning kommenteerida vastavalt vajadusele
ülearused välja, näiteks järgnevalt kasutatakse teisel real olevat isikukoodi:

#isikukood = "60201302715"
isikukood = "48008082727"
#isikukood = "31212230156"
[...]
Hiljem võib lisada isikukoodi küsimise kasutajalt.

Täiendusi:

Vastavalt toodud isikukoodi tutvustavale artiklile võrdle esimest kümmet numbrit ja viimast numbrit (nn.
kontrollnumbrit), et teha selgeks, kas isikukood on üldse kehtiv. Kuna isikukoodi võtame kui sõnet, aga seal olevaid
arve on vaja korrutada, peame tegema tüübiteisenduse: sõnena oleva arvu peame teisendama täisarvuks
(funktsioon"int()").
Koosta funktsioon, mis ise automaatselt koostab kehtivaid isikukoode. Võimatud on näiteks isikukoodid vale
kontrollnumbriga, kuid ka sellised, mis viitavad olematule kuupäevale (algusega "3950230...", mis tähendaks 30.
veebruari) vms. Vali kas "ohutu" tee (ette on antud piirid, mis kehtivad igal juhul) või loo sisemised sõltuvused
(stiilis "kui kuu on aprill, siis maksimaalsete päevade arv on 30")."""

