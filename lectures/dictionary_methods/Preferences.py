from pprint import pprint

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
    pass


def main():
    preferences = extract_preferences(data=PREFERENCES)
    pprint(preferences)


main()
