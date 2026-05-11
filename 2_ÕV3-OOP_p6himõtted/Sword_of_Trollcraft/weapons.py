"""Create weapons.
Selle osa oodatav tulemus on, et loob mängu relvad, erinevate juhu andmetega.
Siin osas demonstreerin sõnastiku ja loendi kasutamist.
"""
import random
from random import randint


class Weapon:
    """Weapon class."""

    __weapon_types = {"Short sword": [2, 6, 9], "Long sword": [5, 8, 7], "Axe": [3, 6, 8], "Spear": [6, 9, 5],
                      "Great sword": [8, 10, 5], "Fists": [1, 1, 10]}

    def __init__(self, w_type="Random"):
        """Initialize weapons."""
        if w_type == "Fists":
            self.__type = w_type
        else:
            self.__type = random.choice(list(self.__weapon_types.keys()))
        self.__damage = randint(self.__weapon_types[self.__type][0], self.__weapon_types[self.__type][1])
        self.__hit_chance = self.__weapon_types[self.__type][2]
        if self.__type == "Fists":
            self.__durability = "Unlimited"
        else:
            self.__durability = randint(1, 10)

    def get_damage(self):
        """Return weapon damage."""
        return self.__damage

    def get_hit_chance(self):
        """Return hit chance."""
        return self.__hit_chance

    def get_weapon_type(self):
        """Return weapon type."""
        return self.__type

    def inspect(self):
        """Return weapon stats."""
        print(f"""|{'Weapon: ':>37}{self.__type:<37}|
|{"_" * 74}|
|{'DMG: ':>15}|{self.__damage:^20}||{'Durability: ':>15}|{self.__durability:^20}|
|{'Hit chance: ':>15}|{f"{self.__hit_chance * 10}%":^20}||""")

    def remove_durability(self):
        """Remove weapon durability point."""
        if self.__type != "Fists":
            if self.__durability > 0:
                self.__durability = self.__durability - 1

    def get_durability(self):
        """Return weapon durability points."""
        return self.__durability

    def __str__(self):
        """Return weapon type."""
        return self.__type


if __name__ == '__main__':
    weapon = Weapon()
    print(weapon)
