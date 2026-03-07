user_input = input("Please input a word: ")

# If the input is a number
if user_input.isdigit():
    raise ValueError("This is not a word!") # Throw an error with specified message

# This will never be printed in case of error
print(f"The word is '{user_input}'")