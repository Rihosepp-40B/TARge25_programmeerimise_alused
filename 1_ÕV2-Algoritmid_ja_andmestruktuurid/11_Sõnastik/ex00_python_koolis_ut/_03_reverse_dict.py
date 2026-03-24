"""Ülesanne 3
Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti keeles, vaid vastavalt kas inglise
või itaalia keeles. Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad."""


from _02_translate import est_eng_dict, est_ita_dict

# k = key, v = value
"""eng_est_dict = {}
for k in est_eng_dict:
    eng_est_dict[est_eng_dict[k]] = k

ita_est_dict = {}
for k in est_ita_dict:
    ita_est_dict[est_ita_dict[k]] = k"""

# lühemalt
"""
eng_est_dict = {}
for k, v in est_eng_dict.items():
    eng_est_dict[v] = k

ita_est_dict = {}
for k, v in est_ita_dict.items():
    ita_est_dict[v] = k"""

# õpetaja versioon
def swap_dict_key_value(original_dict: dict[str, str]) -> dict[str, str]:
    result_dict = {}
    for k, v in original_dict.items():
        result_dict[v] = k
    return result_dict

eng_est_dict = swap_dict_key_value(est_eng_dict)
ita_est_dict = swap_dict_key_value(est_ita_dict)


if __name__ == '__main__':
    print(eng_est_dict)
    print(ita_est_dict)