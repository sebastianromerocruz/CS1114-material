from textColour import TextColour, colour
from random import randrange
from math import ceil

GREEN = TextColour.GREEN
YELLOW = TextColour.YELLOW
RED = TextColour.RED
MIN_HEALTH = 0
MAX_HEALTH = 100
SCALE_FACTOR = int(MAX_HEALTH / 5)
HEALTH_BIT = '='


def get_health_bar_length(current_health):
    """
    Calculates the amount of health bits that should be printed in proportion to the clamp factor. Numbers round up.

    :param current_health: An integer representing the user's current health
    :return: An integer representing an amount of health bits
    """
    health_bar_length = ceil(current_health / MAX_HEALTH * SCALE_FACTOR)
    return health_bar_length


def get_health_bar(health):
    """
    Creates a string representing a user's health bar, displaying a proportionate amount of "health bits" to the user's
    health.

    :param health: An integer representing the user's current health
    :return: A health bar string
    """
    health_bar_length = get_health_bar_length(health)
    num_of_empty_bits = SCALE_FACTOR - health_bar_length
    return "[{}{}]".format(HEALTH_BIT * health_bar_length, ' ' * num_of_empty_bits)


def get_colour_coded_string(health, string):
    """
    Returns a colour-coded string according to the user's health. Assumes positive value for health.

        0 - 33: Red
        34 - 66: Yellow
        67 - 100: Green

    :param health: An integer representing the user's current health
    :param string: A UI-related string (i.e. health bar, etc.)
    :return: A colour-coded string
    """
    if 0 <= health <= 33:
        return colour(string, RED)
    elif 34 <= health <= 66:
        return colour(string, YELLOW)
    else:
        return colour(string, GREEN)


def display_health(health):
    """
    Prints both a numerical and a visual, colour-coded representation of the user's health.

    :param health: An integer representing the user's current health
    :return: None
    """
    health_num_string = "HP: {} / {}".format(health, MAX_HEALTH)
    health_bar_string = get_health_bar(health)

    print(get_colour_coded_string(health, health_num_string))
    print(get_colour_coded_string(health, health_bar_string))


def main():
    display_health(92)
    display_health(54)
    display_health(6)
    curr_health = randrange(MIN_HEALTH, MAX_HEALTH)
    display_health(curr_health)


main()
