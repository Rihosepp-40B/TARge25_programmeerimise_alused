"""Ülesanne 4
Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise"""


import _03_reverse_dict as dicts  # import ---- as dicts, toob kõik eelmisest sisse ühise aliasega "dicts"

dicts.est_eng_dict["headaega"] = "goodbye"
dicts.est_eng_dict["pott"] = "pot"
dicts.est_eng_dict["sõnastik"] = "dictionary"
dicts.est_ita_dict["headaega"] = "goodbye"
dicts.est_ita_dict["pott"] = "pentola"
dicts.est_ita_dict["sõnastik"] = "dizionario"

dicts.eng_est_dict = dicts.swap_dict_key_value(dicts.est_eng_dict)
dicts.ita_est_dict = dicts.swap_dict_key_value(dicts.est_ita_dict)

if __name__ == '__main__':
    print(f"üks -> itaalia keeles: {dicts.est_eng_dict["üks"]}")
    print(f"ciao -> eesti keeles: {dicts.ita_est_dict["ciao"]}")
    print(f"dog -> itaalia keeles: {dicts.est_ita_dict[dicts.eng_est_dict["dog"]]}")
    print(f"pentola -> inglise keeles: {dicts.est_eng_dict[dicts.ita_est_dict["pentola"]]}")