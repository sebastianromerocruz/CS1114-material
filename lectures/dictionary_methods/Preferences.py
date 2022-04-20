from sys import argv
from pprint import pprint

FILEPATH_IDX = 1
FILEPATH = argv[FILEPATH_IDX]
KEY_IDX = 0
VALUE_IDX = 1


def extract_preferences(filepath):
    """
    Extracts user preferences from a CSV file. Uses zeroth element in each line as key, and first element as value.
    Assumes all lines are valid entries. If file not found, returns an empty dictionary.

    :param filepath: Address of CSV file in string form
    :return: A dictionary of preferences
    """
    preferences = {}

    # Step 1: Attempt to safely open the file under read mode
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        # Step 2: If file doesn't exist, return an empty dictionary
        print("WARNING: File '{}' not found. Returning empty dictionary.".format(filepath))
        return preferences

    # Step 3: Iterate through every line in the file EXCEPT for the zeroth one (the header)
    for line in file.readlines()[1:]:
        # Step 4: Prep the file for data extraction
        line = line.strip().split(',')

        # Step 5: Extract data from line
        key, value = line[KEY_IDX], line[VALUE_IDX]

        # Step 6: Create new key-value pair
        preferences[key] = value

    # Step 7: Close file
    file.close()

    # Step 8: Return dictionary of preferences
    return preferences


def main():
    preferences = extract_preferences(filepath=FILEPATH)
    pprint(preferences)


if __name__ == '__main__':
    main()