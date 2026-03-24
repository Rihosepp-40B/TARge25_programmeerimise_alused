"""Ülesanne 4. Ennustaja (Magic 8-ball)
Moodusta järjend järgnevate sõnedega:

Jah, kindlasti!
Jah!
Võib-olla!
Ei!
Tee programm, kus kasutaja saab küsida jah/ei küsimuse ja programm annab vastuse ühe suvalise elemendi eelnevast
järjendist.

Juhuslike arvude genereerimist vaatame tulevikus, kuid praegu lisame programmi algusesse rea, tänu millele Python
suudab juhuslikke arve genereerida:

import random
Seejärel võime suvalises kohas programmis kasutada juhusliku arvu saamiseks funktsiooni random.randint(x, y), mis
genereerib juhusliku täisarvu x-st y-ni (mõlemad kaasaarvatud), näiteks:

juhuarv = random.randint(1, 10)
Lisa ka sisse- ja väljajuhatavad tekstid, et dialoog kasutajaga oleks võimalikult loomulik.

Kui valmis, siis lisa järjendisse 20 erinevat vastusevarianti, mille ingliskeelsed vasted leiad leheküljelt
https://en.wikipedia.org/wiki/Magic_8-Ball"""


import random


answers = ["Jah kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
"It is certain"
"It is decidedly so           "
"Without a doubt              "
"Yes definitely               "
"You may rely onit            "
"As I see it, yes             "
"Most likely                  "
"Outlook good                 "
"Yes                          "
"Signs point to yes           "
"Reply hazy, try again        "
"Ask again later              "
"Better not tell you now      "
"Cannot predict now           "
"Concentrate and ask again    "
"Don't count on it            "
"My reply is no               "
"My sources say no            "
"Outlook not so good          "
"Very doubtful                "


def ask_magic_eight_ball():
    question = input("Palun sisesta oma Jah/ei küsimus ennustajale ")
    random_number = random.randint(0, len(answers) - 1)
    return answers[random_number]


if __name__ == '__main__':
    print("Tere tulemast maailmakuulsa ennustaja jutule")
    answer = ask_magic_eight_ball()
    print(f"Ennustaja kaalus sinu küsimust ja tuli järeldusele, {answer}")