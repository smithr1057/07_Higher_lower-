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
    print("Enter how many rounds you would like to play.")
    print("Press <enter> for continuous mode.")
    print("You can quit at any time by typing in 'xxx'.")
    print("Choose rock, paper, scissors or r, p, s.")
    print("You can choose to see your end game summary at the end of the game.")
    print("Good luck and have fun :D")
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


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no", "y", "n"]
game_summary = []

# Error
error = "Please enter either yes or no"
# Title
statement_generator("Welcome to the Higher Lower Game", "*")
print()

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker("Have you played the game before? "
                               , yes_no_list,
                               error)

if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0

game_summary = []

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

    low_num = "Please choose the low number: "
    high_num = "Please choose the high number: "
    if low_num >= high_num:
        error
