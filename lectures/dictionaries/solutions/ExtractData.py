VG_DATA = """ID,Name,Platform,Year_of_Release,Genre,Publisher,NA_players,EU_players,JP_players,Other_players,Global_players,Critic_Score,Critic_Count,User_Score,User_Count,Developer,Rating
1,Wii Sports,Wii,2006,Sports,Nintendo,41.36,28.96,3.77,8.45,82.53,76,51,8,322,Nintendo,E
2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24,NA,NA,,NA,,
3,Mario Kart Wii,Wii,2008,Racing,Nintendo,15.68,12.76,3.79,3.29,35.52,82,73,8.3,709,Nintendo,E
4,Wii Sports Resort,Wii,2009,Sports,Nintendo,15.61,10.93,3.28,2.95,32.77,80,73,8,192,Nintendo,E
5,Pokemon Red/Pokemon Blue,GB,1996,Role-Playing,Nintendo,11.27,8.89,10.22,1,31.37,NA,NA,,NA,,
6,Tetris,GB,1989,Puzzle,Nintendo,23.2,2.26,4.22,0.58,30.26,NA,NA,,NA,,
7,New Super Mario Bros.,DS,2006,Platform,Nintendo,11.28,9.14,6.5,2.88,29.8,89,65,8.5,431,Nintendo,E
8,Wii Play,Wii,2006,Misc,Nintendo,13.96,9.18,2.93,2.84,28.92,58,41,6.6,129,Nintendo,E
9,New Super Mario Bros. Wii,Wii,2009,Platform,Nintendo,14.44,6.94,4.7,2.24,28.32,87,80,8.4,594,Nintendo,E
10,Duck Hunt,NES,1984,Shooter,Nintendo,26.93,0.63,0.28,0.47,28.31,NA,NA,,NA,,"""

NAME_IDX, PLTFRM_IDX, YEAR_IDX, GENRE_IDX, PUB_IDX, DEV_IDX = 1, 2, 3, 4, 5, 15


def extract_data(data):
    """
    Will return a list of individual video game data (lists themselves) extracted from a multi-line string 
    containing data of multiple games.

    Args:
        data (str): a multi-line python string

    Returns:
        list[list[str]]: a list of lists of string data
    """
    extracted_data = []

    # Split the data by lines, since each line hold an individual game's data
    split_data = data.split('\n')

    # Start at the 1st line, not the 0th, since the 0th line is just the data header
    for game_data in split_data[1:]:

        # Split the game datum by commas
        split_datum = game_data.split(',')

        # Create a list out of it
        datum = [
            split_datum[NAME_IDX], split_datum[PLTFRM_IDX], split_datum[YEAR_IDX],
            split_datum[GENRE_IDX], split_datum[PUB_IDX], split_datum[DEV_IDX]
        ]

        # And append it to our "master list"
        extracted_data.append(datum)
    
    return extracted_data


def main():
    data = extract_data(VG_DATA)
    print(data)


main()
