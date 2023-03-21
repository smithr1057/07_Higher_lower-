# Functions

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

low_num = num_check("Please choose the low number: : ", 0)

high_num = num_check("Please choose the high number: ", low_num)


