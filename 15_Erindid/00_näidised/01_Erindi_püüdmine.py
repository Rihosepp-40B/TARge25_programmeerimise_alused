black_box = ["fly", 42, 13, "bird", ["sub", "list"], "dinosaur", 24]

sum = 0

for element in black_box:
    try:
        # Try to add element to the sum
        sum += element

    except TypeError:
        # If it is not a number, print the message and continue the loop
        print(f"'{element}' is not a number!")

print(sum)