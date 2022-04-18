import sys
import pprint

ARGUMENTS = sys.argv
DATA_IDX = 1
NAME_IDX, PLATFORM_IDX, YR_IDX, GENRE_IDX, PUB_IDX, DEV_IDX = 1, 2, 3, 4, 5, 15


def extract_data_into_list(filepath):
    data = []

    # Step 1: Attempt to safely open the file pointed to by filepath
    try:
        data_file = open(filepath, 'r')
    except FileNotFoundError:
        # Step 2: If the file doesn't exist, return our empty list
        return data

    # Step 3: If it does exist, iterate through each line, ignoring the header
    header = data_file.readline()
    lines = data_file.readlines()
    for line in lines:
        # Step 4: Prepare our list for data extraction; replacing those pesky " signs from each line
        datum_list = line.strip().replace('"', '').split(',')

        # Step 5: Create our data list
        datum = [
            datum_list[NAME_IDX],
            datum_list[PLATFORM_IDX],
            datum_list[YR_IDX],
            datum_list[GENRE_IDX],
            datum_list[PUB_IDX],
            datum_list[DEV_IDX]
        ]

        # Step 6: Append this data list to our main list
        data.append(datum)

    # Step 7: Close our file
    data_file.close()

    # Step 8: Return our whole data list
    return data


def extract_data_to_dict(filepath):
    data = {}

    # Step 1: Attempt to safely open the file pointed to by filepath
    try:
        data_file = open(filepath, 'r')
    except FileNotFoundError:
        # Step 2: If the file doesn't exist, return our empty list
        return data

    # Step 3: If it does exist, iterate through each line, ignoring the header
    for line in data_file.readlines()[1:]:
        # Step 4: Prepare our list for data extraction
        datum_list = line.strip().replace('"', '').split(',')

        # Step 5: Add dictionary entry to our data list
        key = datum_list[NAME_IDX]
        value = [
            datum_list[PLATFORM_IDX],
            datum_list[YR_IDX],
            datum_list[GENRE_IDX],
            datum_list[PUB_IDX],
            datum_list[DEV_IDX]
        ]

        # Step 6: If this entry doesn't already exist in our dictionary, add it
        if key not in data:
            data[key] = value

    # Step 7: Close our file
    data_file.close()

    # Step 8: Return our whole data list
    return data


def main():
    filepath = ARGUMENTS[DATA_IDX]
    data = extract_data_to_dict(filepath)
    pprint.pprint(data)
    pprint.pprint(data["Wii Play"])


if __name__ == '__main__':
    main()
