import random
import math
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
def statement_generator(statement, decoration, lines=None):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    # use 3 lines for headings / heavy decoration
    if lines == 3:
        print(top_bottom)
        print(statement)
        print(top_bottom)
    else:
        # default is one single line
        print(statement)

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
statement_generator("Welcome to the Higher Lower Game", "*", 3)
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
    print()
    if quit == "xxx":
        break

    if rounds_played == 0:
        low_num = int_check("Please choose the low number:  ", 0)
        high_num = int_check("Please choose the high number: ", low_num)

    else:
        print(f"Number is between {low_num} and {high_num}")

    sec_num = random.randint(low_num, high_num)
    already_guessed = []

    num_guesses = 0

    # Finds the max amount of guesses the user gets
    range = high_num - low_num + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1

    guesses_left = max_guesses


    user_guess = ""

    while user_guess != sec_num and guesses_left >= 1:

        if guesses_left == 0:
            continue

        # Print how many guesses user has left
        if guesses_left > 1:
            print(f"You have {guesses_left} guesses")

        elif guesses_left == 1:
            print(f"You have {guesses_left} guess")

        print()
        user_guess = int_check("Please enter your guess: ",
                               low_num, high_num)

        # checks that guess is not a duplicate
        if user_guess in already_guessed:
            print(f"You already guessed that number!"
                  f" Please try again. You *still* have"
                  f" {guesses_left} guesses left")
            continue

        guesses_left -= 1

        already_guessed.append(user_guess)


        # Compares user guess and secret number to
        # respond if user is to low or to high
        if guesses_left >= 1:

            if user_guess < sec_num:
                print("Too low, try again")
                num_guesses += 1

            if user_guess > sec_num:
                print("To high, try again")
                num_guesses += 1
        else:
            if user_guess < sec_num:
                print("Too low!")
                print("You lost, better luck next time")
                rounds_lost += 1
                num_guesses += 1

            elif user_guess < sec_num:
                print("Too high!")
                print("You lost, better luck next time")
                rounds_lost += 1
                num_guesses += 1
            result = "Lost"



    # Unique relpy if user gets the number first try
    if user_guess == sec_num:
        num_guesses += 1
        if guesses_left == max_guesses:
            print("Amazing!! You got the number first try :D")

        else:
            print(f"** Congrats you got the number "
                  f"in {num_guesses} guesses **")
        print()

        rounds_won += 1
        result = "Won"

    outcome = f"Round {rounds_played + 1}: {result}"
    game_summary.append(outcome)
    print()

    rounds_played += 1

    if rounds_played == rounds:
        break



if rounds_played > 1:
    # Ask user if they want to see their game history
    # if 'yes' show game history
    show_stats = choice_checker("Would you like to see your"
                                " end game history? "
                                , yes_no_list, y_n_error)

    # Calculate stats and print them out
    if show_stats == "yes":



        # Calculate game stat
        percent_win = rounds_won / rounds_played * 100
        percent_lose = rounds_lost / rounds_played * 100

        # Displays game history
        print()
        print("***** Game History *****")
        for game in game_summary:
            print(game)

        print()

        # displays game stats with % values to the nearest whole number
        print(" ***** Game Statistics *****")
        print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, "
              f"{percent_lose:.0f}%")


    print()
    print("Thanks for playing the higher lower game :D")


# If user hasn't played a round comment
# Don't give them the option of game history
elif rounds_played < 1:
    print("Maybe play the game next time :)")

