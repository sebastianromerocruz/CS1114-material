from pprint import pprint

KEY_IDX = 0
VALUE_IDX = 1
PREFERENCES = """Field,Preference
Colour,Bleu de France
Movie,Liz and the Blue Bird
Composer,Debussy
Writer,Marcel Proust
Programming Language,ASM 6502
City,Kyoto"""


def extract_preferences(data):
    """
    Extracts user preferences from a CSV file. Uses zeroth element in each line as key, and first element as value.
    Assumes all lines are valid entries. If file not found, returns an empty dictionary.

    :param filepath: Address of CSV file in string form
    :return: A dictionary of preferences
    """
    preferences = {}

    # Step 1: Split the data by the newline character
    data = data.split('\n')

    # Step 3: Iterate through every line in the file EXCEPT for the zeroth one (the header)
    for line in data[1:]:
        # Step 4: Prep the file for data extraction
        line = line.split(',')

        # Step 5: Extract data from line
        key, value = line[KEY_IDX], line[VALUE_IDX]

        # Step 6: Create new key-value pair
        preferences[key] = value

    # Step 7: Return dictionary of preferences
    return preferences


def main():
    preferences = extract_preferences(data=PREFERENCES)
    pprint(preferences)


main()
