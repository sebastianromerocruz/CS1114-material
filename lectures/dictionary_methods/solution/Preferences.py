from pprint import pprint

PREFERENCES = "lectures/dictionary_methods/preferences.csv"
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

    # Step 1: Safely open our file–return empty dictionary if unsuccessful
    try:
        data_file = open(filepath, 'r')
    except FileNotFoundError:
        print(f"WARNING: Could not open file '{preferences}'. Returning empty dictionary.")
        return preferences

    data_file.readline()  # header

    # Step 3: Iterate through every line in the file EXCEPT for the zeroth one (the header)
    for line in data_file:
        # Step 4: Prep the file for data extraction
        line = line.strip().split(',')

        # Step 5: Extract data from line
        key, value = line[KEY_IDX], line[VALUE_IDX]

        # Step 6: Create new key-value pair
        preferences[key] = value

    # Step 7: Return dictionary of preferences
    return preferences


def main():
    preferences = extract_preferences(filepath=PREFERENCES)
    pprint(preferences)


main()
