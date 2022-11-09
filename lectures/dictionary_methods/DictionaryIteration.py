from pprint import pprint
from ExtractData import extract_data_to_dict


def get_all_games_of_console(data, console_name):
    """
    Given a dictionary of video game data, extracts all of the video games that were released for the desired console
    and returns their names as a list.

    :param data: A dictionary of games of the format {GAME_NAME: [GAME_DATA]}
    :param console_name: The name of a video game console
    :return: A list of video game names
    """
    games = []

    # Step 1: To iterate through both keys and values, we use the items() dictionary method
    for key_value in data.items():
        # Step 2: Since we know items() returns a tuple of the form (KEY, VALUE), we can extract both in one line
        game_name, game_data = key_value

        # Step 3: Append game name if and only if this game's console name is equal to the desired console and is unique
        if game_data[0] == console_name and game_name not in games:
            games.append(game_name)

    # Step 4: Return list
    return games


def main():
    filepath = "video_game.csv"
    console = "NES"
    game_data = extract_data_to_dict(filepath)
    games = get_all_games_of_console(game_data, console)

    pprint(games)


main()
