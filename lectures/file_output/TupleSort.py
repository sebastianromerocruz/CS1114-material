"""
Sebastián Romero Cruz
CS 1114
Spring 2022
NYU Tandon School of Engineering
"""


def tuple_sort(tuple_list, sort_index, descending=True):
    """
    Based on https://stackoverflow.com/a/3121985. Sorts a list of tuples by the value of a certain index in place.

    :param tuple_list: A non-empty list of tuples
    :param sort_index: A desired int index; assumes valid index value
    :param descending: True if ascending order is desired, False if descending
    :return: tuple_list sorted in place
    """
    return tuple_list.sort(key=lambda tup: tup[sort_index], reverse=descending)
