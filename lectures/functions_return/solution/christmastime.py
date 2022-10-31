"""
Author: Sebastián Romero Cruz
Fall 2022
NYU Tandon School of Engineering
"""
SPACE_CHR = ' '


def print_shifted_triangle(height, margin, symbol):
    """
    print a `height`-line triangle, filled with `symbol` characters, shifted to the right by a `margin` number of
    spaces. For example, an input of 3, 4, and '%' will yield the following triangle output:

           %
          %%%
         %%%%%

    :param height: An int value representing the number of "levels" in triangle
    :param margin: An int value representing distance from the screen's left margin
    :param symbol: A str value representing the character that will be use to draw triangle
    :return: None
    """
    for level_number in range(height, -1, -1):
        number_of_spaces = margin + level_number
        number_of_chars = 2 * (height - level_number) + 1

        print(SPACE_CHR * number_of_spaces + symbol * number_of_chars)


def print_pine_tree(levels, symbol):
    """
    Prints a sequence of levels-number of triangles of increasing sizes, forming a "pine tree". The triangles will be
    drawn using the symbol character.

    :param levels: An int value representing the number of triangles in "pine tree"
    :param symbol: A str value representing the character that will be use to draw triangle
    :return: None
    """
    for level_number in range(1, levels + 1):
        print_shifted_triangle(level_number, levels - level_number, symbol)


def main():
    user_levels = int(input("Enter a positive, non-zero, integer: "))
    while user_levels <= 0:
        user_levels = int(input("Enter a positive, non-zero, integer: "))

    user_character = input("Enter a non-whitespace, non-alphanumeric character: ")
    while user_character.isalnum() or user_character.isspace():
        user_character = input("Enter a non-whitespace, non-alphanumeric character: ")

    print_pine_tree(user_levels, user_character)


# main()
