import math

# Loop Component for easy testing
for item in range(0, 4):

    # Ask user to choose low / high number
    low = int(input("Low: "))
    high = int(input("High: "))

    # Finds the max amount of guesses
    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    # Prints guesses
    print(f"Max Guesses : {max_guesses}")

    print()




