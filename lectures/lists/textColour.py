"""
Sebastián Romero Cruz
CS 1114
Spring 2022
NYU Tandon School of Engineering
"""


class TextColour:
    """
    Escape sequences for different colours
    """
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END_CODE = '\033[0m'


def colour(text: str, colour: str) -> str:
    """
    Returns a colour-coded version of `text`, depending on the inputted escape sequence.

    :param text: Any string
    :param colour: An colour escape sequence
    :return:
    """
    return "{}{}{}".format(colour, text, TextColour.END_CODE)


def main():
    print(colour("Hello", TextColour.RED))
    print(colour("Hello", TextColour.YELLOW))
    print(colour("Hello", TextColour.GREEN))


if __name__ == '__main__':
    main()