# import the random module for random value generation
import random

# asking the user for their two numbers and immediately converting them into float values
number_one = float(input("Enter a number: "))
number_two = float(input("Enter another number: "))

# Generating a random number between and including 0 and 100
random_number = random.randrange(0, 101)

# # Printing the result
# print(0 <= number_one <= random_number and 0 <= number_two <= random_number or 0 <= number_one / number_two <= random_number)

condition_one   = 0 <= number_one / number_two <= random_number
condition_two   = 0 <= number_one <= random_number
condition_three = 0 <= number_two <= random_number

if condition_one:
    print("The ratio is between 0 and", random_number, "so the the expression evaluates to true.")
elif condition_two and condition_three:
    print("Both numbers are within 0 and", random_number, "so the the expression evaluates to true.")
else:
    print("Both conditions are not met.")