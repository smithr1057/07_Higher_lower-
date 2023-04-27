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
    print()
    print("**** How to Play ****")
    print()
    print("Choose how many rounds you want to "
          "play (press <enter> for continuous mode)")
    print()
    print("Choose your lowest and highest number")
    print("Keep in mind this will stay with you for the rest of the game")
    print()
    print("You will have a set amount of guesses "
          "to get the correct number")
    print()
    print("You can enter 'xxx' at the start of any round to quit")
    print()
    print("You are able to see your game statistics after each game")
    print()
    print("At the end of the game you may choose to begin a new game")
    print()
    print("Good Luck :D")
    print()
    return ""


# Adds decorations to selected text
def statement_generator(statement, decoration, lines=None):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    # use 3 lines for headings / heavy decoration
    if lines == 3:
        new_statement = f"{top_bottom}\n{statement}\n{top_bottom}"

    else:
        # default is one single line
        new_statement = statement

    return new_statement


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


# Lets you change color of printed text easily
def color_text(text, color):
    # list of colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    # Prints text in specified color
    print(f"{colors[color]}{text}\033[0m")


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no"]

# Error
y_n_error = "Please enter either yes or no"
low_high_error = "Please choose an integer that is " \
                 "larger than low number"

# Prints title with decorations and color
title = statement_generator("Welcome to the Higher / Lower Game", "*", 3)
colour_title = color_text(title, 'cyan')

print()

# Ask user if they have played before
# If 'no', show instructions
played_before = choice_checker("Have you played the game before? "
                               , yes_no_list,
                               y_n_error)

if played_before == "no":
    instructions()

play_again = "yes"
while play_again == "yes":

    rounds_played = 0
    rounds_lost = 0
    rounds_won = 0

    game_summary = []
    guess_summary = []

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

        color_text(heading, 'yellow')

        quit_game = input("Press <enter> to continue or 'xxx' to quit: ")
        print()
        # if user enters 'xxx' game ends
        if quit_game == "xxx":
            break

        # choose the high and low number
        if rounds_played == 0:
            low_num = int_check("Please choose the low number:  ", 0)
            high_num = int_check("Please choose the high number: ", low_num)

        else:
            print(f"Number is between {low_num} and {high_num}")

        # Generates secret number
        sec_num = random.randint(low_num, high_num)
        print("spoiler alert", sec_num)
        already_guessed = []

        num_guesses = 0

        # Finds the max amount of guesses the user gets
        range = high_num - low_num + 1
        max_raw = math.log2(range)
        max_upped = math.ceil(max_raw)
        max_guesses = max_upped + 1

        guesses_left = max_guesses

        # loop until user guesses number or out of guesses
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
                      f" Please try again.\nYou *still* have"
                      f" {guesses_left} guesses left")
                continue

            guesses_left -= 1

            already_guessed.append(user_guess)

            # Compares user guess and secret number
            # respond if user is too low or to high
            if guesses_left >= 1:

                if user_guess < sec_num:
                    print("Too low, try again")

                elif user_guess > sec_num:
                    print("To high, try again")
                num_guesses += 1

            else:
                color_text(f"You lost, better luck next time", "red")
                rounds_lost += 1
                result = "lost"
                num_guesses += 1

        # Unique reply if user gets the number first try
        if user_guess == sec_num:
            if num_guesses == 1:
                color_text("Amazing!! You got the number first try :D", "green")

            else:
                win_statement = statement_generator(f"Congrats you got the number "
                                                    f"in {num_guesses} guesses", "*", 1)
                color_win_statement = color_text(win_statement, "green")

            rounds_won += 1
            result = "won"

        outcome = f"Round {rounds_played + 1}: You {result} with {num_guesses} guesses"

        game_summary.append(outcome)
        print()

        rounds_played += 1

        if rounds_played == rounds:
            break

    if rounds_played >= 1:
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
            game_history = statement_generator("Game History", "-", 3)
            color_game_history = color_text(game_history, 'cyan')

            for game in game_summary:
                print(game)

            print()

            # displays game stats with % values to the nearest whole number
            statement_generator("Game Statistics", "-", 3)
            color_text(f"Win: {rounds_won}, {percent_win:.0f}%", 'green')
            color_text(f"Loss: {rounds_lost}, {percent_lose:.0f}%", 'red')

    # Ask user if they want to play again
    print()
    play_again = choice_checker("Would you like to play again? "
                                , yes_no_list, y_n_error)

# If user hasn't played a round comment
# Don't give them the option of game history
if rounds_played < 1:
    print()
    print("Maybe play the game next time :)")
else:
    print()
    color_text("Thanks for playing the Higher / Lower Game :D", "blue")
