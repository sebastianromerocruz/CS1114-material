import TupleSort

DATUM_QUANTITY = 4
TITLE_IDX = 0
PLAYTIME_IDX = 2
OUTPUT_HEADER = "Title,Play Time (hrs)"


def parse_information(line):
    # Step 1: Strips and splits by commas, since it is a CSV
    lst = line.strip().split(',')

    # Step 2: Check if we have enough data to read. It's a potentially fatal error, so we raise a ValueError
    if len(lst) != DATUM_QUANTITY:
        raise ValueError("Line '{}' does not have enough values.".format(line))

    # Step 3: Read the value; this is a guaranteed to work because of step 2
    title = lst[TITLE_IDX]

    # Step 4: Attempt to convert the value into a float. Potentially fatal, so we raise a ValueError
    try:
        playtime = float(lst[PLAYTIME_IDX])
    except ValueError:
        raise ValueError("Playtime value in line '{}' is non-numerical".format(lst[PLAYTIME_IDX]))

    # Step 5: Return the information as a tuple
    return title, playtime


def get_library_contents(filepath):
    library = []

    # Step 1: Attempt to safely open our file, return empty list if file doesn't exist
    try:
        library_file = open(filepath, 'r')
    except FileNotFoundError:
        print("WARNING: File {} does not exist. Returning empty list.")
        return library

    # Step 2: Get rid of the header
    library_file.readline()

    # Step 3: Extract the information that we need from our file
    for line in library_file:
        information = parse_information(line)
        library.append(information)

    # Step 4: Close your file. Please.
    library_file.close()

    # Step 5: Return library information
    return library


def create_report(library_information, report_filename="report.csv"):
    # Step 1: Open the file.
    report_file = open(report_filename, 'w')

    # Step 2: Write the header into report_file using the print() function
    print(OUTPUT_HEADER, end='\n', file=report_file)

    # Step 3: Iterate through each of the tuples
    for game_information in library_information:
        # Step 4: Write the line into report_file using the print() function
        game_title = game_information[0]
        game_playtime = game_information[1]
        print(game_title, game_playtime, sep=',', end='\n', file=report_file)

    # Step 5: Close the file.
    report_file.close()


def main():
    library = get_library_contents(filepath="library.csv")
    TupleSort.tuple_sort(library, 1, True)
    create_report(library_information=library)


main()
