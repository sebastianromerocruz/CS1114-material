VG_DATA = "lectures/dictionaries/video_game_clean.csv"


def extract_data(filepath):
    """
    Will return a list of individual video game data (lists themselves) extracted from a multi-line file 
    containing data of multiple games.

    Args:
        filepath (str): the address of our data file

    Returns:
        list[list[str]]: a list of lists of string data
    """
    pass


def main():
    data = extract_data(VG_DATA)
    print(data[:10])  # print only first ten lines


main()
