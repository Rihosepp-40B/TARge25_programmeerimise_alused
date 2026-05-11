"""Game 'Sword of TrollCraft.
Programmi peab looma maailma, mis on täidetud erinevate tegelaste, relvadega. Mängija navigeerib mängu maailmas läbi
teksti valikute. Eesmärk on mängijal leida pahad tegelased ning nad hävitada. Võitlus valikus on mängijal valikud:
põikle (vasakule-paremale), viruta (vasakule, keskele, paremale, eemaldu lahingust, põgene, palu vabandust (juhul kui
sõbralik, siis lõpetab võitluse). Valikud koosnevad kahe tegevuse kombost (väljaarvatud vabandus). Vastased teevad
sarnaseid kahe-osalisi kombosid."""
import time

from world import spawn_world_objects, generate_location, build_world_locations, read_world_from_file
from characters import Player
from navigation import navigation_menu
from actions import action_menu
from combat_actions import Combatant
from common import exit_program, print_sword_of_trollcraft, selection_exception, print_top_10


def location_menu(player, world_data, combat):
    """Return action menu from different selections."""
    selections = []
    selections.extend(navigation_menu(player, read_world_from_file(), world_data))
    selections.extend(action_menu(player, world_data, combat))

    actions = {"q": ("Exit Program", lambda: exit_program(player))}
    nr = 1
    for i in selections:
        actions[f"{nr}"] = i
        nr += 1

    return actions


def check_inspection(player, world_data):
    """Print info lines about inspected locations."""
    print(f"Your current coordinates: {player.get_location()}")
    time.sleep(0.3)
    if world_data[player.get_location()].get_inspected():
        npc = world_data[player.get_location()].get_npc()
        print("This area has been inspected!")
        time.sleep(0.2)
        if npc is not None:
            print(f"Creatures in area: {npc[0].get_race()} named {npc[0].get_name()}")
            time.sleep(0.2)
        print(f"Items in area: {world_data[player.get_location()].get_weapon_types()}")
    else:
        print("Area not inspected!")
    print()
    time.sleep(0.2)


def game_ui(player, world_data, combat):
    """Print all possible moves and actions in any situation."""
    if player.check_if_dead():
        print("GAME OVER! YOU DIED!")
        exit_program(player)
    check_inspection(player, world_data)
    actions = location_menu(player, world_data, combat)

    for action, text in actions.items():
        print(f"{action:^3} | {text[0]}")
        time.sleep(0.2)
    game_ui_selection(actions)
    game_ui(player, world_data, combat)


def game_ui_selection(actions):
    """Ask input and run function based of choice."""
    try:
        print()
        action = input("Select action: ")
        time.sleep(0.2)
        actions[action][1]()
        return
    except (KeyError, ValueError, IndexError):
        selection_exception()
        game_ui_selection(actions)
    finally:
        print()


def start_game():
    """Set up new game: ask player name for setting character name, spawn world with objects. Take player to game ui."""
    name = input("Player insert your character name: ")
    print()
    player = Player(name, generate_location())
    combatant1 = Combatant()
    combatant2 = Combatant()
    combat = (combatant1, combatant2)
    npc_count = 40
    world_info = spawn_world_objects(npc_count, player)
    world_data = build_world_locations(world_info)
    game_ui(player, world_data, combat)


def main_menu() -> None:
    """Print menu options on screen and ask player to make input."""
    actions = {"0": ("Start game.", lambda: start_game()),
               "1": ("See score tabel.", lambda: print_top_10()),
               "q": ("Exit program.", lambda: exit_program(None))}
    for action, text in actions.items():
        print(f"{action:^3} | {text[0]}")
        time.sleep(0.3)
    menu_selection(actions)


def menu_selection(actions) -> None:
    """Start function selected in main menu."""
    try:
        print()
        action_nr = input("Type preferable option from above: ")
        if action_nr == "1":
            print()
            actions[action_nr][1]()
            print()
            main_menu()
        else:
            actions[action_nr][1]()
    except (KeyError, ValueError, IndexError):
        selection_exception()
        menu_selection(actions)


def run_game():
    """Run program."""
    print_sword_of_trollcraft()
    main_menu()


if __name__ == '__main__':
    run_game()
