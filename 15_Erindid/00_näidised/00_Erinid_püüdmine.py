"""try:
    # Try to to something, which may cause an error

except <Name of the error class>
    # If what you tried caused an error, this code block is executed
    # If the error was not thrown, this code block is ignored

finally:
    # This code block is executed anyway"""
some_word = "word"

try:
    # The ValueError is being thrown then executing this statement
    int(some_word)
    # After the error is thrown, the <except> code block is immediately executed
    print("This is not printed to the console")

# Catching the thrown error
except ValueError:
    print("This is printed to the console")

finally:
    print("This is printed anyway")