"""Make world.
Selle osa eesmärk on lugeda mängumaailma 'kaart' failist ning genereerida tegelaste jaoks juhuslike koordinaate.
Siin osas demonstreerin faili andmete lugemist ning trükkimist sõnastikku."""

import random
from weapons import Weapon
from characters import NPC, Troll, Human


class Location:
    """Location class."""

    def __init__(self, coordinates, npc: NPC = None, weapons: list[Weapon] = None):
        """Initialize location class."""
        self.__coordinates = coordinates
        self.__npc = npc
        self.__weapons = weapons
        self.__visited = False
        self.__inspected = False

    def get_coordinates(self):
        """Return location coordinates."""
        return self.__coordinates

    def get_npc(self):
        """Return NPC in location."""
        return self.__npc

    def get_weapons(self):
        """Return weapons around the area."""
        return self.__weapons

    def get_weapon_types(self):
        """Return list of weapon types."""
        weapon_types = []
        if self.get_weapons() is not None:
            for w in self.get_weapons():
                weapon_types.append(w.get_weapon_type())
        return weapon_types

    def get_visited(self):
        """Return if player has visited location."""
        return self.__visited

    def get_inspected(self):
        """Return if player has inspected location."""
        return self.__inspected

    def remove_weapon(self, weapon):
        """Remove weapon from location."""
        self.__weapons.remove(weapon)

    def add_weapon(self, weapon):
        """Add weapon to location."""
        self.__weapons.append(weapon)

    def set_visited(self):
        """Set visited True."""
        self.__visited = True

    def set_inspected(self):
        """Set inspected True"""
        self.__inspected = True


def build_world_locations(object_dict):
    """Make location objects."""
    locations = {}
    for row, value in read_world_from_file().items():
        for col in value:
            npc, weapons = None, None
            coordinate = f"{row}-{col}"
            if coordinate in object_dict:
                if "npc" in object_dict[coordinate]:
                    npc = object_dict[coordinate]["npc"]
                if "weapons" in object_dict[coordinate]:
                    weapons = object_dict[coordinate]["weapons"]
            locations.setdefault(coordinate, Location(coordinate, npc, weapons))
    return locations


def read_world_from_file(filename="world1.txt") -> dict:
    """Load world from file."""
    world = {}
    key = 1
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            world[f"{key}"] = line.split(" ")
            key = key + 1
    return world


def generate_location():
    """Return random location in world."""
    world = read_world_from_file()
    row = random.choice(list(world.keys()))
    col = random.choice(world[row])
    return f"{row}-{col}"


def spawn_world_objects(param, player, wpn_multiplier=2):
    """Return dictionary of locations with lists of characters and weapons (doesn't include weapons equipped)."""
    spawned_npc = spawn_npc(param, player)
    world_objects = spawn_weapons(param * wpn_multiplier)

    for key, value in spawned_npc.items():
        world_objects.setdefault(key, {}).update(value)
    return world_objects


def spawn_npc(param, player):
    """Return dictionary of locations with list of npc at that locations."""
    spawned_npc = {}
    while len(spawned_npc) < param:
        location = generate_location()
        if location == player.get_location():
            continue
        if location not in spawned_npc:
            spawned_npc.setdefault(location, {"npc": [random.choice([Troll(), Human()])]})
    return spawned_npc


def spawn_weapons(param):
    """Return dictionary of locations with added weapons to locations."""
    spawned_weapon = {}
    for i in range(param):
        location = generate_location()
        weapon = Weapon()
        if weapon.get_weapon_type() == "Fists":
            continue
        if location not in spawned_weapon:
            spawned_weapon.setdefault(location, {"weapons": [weapon]})
        else:
            spawned_weapon[location]["weapons"].append(weapon)
    return spawned_weapon


def drop_weapon(player, character, world_data):
    """Drop character weapon to location."""
    location = world_data[player.get_location()]
    weapon = character.get_weapon()
    if weapon.get_weapon_type() != "Fists":
        print(f"{character.get_name()}: *dropped {character.get_weapon().get_weapon_type()}*")
        character.remove_weapon()
        location.add_weapon(weapon)


def take_weapon(player, weapon, world_data):
    """Take weapon from location and add to player."""
    location = world_data[player.get_location()]
    drop_weapon(player, player, world_data)
    player.add_weapon(weapon)
    location.remove_weapon(weapon)
