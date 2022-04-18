"""
Sebastián Romero Cruz
CS 1114
Spring 2022
NYU Tandon School of Engineering
"""
from enum import Enum


class TouchType(Enum):
    """
    Represents the type of touch the user performs on a smartphone screen
    """
    SINGLE_TOUCH = 0
    SWIPE = 1
    DOUBLE_TAP = 2
    HOLD = 3


class SwipeDirection(Enum):
    """
    Represents the direction of swipe the user performs on a smartphone screen; NO_DIR for non-swipe touches
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NO_DIR = 4
