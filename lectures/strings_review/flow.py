"""
In what order will these print() statements execute?
"""


def function_three():
    print('C', end=' ')
    function_two()
    print('D', end=' ')


def function_two():
    print('B', end=' ')


def function_one():
    print('A', end=' ')
    function_three()
    print('F', end=' ')
    function_two()
    print('E', end=' ')


def main():
    print('G', end=' ')
    function_one()
    print('H', end=' ')


main()
print('J')
