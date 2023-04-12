<h2 align=center>Lecture 18</h2>

<h1 align=center>Dictionary Methods and Iteration</h1>

### 22 Germinal, Year CCXXXI

***Song of the day***: _[**Purple Rose Minuet**](https://youtu.be/A6bdVuHarKo) by Susumu Yokata (2005)._

---

### Part 1: _Review_

Alright, let's do a simple dictionary problem to review how they work. Let's pretend we have a short CSV file that saves our preferences in various fields:

```csv
Field,Preference
Colour,Bleu de France
Movie,Liz and the Blue Bird
Composer,Debussy
Writer,Marcel Proust
Programming Language,ASM 6502
City,Kyoto
```

_**Figure and Code Block 1**: Contents of file [**preferences.csv**](preferences.csv) and their multi-line Python string equivalent. Feel free to change it to your own preferences._

Write a function, `extract_preferences()`, that accepts a preferences filepath as its sole parameter and creates a dictionary which saves a key-value pair for each line. The zeroth element of each line should be used as the key, and the first should be used as the value. Once properly implemented, you should see the following happen:

```python
from pprint import pprint

PREFERENCES = "preferences.csv"

def main():
    preferences = extract_preferences(filepath=PREFERENCES)
    pprint(preferences)

main()
```

Output:

```commandline
{'City': 'Kyoto',
 'Colour': 'Bleu de France',
 'Composer': 'Debussy',
 'Movie': 'Liz and the Blue Bird',
 'Programming Language': 'ASM 6502',
 'Writer': 'Marcel Proust'}
```

You may assume that all data in the file, if opened, will be valid.

---

[**Solution**](solution/Preferences.py):

```python
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
```

### Part 2: _Safe key lookup_

There are a couple of ways of safely getting the value corresponding to a key. We saw the `if` version
earlier:

```python
key = "band"

if key in preferences:
    value = preferences[key]
    print(f"This user's favourite {key} is '{value}'.")
else:
    print(f"This user does not have a favourite {key}.")
```

---

This is fine, but there is actually a way of doing something similar in one line using ***conditional
expressions***. This is my personal favourite way of doing this:

```python
key = "band"
value = preferences[key] if key in preferences else None
```

The second line reads as such in English:

> Inside the parameter `value`, save the value corresponding to the key `key` in the dictionary `preferences` **if** 
> `key`　exists **in** `preferences`. If not (`else`), save the value of `None` instead.

You need not necessarily use `None` as an alternative value. For example:

```python
key = "band"
value = preferences[key] if key in preferences else None

message = f"This user's favourite {key} is '{value}'." if value else f"This user does not have a favourite {key}."
print(message)
```

That is,

> If `value` is not `None`, save `f"This user's favourite {key} is '{}value'."` inside the variable `message`.
> If `value` is `None`, save the value `f"This user does not have a favourite {key}."` instead.

The reason why I personally like this method is because it is not **dictionary exclusive**; you can use conditional 
expressions just about anywhere in Python. I'll be using them a lot from now on, so make sure to get used to them!

---

A third way of doing this is by using the dictionary method `get()`. Get takes two parameters:

1. `key`: The key you are trying to search up.
2. `alt`: The value returned if the key does not exist in the dictionary. This is an optional variable, with a default
value of `None`.

```python
key = "band"
alternative = "NA"
value = preferences.get(key, alternative)

# With a specified alternative value
message = f"This user's favourite {key} is '{value}'." if value != "NA" else f"This user does not have a favourite {key}."
print(message)

# Using the default alternative value
value = preferences.get(key)
message = f"This user's favourite {key} is '{value}'." if value else f"This user does not have a favourite {key}."
print(message)
```

This is probably the simplest way to safely extracting values from a dictionary, but again, the `get()` method only 
exists for Python dictionaries, and not anywhere else.

### Part 2: Updating dictionaries

What is the user updated their preferences, changing some originals and adding new preferences?

```python
latest_update = {"Colour": "Royal Blue", "Band": "The 1975", "Movie": "The French Dispatch"}
```

What we ***cannot*** do is this:

```python
preferences = preferences + latest_update
```

Output:

```commandline
Traceback (most recent call last):
  File "Preferences.py", line 54, in <module>
    main()
  File "Preferences.py", line 50, in main
    preferences = preferences + latest_update
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
```

Instead, use the `update()` method:

```python
preferences.update(latest_update)

pprint(preferences)
```

Output:

```commandline
{'Band': 'The 1975',
 'City': 'Kyoto',
 'Colour': 'Royal Blue',
 'Composer': 'Debussy',
 'Movie': 'The French Dispatch',
 'Programming Language': 'Swift',
 'Writer': 'Sanaë Lemoine'}
```

So, this is basically the only safe way of quickly "adding" dictionaries together.

### Part 3: _Dictionary views_

I mentioned that dictionaries are non-sequential containers, and therefore cannot be iterated through the same way
lists, ranges, strings, and tuples can be:

```python
for key_value in preferences:
    print(key_value)
```

Output:

```commandline
Colour
Movie
Composer
Writer
Programming Language
City
```

While the code doesn't crash, we're clearly not getting the full key-value pair information; we only get back the 
keys—and not in any particular order. So how do we specify which information we want to iterate through? We use 
something called **views**.

```python
keys = preferences.keys()
pprint(keys)

values = preferences.values()
pprint(values)

key_values = preferences.items()
pprint(key_values)
```

Output:

```commandline
dict_keys([
    'Colour', 
    'Movie', 
    'Composer', 
    'Writer', 
    'Programming Language', 
    'City'
])
dict_values([
    'Bleu de France', 
    'Liz and the Blue Bird', 
    'Debussy', 
    'Sanaë Lemoine', 
    'Swift', 
    'Kyoto'
])
dict_items([
    ('Colour', 'Bleu de France'), 
    ('Movie', 'Liz and the Blue Bird'), 
    ('Composer', 'Debussy'), 
    ('Writer', 'Sanaë Lemoine'), 
    ('Programming Language', 'Swift'), 
    ('City', 'Kyoto')
])
```

These `dict_keys()`, `dict_values()`, and `dict_items()` objects are `view` objects. They are containers of the sequence
family that can be iterated in a similar fashion to lists:

```python
key_values = preferences.items()

 for key_value in key_values:
    print(key_value)
```

Output:

```commandline
('Colour', 'Bleu de France')
('Movie', 'Liz and the Blue Bird')
('Composer', 'Debussy')
('Writer', 'Sanaë Lemoine')
('Programming Language', 'Swift')
('City', 'Kyoto')
```

However, we cannot index a view object in the same way we can index a list, or a tuple:

```commandline
Traceback (most recent call last):
  File "Preferences.py", line 57, in <module>
    main()
  File "Preferences.py", line 53, in main
    print(key_values[0])
TypeError: 'dict_items' object is not subscriptable
```

So we must **explicitely cast them to a list or tuple in order to do this**:

```python
key_values = preferences.items()
key_values = tuple(key_values)
    
for index in range(len(key_values)):
    print(key_values[index])
```

Output:

```commandline
('Colour', 'Bleu de France')
('Movie', 'Liz and the Blue Bird')
('Composer', 'Debussy')
('Writer', 'Sanaë Lemoine')
('Programming Language', 'Swift')
('City', 'Kyoto')
```

---

### Part 4: _Dictionary traversal_

Let's use views in this sample problem: let's say we had the video game file from Monday:

```csv
ID,Name,Platform,Year_of_Release,Genre,Publisher,NA_players,EU_players,JP_players,Other_players,Global_players,Critic_Score,Critic_Count,User_Score,User_Count,Developer,Rating
1,Wii Sports,Wii,2006,Sports,Nintendo,41.36,28.96,3.77,8.45,82.53,76,51,8,322,Nintendo,E
2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24,NA,NA,,NA,,
3,Mario Kart Wii,Wii,2008,Racing,Nintendo,15.68,12.76,3.79,3.29,35.52,82,73,8.3,709,Nintendo,E
4,Wii Sports Resort,Wii,2009,Sports,Nintendo,15.61,10.93,3.28,2.95,32.77,80,73,8,192,Nintendo,E
5,Pokemon Red/Pokemon Blue,GB,1996,Role-Playing,Nintendo,11.27,8.89,10.22,1,31.37,NA,NA,,NA,,
6,Tetris,GB,1989,Puzzle,Nintendo,23.2,2.26,4.22,0.58,30.26,NA,NA,,NA,,
7,New Super Mario Bros.,DS,2006,Platform,Nintendo,11.28,9.14,6.5,2.88,29.8,89,65,8.5,431,Nintendo,E
8,Wii Play,Wii,2006,Misc,Nintendo,13.96,9.18,2.93,2.84,28.92,58,41,6.6,129,Nintendo,E
9,New Super Mario Bros. Wii,Wii,2009,Platform,Nintendo,14.44,6.94,4.7,2.24,28.32,87,80,8.4,594,Nintendo,E
10,Duck Hunt,NES,1984,Shooter,Nintendo,26.93,0.63,0.28,0.47,28.31,NA,NA,,NA,,
```

_**Figure 3**: The first eleven lines of [**video_game_clean.csv**](video_game_clean.csv)._

Using the `extract_data_into_list()` function from [**Monday's class**](ExtractData.py), how would we write a function
to get the names of all the games from a specific console? For instance, if your boss wanted the names of all the 
[**NES**](https://en.wikipedia.org/wiki/Nintendo_Entertainment_System) games, you would be able to do this:

```python
def main():
    game_data = extract_data_to_dict(filepath="video_game.csv")
    games = get_all_games_of_console(data=game_data, console_name="NES")

    pprint(games)

main()
```

Output:

```text
['Super Mario Bros.',
 'Duck Hunt',
 'Super Mario Bros. 3',
 'Super Mario Bros. 2',
 'The Legend of Zelda',
 'Zelda II: The Adventure of Link',
 'Teenage Mutant Ninja Turtles',
 'Excitebike',
 'Golf',
 'Dragon Warrior III',
 'Kung Fu',
 'Baseball',
 'Dragon Warrior IV',
 'World Class Track Meet',
 "Mike Tyson's Punch-Out!!",
 'Metroid',
 'Super Mario Bros.: The Lost Levels',
 'Dragon Warrior II',
 'Dragon Warrior',
 'Ice Hockey',
 'Pro Wrestling',
 'Mario Bros.',
 'Teenage Mutant Ninja Turtles II: The Arcade Game',
 'Pro Yakyuu Family Stadium',
 'Tennis',
 'Volleyball',
 'R.C. Pro-Am',
 'Mahjong',
 'Soccer',
 'Rad Racer',
 'Pinball',
 'Kid Icarus',
 "Kirby's Adventure",
 'Yoshi',
 "Disney's DuckTales",
 "Ghosts 'n Goblins",
 'Donkey Kong Classics',
 'Xevious',
 'F1 Race',
 'Mega Man 2',
 'Ninja Hattori Kun: Ninja wa Shuugyou Degogiru no Maki',
 'Ice Climber',
 'Nintendo World Cup',
 '4 Nin uchi Mahjong',
 "Pro Yakyuu Family Stadium '87",
 'Teenage Mutant Ninja Turtles III: The Manhattan Project',
 'Gradius',
 'Gyromite',
 "Hogan's Alley",
 'Dragon Ball: Daimaou Fukkatsu',
 'Gegege no Kitarou 2: Youkai Gundan no Chousen',
 'Castlevania',
 'TwinBee',
 'Ganbare Goemon! Karakuri Douchuu',
 "Disney's Chip 'n Dale: Rescue Rangers",
 "Pro Yakyuu Family Stadium '88",
 'Mega Man 3',
 'Doraemon',
 'Commando',
 'Donkey Kong Jr.',
 'Lode Runner',
 'Famicom Jump: Eiyuu Retsuden',
 'Popeye',
 'Tag Team Match M.U.S.C.L.E.',
 'Adventure Island',
 'Bomberman',
 '1942',
 'NES Open Tournament Golf',
 'Tetris 2',
 'Star Soldier',
 "Castlevania II: Simon's Quest",
 'Mega Man 4',
 'Balloon Fight',
 "Castlevania III: Dracula's Curse",
 'Final Fantasy',
 'Clu Clu Land',
 'Mega Man',
 'Mega Man 5',
 'Mappy',
 'The Mysterious Murasame Castle',
 'Mega Man 6',
 'Wrecking Crew',
 'Bomberman II',
 'Jurassic Park',
 'Tetris 2 + Bombliss',
 "Famista '91",
 "Famista '92",
 'Final Fantasy I & II',
 'Teenage Mutant Ninja Turtles: Tournament Fighters',
 'Adventures of Lolo']
```

I personally would approach this by using the `items()` method to extract both the key (i.e. the name of the video game)
and the value (i.e. the data that contains the console of the game) all at once:

```python
def get_all_games_of_console(data, console_name):
    games = []

    # Step 1: To iterate through both keys and values, we use the items() dictionary method
    for key_value in data.items():
        # Step 2: Since we know items() returns a tuple of the form (KEY,VALUE), we can extract both in one line
        game_name, game_data = key_value

        # Step 3: Append game name if and only if this game's console name is equal to the desired console and is unique
        if game_data[0] == console_name and game_name not in games:
            games.append(game_name)

    # Step 4: Return list
    return games
```

[**Here's**](DictionaryIteration.py) the finished implementation.