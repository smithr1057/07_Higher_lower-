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
sec_num = 7
guesses_allowed = 5
low_num = 1
high_num = 50
num_guesses = 0

already_guessed = []
guesses_left = guesses_allowed
num_won = 0
user_guess = ""

while user_guess != sec_num and guesses_left >= 1:

    user_guess = int_check("Please enter your guess: ",
                           low_num, high_num)

    # checks that guess is not a duplicate
    if user_guess in already_guessed:
        print(f"You already guessed that number! Please try again. You *still* have {guesses_left} guesses left")
        continue

    guesses_left -= 1
    already_guessed.append(user_guess)

    if guesses_left >= 1:

        if user_guess < sec_num:
            print("Too low, try again")
            num_guesses =+ 1

        if user_guess > sec_num:
            print("To high, try again")
            num_guesses =+ 1
    else:
        if user_guess < sec_num:
            print("Too low!")
        elif user_guess < sec_num:
            print("Too high!")

if user_guess == sec_num:
    if guesses_left == guesses_allowed:
        print("Amazing!! You got the number first try :D")

    else:
        print("Well done, you got the number :)")

    num_guesses =+ 1
    rounds_won =+ 1
    result = "Won"

print(f"You got the number in {num_guesses} guesses")