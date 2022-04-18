import math
"""
Let's say I wanted to print the square, cube, and factorial of every EVEN number from 1 through 10. Here's how to do it
without the continue keyword.

LOWER_LIMIT = 1
UPPER_LIMIT = 11

for number in range(LOWER_LIMIT, UPPER_LIMIT):
    if number % 2 == 0:
        print("{}-squared is {}.".format(number, math.pow(number, 2)))
        print("{}-cubed is {}.".format(number, math.pow(number, 3)))
        print("{}! is {}".format(number, math.factorial(number)))

If you wanted to use the continue keyword, it would work as follows:
"""
LOWER_LIMIT = 1
UPPER_LIMIT = 11

for number in range(LOWER_LIMIT, UPPER_LIMIT):
    if number % 2 != 0:
        # That is, if the number is NOT even, skip (or continue) to the next iteration
        # and ignore everything inside the for-loop past line 24
        continue

    print("{}-squared is {}.".format(number, math.pow(number, 2)))
    print("{}-cubed is {}.".format(number, math.pow(number, 3)))
    print("{}! is {}".format(number, math.factorial(number)))

"""
This method of "skipping" numbers is useful for when you only want the loop to execute under a specific condition that 
you can check early in the loop. If it doesn't meet those conditions (in this case, divisibility by 2), it will continue
to the next iteration.
"""
