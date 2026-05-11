"""Navigation possibilities in location.
Selle osa eesmärk on luua mängijale navigatsiooni menüü osa vastavalt asukohale, ning kalkuleerida
liigumise korral uue asukoha andmed.
Siin osas demonstreerin: for tsüklit, sõnastiku ja järjendi kasutamist."""


def navigation_menu(player, worldmap, world_data):
    """Return navigation menu selection."""
    directions = possible_directions(player.get_location(), worldmap)
    actions = []
    for direction in directions:
        been_there = ""
        new_location = calculate_new_coordinates(direction, player.get_location())
        if new_location in player.get_all_visited_locations():
            been_there = " (visited before)(not inspected)"
            if world_data[new_location].get_inspected():
                been_there = " (visited before)"
        actions.append([f"Go {direction}{been_there}.", lambda path=direction: player.set_location(
            calculate_new_coordinates(path, player.get_location()))])
    return actions


def possible_directions(location, worldmap):
    """Return filtered possible directions from location. Possible directions are: north, east, south and west."""
    north_south = {"1": "north", f"{len(worldmap)}": "south"}
    east_west = {"1": "west", f"{len(worldmap["1"])}": "east"}
    directions = ["south", "north", "east", "west"]
    row = location.split("-")[0]
    if row in north_south:
        directions.remove(north_south[row])
    col = location.split("-")[1]
    if col in east_west:
        directions.remove(east_west[col])
    return directions


def calculate_new_coordinates(selection, location):
    """Return new coordinates depending on choice."""
    directions = {"south": 1, "north": -1, "east": 1, "west": -1}
    row, col = (int(location.split("-")[0]), int(location.split("-")[1]))
    if selection == "south" or selection == "north":
        row = row + directions[selection]
    else:
        col = col + directions[selection]
    return f"{row}-{col}"
