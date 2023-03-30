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



rounds_played = 5
rounds_lost = 3
rounds_won = 2

y_n_error = "Please enter either yes or no"
yes_no_list = ["yes", "no", "y", "n"]
game_summary = []

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