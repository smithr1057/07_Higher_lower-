import random
# Functions


# Asks users how many rounds they want to play
def check_rounds():
    while True:
        response = input("How many rounds: ")
        print()

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is to low print error and
                # restart the loop

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# checks user answers with valid answer
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Displays instructions
def instructions():
    print("**** How to Play ****")
    print()
    return ""


# Adds decorations to selected text
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


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

# List of valid responses
yes_no_list = ["yes", "no", "y", "n"]
game_summary = []

# Error
y_n_error = "Please enter either yes or no"
low_high_error = "Please choose an integer that is " \
                 "larger than low number"
# Title
statement_generator("Welcome to the Higher Lower Game", "*")
print()

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker("Have you played the game before? "
                               , yes_no_list,
                               y_n_error)

if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0
rounds_lost = 0
rounds_won = 0
num_guesses = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start the game play loop

    # Rounds Heading
    if rounds == "":
        heading = f"*** Continuous Mode: Round" \
                  f" {rounds_played + 1} ***"
    else:
        heading = f"*** Round {rounds_played + 1}" \
                  f" of {rounds} ***"

    print(heading)

    quit = input("Press <enter> to continue or 'xxx' to quit: ")
    if quit == "xxx":
        break

    low_num = int_check("Please choose the low number: : ", 0)

    high_num = int_check("Please choose the high number: ", low_num)

    sec_num = random.randint(low_num, high_num)
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
                num_guesses = + 1

            if user_guess > sec_num:
                print("To high, try again")
                num_guesses = + 1
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

        num_guesses = + 1
        rounds_won = + 1
        result = "Won"

    rounds_played = + 1
    print(f"You {result}")
    print()


    if rounds_played == rounds:
        break

