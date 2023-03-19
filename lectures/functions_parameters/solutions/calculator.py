ARITHMETIC_OPERATORS = "+-*/"
ADD_IDX = 0
SUB_IDX = 1
MUL_IDX = 2
DIV_IDX = 3
END_CODE = "DONE"
SHUTDOWN_CODE = 'n'


def add():
    # Asking user for input
    number_one = float(input("Enter a number: "))
    number_two = float(input("Enter another number: "))

    # Calculating the sum
    addition = number_one + number_two

    # Displaying result
    print("{} + {} = {}".format(number_one, number_two, addition))


def subtract():
    # Asking user for input
    number_one = float(input("Enter a number: "))
    number_two = float(input("Enter another number: "))

    # Calculating the difference
    difference = number_one - number_two

    # Displaying result
    print("{} - {} = {}".format(number_one, number_two, difference))


def multiply():
    # Asking user for input
    number_one = float(input("Enter a number: "))
    number_two = float(input("Enter another number: "))

    # Calculating the product
    product = number_one * number_two

    # Displaying result
    print("{} * {} = {}".format(number_one, number_two, product))


def divide():
    # Asking for input
    number_one = float(input("Enter a number: "))
    number_two = float(input("Enter another number: "))

    # Calculating the ratio, or division
    ratio = number_one / number_two

    # Displaying result
    print("{} / {} = {}".format(number_one, number_two, ratio))


def do_arithmetic():
    # Setting up out flag system
    is_operation_not_done = True

    while is_operation_not_done:
        user_operator = input("Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to "
                              "end. ")

        # If the user enters the end code ("DONE", stored in the constant END_CODE), turn the flag to False
        # and skip to the next iteration by using the continue keyword
        if user_operator == END_CODE:
            is_operation_not_done = False
            continue

        # If the user did not enter the end code, check which operation they want to do
        # If they didn't enter a valid operator, we give them an error message (line 83)
        if user_operator == ARITHMETIC_OPERATORS[ADD_IDX]:
            add()
        elif user_operator == ARITHMETIC_OPERATORS[SUB_IDX]:
            subtract()
        elif user_operator == ARITHMETIC_OPERATORS[MUL_IDX]:
            multiply()
        elif user_operator == ARITHMETIC_OPERATORS[DIV_IDX]:
            divide()
        else:
            print("ERROR: Please enter a valid operator (i.e. +, -, *, /).")


def main():
    print("Welcome to the S.E.B Calculator!")
    user_choice = input("Would you like to calculate (y), or shut down (n)? ")

    while user_choice != SHUTDOWN_CODE:
        do_arithmetic()
        user_choice = input("Would you like to continue operation? [y/n] ")


main()  # This line runs the entire program
