"""tingimuslausega võib tulla palju koodi ja raskesti loetav"""

games = ["Minecraft", "GTA V", "Soma", "Heavy Rain", "Fahrenheit", "Witcher 3", "Skyrim"]

input_index = input(f"Type the number (0-{len(games) - 1}) to get a game to play: ")  # Ask for input number

# If input value is not a number
if not input_index.isdigit():
    print("This is not a number!")
    raise SystemExit  # Need to raise SystemExit for our program to stop

# If the input value is not a valid index
if int(input_index) > len(games) - 1 or int(input_index) < 0:
    print("This is not a valid index!")
    raise SystemExit

# If we have not raised SystemExit before, we will face the error anyway
game = games[int(input_index)]  # Get the element from list with the input index

print(f"And you should play '{game}'")