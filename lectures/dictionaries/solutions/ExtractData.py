NAME_IDX, PLTFRM_IDX, YEAR_IDX, GENRE_IDX, PUB_IDX, DEV_IDX = 1, 2, 3, 4, 5, 15


def extract_data(filepath):
    extracted_data = []

    # Attempt to safely open the file, and return empty list if unsuccessful
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        print(f"ERROR: Could not open file '{filepath}'")
        return extracted_data

    # Get rid of header
    file.readline()

    # Iterate through each line of file
    for game_data in file:

        # Split the game datum by commas
        split_datum = game_data.split(',')

        # Create a list out of it
        datum = [
            split_datum[NAME_IDX], split_datum[PLTFRM_IDX], split_datum[YEAR_IDX],
            split_datum[GENRE_IDX], split_datum[PUB_IDX], split_datum[DEV_IDX]
        ]

        # And append it to our "master list"
        extracted_data.append(datum)

    file.close()
    
    return extracted_data


def main():
    data = extract_data(VG_DATA)
    print(data[:10])  # print only first ten lines


main()
