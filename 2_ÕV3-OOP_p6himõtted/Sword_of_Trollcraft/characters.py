"""Create player and NPC characters.
Selle osa oodatav tulemus on, et loob mängija objekti ning mängu maailma tegelased erinevate juhu andmetega.
Siin osas demonstreein klassi objekte, pärimist ja polumorfismi ning ka modulaarsust, konstruktorit ja kapseldamist.
Veel näitan f-sõne kasutamist koos vormistusega."""
import random
from math import floor
from random import randint
from weapons import Weapon


class Character:
    """Characters / creatures class."""

    def __init__(self, name="None", health=100, strength=5, weapon=Weapon()):
        """Initialize character."""
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__weapon = weapon

    def get_health(self):
        """Return character health status."""
        return self.__health

    def get_strength(self):
        """Return character strength status. """
        return self.__strength

    def remove_health_points(self, damage):
        """Remove health points."""
        self.__health = self.__health - damage

    def add_health(self, add_points):  # unused - meant for future iteration
        """Add health points."""
        if not self.check_if_dead():
            self.__health = self.__health + add_points
            if self.__health > 100:
                self.__health = 100

    def add_weapon(self, weapon):
        """Add weapon to character."""
        self.__weapon = weapon

    def remove_weapon(self):
        """Remove weapon from character."""
        self.__weapon = Weapon("Fists")

    def get_weapon(self):
        """Get info what weapon character has."""
        return self.__weapon

    def get_name(self):
        """Return character name."""
        return self.__name

    def get_total_dmg(self):
        """Return total damage, rounded down strength + weapon DMG."""
        return floor(self.__strength) * self.get_weapon().get_damage()

    def check_if_dead(self):
        """Return if character is dead."""
        if self.get_health() <= 0:
            return True
        return False

    def add_strength(self):
        """Add strength."""
        self.__strength = (self.__strength * 10 + 1) / 10

    def __str__(self):
        """Return character name."""
        return self.__name


class Player(Character):
    """Player class."""

    def __init__(self, name, location, weapon=Weapon("Fists")):
        """Initialize player."""
        super().__init__(name, weapon=weapon)
        self.__location = location
        self.__old_location = ""
        self.__all_visited_locations = []
        self.__score = 0

    def get_stats(self):
        """Return player stats combined with weapons."""
        print(f"""|{'Player: ':>15}|{self.get_name():^20}||{'Health: ':>15}|{self.get_health():^20}|
|{'Strength: ':>15}|{self.get_strength():^20}||{'Weapon: ':>15}|{self.get_weapon().get_weapon_type():^20}|
|{'Weapon DMG: ':>15}|{self.get_weapon().get_damage():^20}||{'Hit chance: ':>15}|{f"{self.get_weapon().get_hit_chance() * 10}%":^20}|
|{"_" * 74}|
|{'Total DMG: ':>53}|{self.get_total_dmg():^20}|""")

    def get_location(self):
        """Return character location in world."""
        return self.__location

    def set_location(self, location):
        """Set new location."""
        self.__old_location = self.__location
        if self.__location not in self.__all_visited_locations:
            self.__all_visited_locations.append(self.__location)
        self.__location = location

    def get_old_location(self):
        """Return characters last location in world."""
        return self.__old_location

    def get_all_visited_locations(self):
        """Return list of all locations visited."""
        return self.__all_visited_locations

    def set_score(self, points):
        """Set player total score."""
        self.__score = self.__score + points

    def get_score(self):
        """Return player total score."""
        return self.__score


