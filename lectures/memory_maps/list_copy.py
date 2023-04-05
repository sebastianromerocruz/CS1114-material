from random import randrange, shuffle
from copy import deepcopy

NUMBER_OF_ELEMENTS = 10
RANDOM_LIMIT = 100


def get_list_copy(lst, is_separate_copy=True):
    """
    Returns either an entirely new list with the same elements as lst, or the same exact list as lst.

    :param lst: A list of elements
    :param is_separate_copy: A bool representing whether we want a copy of the list returned or not
    :return: A list of elements
    """
    if not is_separate_copy:
        return lst

    copy = deepcopy(lst)

    return copy


def main():
    sample_list = []

    for index in range(NUMBER_OF_ELEMENTS):
        sample_list.append(randrange(RANDOM_LIMIT + 1))

    copy_a = get_list_copy(sample_list, False)
    copy_b = get_list_copy(sample_list, True)

    print("Shuffling original list...", end="\n\n")
    shuffle(sample_list)

    print("Sample list:   {}".format(sample_list))
    print("Copy A (same): {}".format(copy_a))
    print("Copy B (copy): {}".format(copy_b))

    original = [1, 2, 3]
    copy = get_list_copy(original, True)

    print("original's ID: {}".format(id(original)))
    print("copy's ID:     {}".format(id(copy)))


main()
