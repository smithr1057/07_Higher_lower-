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


# Main Routine
low_num = 20
high_num = 50

random_num = random.randint(low_num, high_num)

num_guess = num_check("Please enter your guess: ", low_num, high_num)

if num_guess == random_num:
    print("Congrats you won")

else:
    print("try again")