class NPC(Character):
    """NPC class."""

    def __init__(self, name, health, strength, weapon=Weapon, is_aggressive=False, is_friendly=True, threatened=False,
                 race=""):
        """Initialize NPC character."""
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)
        self.__is_aggressive = is_aggressive
        self.__is_friendly = is_friendly
        self.__threatened = threatened
        self.__race = race
        self.__inspected = False
        self.__friendliness_known = False

    def get_inspected(self):
        """Return if npc has been inspected."""
        return self.__inspected

    def set_inspected(self):
        """Set inspected True."""
        self.__inspected = True

    def get_friendliness_known(self):  # unused - meant for future iteration
        """Return if npc friendliness has been tested."""
        return self.__friendliness_known

    def set_friendliness_known(self):  # unused - meant for future iteration
        """Set friendliness True."""
        self.__friendliness_known = True

    def get_is_friendly(self):  # unused - meant for future iteration
        """Return is or not friendly."""
        return self.__is_friendly

    def get_is_aggressive(self):  # unused - meant for future iteration
        """Return if is or not aggressive."""
        return self.__is_aggressive

    def get_threatened(self):  # unused - meant for future iteration
        """Return is NPC feels threatened."""
        return self.__threatened

    def friendly_state(self):  # unused - meant for future iteration
        """Set friendly status."""
        if self.__is_friendly:
            if self.__threatened:
                self.__threatened = False
            else:
                self.__threatened = True

    def get_race(self):
        """Return NPC's race:"""
        return self.__race

    def get_stats(self):
        """Return NPC's stats."""
        print(f"""|{f"{self.get_race()}: ":>15}|{self.get_name():^20}||{'Health: ':>15}|{self.get_health():^20}|
|{'Strength: ':>15}|{self.get_strength():^20}||{'Weapon: ':>15}|{self.get_weapon().get_weapon_type():^20}|
|{'Weapon DMG: ':>15}|{self.get_weapon().get_damage():^20}||{'Hit chance: ':>15}|{f"{self.get_weapon().get_hit_chance() * 10}%":^20}|
{"_" * 76}
|{'Total DMG: ':>53}|{self.get_total_dmg():^20}|""")


class Troll(NPC):
    """NPC Troll class."""

    names = [
        "Paih'jeju",
        "Shug'ma",
        "Kuvahn",
        "Ran'chuso",
        "Lih'jan",
        "Shogan",
        "Driboku",
        "Jon'ghen",
        "Rosuge",
        "Voxepi",
        "Tzol'jasu",
        "Rujer",
        "Rhar'so",
        "Surmepin",
        "Rah'gik",
        "Ayan",
        "Wanokuh",
        "Keh'ra",
        "U'ghipo",
        "Rih'kun"
    ]
    healths = [100, 110, 120]

    def __init__(self):
        """Initialize NPC Troll."""
        name = random.choice(self.names)
        health = random.choice(self.healths)
        strength = randint(4, 10)
        weapon = Weapon()
        aggressive = random.choice([True, False])
        friendly = random.choice([True, False])
        threatened = random.choice([True, False])
        race = "Troll"

        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_aggressive=aggressive,
                         is_friendly=friendly, threatened=threatened, race=race)


class Human(NPC):
    """NPC Human class."""
    names = [
        "Grayson Hamilton",
        "Hakan Paddley",
        "Bradyn Coombs",
        "Glen Preston",
        "Brady Bush",
        "Bryan Nutlee",
        "Austen Branson",
        "Jerry Sweete",
        "Franke Charlton",
        "Franklin Helton",
        "Barks Smyth",
        "Linn Remington",
        "Clovis Rowley",
        "Maruck Copeland",
        "Neilson Lea",
        "Adolf Barney",
        "Clemens Oakley",
        "Marcos Lester",
        "Silvain Withers",
        "Oleg Dukes"
    ]
    healths = [60, 70, 80, 90, 100]

    def __init__(self):
        """Initialize NPC Human."""
        name = random.choice(self.names)
        health = random.choice(self.healths)
        strength = randint(1, 7)
        weapon = Weapon()
        aggressive = random.choice([True, False])
        friendly = random.choice([True, False])
        threatened = random.choice([True, False])
        race = "Human"

        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_aggressive=aggressive,
                         is_friendly=friendly, threatened=threatened, race=race)
