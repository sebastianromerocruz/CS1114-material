from ast import In
import random

QUIT_SIGNAL = 'q'

# Initialise the game
print("|————————WELCOME TO THE NUMBER GUESSING GAME————————|")
upper_limit = int(input("> ENTER THE UPPER LIMIT OF THE GENERATED NUMBERS (must be higher than 0): "))
tolerance = float(input("> ENTER THE TOLERANCE OF YOUR ANSWER: "))

while upper_limit <= 0:
    upper_limit = int(input("> ENTER THE UPPER LIMIT OF THE CORRECT ANSWER (must be higher 0): "))

input("> READY? (press any key to begin) ")

# Game loop
user_input = ""

while user_input != QUIT_SIGNAL:
    # Actual run of the game
    summation = 0
    user_input = int(input("> HOW MANY NUMBERS WOULD YOU LIKE TO AVERAGE? "))

    for number in range(user_input):
        random_number = random.randrange(1, upper_limit)
        summation += random_number
        print("> ADDING " + str(random_number) + " TO THE SUM...")
    
    answer = summation / float(user_input)
    user_input = float(input("> WHAT IS THE AVERAGE OF THESE " + str(user_input) + " NUMBERS? "))

    while answer - tolerance > user_input or answer + tolerance < user_input:
        print("> INCORRECT!")
        user_input = float(input("> WHAT IS THE AVERAGE OF THESE " + str(user_input) + " NUMBERS? "))
    
    user_input = input("CORRECT! THE EXACT ANSWER WAS " + str(answer) + ". WOULD YOU LIKE TO PLAY AGAIN? (press any key for yes, 'q' for no) ")

print("GAME OVER.")
