"""Other action possibilities in location.
Selle osa eesmärk on luua uued valikud olenevalt mängija asukohast. Siin demonstreerin lambda kasutamist järjendite
liitmist."""

from world import drop_weapon, take_weapon
from combat_actions import play_combat


def action_menu(player, world_data, combat):
    """Return list of other actions player can do out of combat."""
    location = player.get_location()
    location_inspection = inspect_location(player, location, world_data, combat)
    action = [
        ["Inspect your weapon.", lambda: player.get_weapon().inspect()],
        ["Check your stats.", lambda: player.get_stats()],
        ["Drop weapon.", lambda: drop_weapon(player, player, world_data)]
    ]
    action.extend(location_inspection)
    return action


def inspect_location(player, location, world_data, combat):
    """Return menu selection. Selection depends on if location is inspected."""
    location_inspection = []
    if world_data[location].get_inspected():
        npc = world_data[location].get_npc()
        if npc is not None:
            location_inspection.extend(actions_with_npc(npc[0], player, combat))
        weapons = world_data[location].get_weapons()
        if weapons is not None or weapons != []:
            for wpn in actions_with_weapons(player, weapons, world_data):
                location_inspection.append(wpn)
    else:
        location_inspection = [["Inspect location.", lambda: world_data[location].set_inspected()], ]
    return location_inspection


def actions_with_npc(npc, player, combat):
    """Return action menu with npc, out of combat."""
    npc_action = [
        [f"Inspect {npc.get_race()}", lambda c=npc: c.get_stats()],
        [f"Engage with {npc.get_race()}", lambda: setup_combat(combat, player, npc)]
    ]
    return npc_action


def actions_with_weapons(player, weapons, world_data):
    """Return action menu with weapons in location."""
    wpn_action = []
    if weapons is not None:
        for wpn in weapons:
            wpn_action.append([f"Inspect {wpn.get_weapon_type()}", lambda w=wpn: w.inspect()])
            wpn_action.append([f"Pick up {wpn.get_weapon_type()}", lambda w=wpn: take_weapon(player, w, world_data)])
    return wpn_action


def setup_combat(combat, player, npc):
    """Place characters into combat as combatants."""
    combat[0].set_combatant(player)
    combat[1].set_combatant(npc)
    play_combat(combat, player, npc)
