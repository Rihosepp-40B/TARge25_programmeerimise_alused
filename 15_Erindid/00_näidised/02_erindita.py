games = ["Minecraft", "GTA V", "Soma", "Heavy Rain", "Fahrenheit", "Witcher 3", "Skyrim"]

input_index = input(f"Type the number (0-{len(games) - 1}) to get a game to play: ")  # Ask for input number

game = games[int(input_index)]  # Get the element from list with the input index

print(f"And you should play '{game}'")