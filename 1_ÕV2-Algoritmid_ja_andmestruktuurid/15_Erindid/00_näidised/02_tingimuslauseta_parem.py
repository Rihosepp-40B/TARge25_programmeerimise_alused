games = ["Minecraft", "GTA V", "Soma", "Heavy Rain", "Fahrenheit", "Witcher 3", "Skyrim"]

input_index = input(f"Type the number (0-{len(games) - 1}) to get a game to play: ")

try:
    game = games[int(input_index)]
    print(f"And you should play '{game}'")
except ValueError:
    print("This is not a number!") # If the input value is not a number
except IndexError:
    print("This is not a valid number!") # If the input number is not a valid index