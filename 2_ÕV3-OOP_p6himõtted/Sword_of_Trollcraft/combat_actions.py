"""Combat actions.
Selle osa eesmärk on luua mängijale võitluse valikud ning kalkuleerida sellega seotud olukordi.
Siin osas demonstreerin Klassist andmete leidmist ning sõnastike kasutamist."""
import random
import time
from common import exit_program, selection_exception


class Combatant:
    """Combat class."""
    POSITION = "middle"
    POSITION_R = "right"
    POSITION_L = "left"

    def __init__(self):
        """Initialize combat."""
        self.__combatant = None
        self.__combat_position = "middle"
        self.__strike_dir = None

    def set_combatant(self, character):
        """Set characters, who are engaging in combat."""
        self.__combatant = character

    def get_combatant(self):
        """Return parties in combat."""
        return self.__combatant

    def reset_turn_positions(self):
        """Reset combat settings back to default."""
        self.__combat_position = "middle"
        self.__strike_dir = None

    def set_position(self, position):
        """"Set combat positions."""
        combat_list = [Combatant.POSITION, Combatant.POSITION_R, Combatant.POSITION_L]
        if position.lower() in combat_list:
            self.__combat_position = position.lower()
            print(f"{self.__combatant.get_name()}: *Dodges to {position}*")

    def get_position(self):
        """Return combat position."""
        return self.__combat_position

    def set_strike_dir(self, direction):
        """set player strike direction."""
        combat_list = [Combatant.POSITION, Combatant.POSITION_R, Combatant.POSITION_L]
        if direction.lower() in combat_list:
            self.__strike_dir = direction.lower()
            print(f"{self.__combatant.get_name()}: *Strikes to {direction}*")

    def get_strike_dir(self):
        """Return strike direction."""
        return self.__strike_dir

    def get_aar(self):
        """Print after action report."""
        print(f"{self.__combatant.get_name()}: {self.__combatant.get_health()} points left.")
        time.sleep(0.2)


def combat_damage(party1, party2, player):
    """Set damage to combatant1 in case, positions and chances align."""
    if party1.get_position() == party2.get_strike_dir():
        chance = party2.get_combatant().get_weapon().get_hit_chance()
        if random.choice(range(chance)) in range(10):
            print()
            print(
                f"{party1.get_combatant().get_name()} was hit and lost {party2.get_combatant().get_total_dmg()} health points.")
            party1.get_combatant().remove_health_points(party2.get_combatant().get_total_dmg())
            if party2 == player:
                party2.get_combatant().set_score(party2.get_combatant().get_total_dmg())
            print()
            party1.get_aar()
            party2.get_aar()
        else:
            print(
                f"{party2.get_combatant.get_name()}: *Struck {party2.get_strike_dir()}, but missed {party1.get_combatant.get_name()}*")
            print()


def retreat(combat):
    """Set thing in case of retreat from combat."""
    points = 10
    c = combat[0].get_combatant()
    if c is not None:
        c.remove_health_points(points)
        print(
            f"*{c.get_name()} takes damage {points} health points, while trying to retreat from combat.*")
        print(f"{c.get_name()}: {c.get_health()} points left.")
        c.set_location(c.get_old_location())
        combat[0].set_combatant(None)
        combat[1].set_combatant(None)
        combat[0].reset_turn_positions()
        combat[1].reset_turn_positions()


def combat_menu(combat):
    """Return combat menu with combat selections: dodge - left, right; attack - left, middle, right; retreat."""
    combat_selection = {
        "q": ["Exit Program", lambda: exit_program(combat[0].get_combatant())],
        "1": ["Attack left", lambda: combat[0].set_strike_dir("left")],
        "2": ["Attack right", lambda: combat[0].set_strike_dir("right")],
        "3": ["Attack middle", lambda: combat[0].set_strike_dir("middle")],
        "4": ["Dodge left", lambda: combat[0].set_position("left")],
        "5": ["Dodge right", lambda: combat[0].set_position("right")],
        "6": ["Dodge middle", lambda: combat[0].set_position("middle")],
        "r": ["Retreat", lambda: retreat(combat)]
    }
    return combat_selection


def npc_combat_menu(combat):
    """Return npc combat choices."""
    npc_combat = [
        ["Attack left", lambda: combat[1].set_strike_dir("left")],
        ["Attack right", lambda: combat[1].set_strike_dir("right")],
        ["Attack middle", lambda: combat[1].set_strike_dir("middle")],
        ["Dodge left", lambda: combat[1].set_position("left")],
        ["Dodge right", lambda: combat[1].set_position("right")],
        ["Dodge middle", lambda: combat[1].set_position("middle")],
    ]
    return npc_combat


def action_menu(combat):
    """Print out combat menu."""
    for action, text in combat_menu(combat).items():
        print(f"{action:^3} | {text[0]}")
        time.sleep(0.2)


def action_selection(combat):
    """Return player and npc selections."""
    player_selections, npc_moves = [], []
    action_menu(combat)
    for n in range(2):
        player_selection, npc_choice, action = selection(combat, n)
        if action == "r":
            return None, None
        npc_moves.append(npc_choice[1])
        player_selections.append(combat_menu(combat)[action][1])
    return player_selections, npc_moves


def selection(combat, n):
    """Return player and npc choice."""
    try:
        print()
        action = input(f"Select action {n + 1}: ")
        time.sleep(0.2)
        npc_choice = random.choice(npc_combat_menu(combat))
        player_selection = what_if_selection(combat, action)
        return player_selection, npc_choice, action
    except (KeyError, ValueError, IndexError):
        selection_exception()
        return selection(combat, n)


def what_if_selection(combat, action):
    """Return what if cases of selection."""
    player_selection = []
    if action == "q":
        combat_menu(combat)[action][1]()
    elif action == "r":
        combat_menu(combat)[action][1]()
    else:
        player_selection = combat_menu(combat)[action][1]
    return player_selection


def play_combat(combat, player, npc):
    """Run combat and return play_combat until combat is active, if player is dead, exit program,
    else return to navigation."""
    if player.check_if_dead():
        print("GAME OVER! YOU DIED!")
        exit_program(player)
    elif npc.check_if_dead():
        print(f"{npc.get_race()} {npc.get_name()} is dead.")
        return
    print()
    player_moves, npc_moves = action_selection(combat)
    if player_moves is None:
        return
    print()
    combat_loop(combat, player_moves, npc_moves)
    play_combat(combat, player, npc)


def combat_loop(combat, player_moves, npc_moves):
    """Run combat loop."""
    for i in [0, 1]:
        player_moves[i]()

        npc_moves[i]()
        combat_damage(combat[0], combat[1], combat[0])
        time.sleep(1)
        combat_damage(combat[1], combat[0], combat[0])
        after_action_settings(combat)
        time.sleep(1)


def after_action_settings(combat):
    """Set stats of paries and reset stances."""
    combat[0].get_combatant().add_strength()
    combat[1].get_combatant().add_strength()
    time.sleep(1)
    combat[0].reset_turn_positions()
    combat[1].reset_turn_positions()
