# Functions


# Asks users how many rounds they want to play
def check_rounds():
    while True:
        response = input("How many rounds: ")

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
def num_check(question, low):

    error = f"Please enter a whole number above {low}\n"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give error
            if low < response:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no", "y", "n"]
game_summary = []

# Error
y_n_error = "Please enter either yes or no"
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

# Lists

# Errrors
low_high_error = "Please choose an integer that is " \
                 "larger than low number"

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
    print()

    quit = input("Press <enter> to continue or 'xxx' to quit: ")
    if quit == "xxx":
        break

    low_num = num_check("Please choose the low number: : ", 0)

    high_num = num_check("Please choose the high number: ", low_num)





    if rounds_played == rounds:
        break