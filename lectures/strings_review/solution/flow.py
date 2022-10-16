"""
In what order will these print() statements execute?

Correct answer:
G A C B D F B E H J
"""


# All of the following are definitions only, so they don't run code
# First line to actually execute is line 39
def function_three():
    print('C', end=' ')  # 3
    function_two()  # Go to function_two() definition
    print('D', end=' ')  # 5
    """Return to where function_three() was executed (i.e. function_one())"""


def function_two():
    print('B', end=' ')  # 4; 7
    """Return to where function_two() was executed (i.e. function_three())"""


def function_one():
    print('A', end=' ')  # 2
    function_three()  # Go to function_three() definition
    print('F', end=' ')  # 6
    function_two()  # Go to function_two() definition
    print('E', end=' ')  # 8
    """Return to where function_one() was executed (i.e. main())"""


def main():
    print('G', end=' ')  # 1
    function_one()  # Go to function_one() definition
    print('H', end=' ')  # 9
    """Return to where main() was executed (i.e. line 39)"""


main()  # This is the first line to be executed; go to main() definition
print('J')  # 10
"""END OF PROGRAM"""
