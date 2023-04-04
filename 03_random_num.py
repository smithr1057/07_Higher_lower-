# Functions
import random


# checks users enter an integer between a low and high number
def num_check(question, low, high):

    error = f"Please enter a whole number between {low} and {high}\n"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give error
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


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
end_game = "no"
while end_game == "no":
    low_num = int_check("Please choose the low number: ", 1)
    high_num = int_check("Please choose the high number: ", low_num)

    sec_num = random.randint(low_num, high_num)

    num_guess = num_check("Please enter your guess: ", low_num, high_num)
    print(sec_num)
    if num_guess == sec_num:
        print("Congrats you won")

    else:
        print("try again")




