# Functions

# checks users enter an integer between a low and high number
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # Checks input is not too high or
            # too low if a both upper and
            # lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between "
                          f"{low} and {high}")
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more"
                          f"than (or equal to) {low}")
                    continue

            return response

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine
sec_num = 50
low_num = 1
high_num = 100


result = "wrong"
while result == "wrong":

    user_guess = int_check("Please enter your guess: ", low_num, high_num)

    if user_guess < sec_num:
        print("Higher")
        num_guesses = + 1

    if user_guess > sec_num:
        print("Lower")
        num_guesses = + 1

    if user_guess == sec_num:
        num_guesses = + 1
        rounds_won = + 1
        result = "Won"
        continue


rounds_played = + 1
print(f"You {result}")
print()


