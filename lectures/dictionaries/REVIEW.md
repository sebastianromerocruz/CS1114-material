<h2>Lecture 18</h2>

<h1>Beyond Sequences: The Python Dictionary</h1>

### 17 Brumaire, Year CCXXXI

***Song of the day***: _[**House Of The Rising Sun**](https://youtu.be/OdO6HdO32_8) by Minoru Muraoka (1970)._

---

### Part 1: _A Sample Problem, for Motivation_

Let's start with a simple problem to illustrate the usefulness of the topic we're covering next. Let's say we have a 
[**file**](video_game_clean.csv) that contains information for a large number of video games:

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

_**Figure 1**: First ten lines of [**video_game.csv**](video_game.csv) ([**Source**](https://www.kaggle.com/juttugarakesh/video-game-data)). Cleaned up using [**cleanup.py**](cleanup.py)._

We'll get to reading data from files next week, but for now, let's pretend that this data is instead saved in a really (_really_) long multi-line string:

```python
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
10,Duck Hunt,NES,1984,Shooter,Nintendo,26.93,0.63,0.28,0.47,28.31,NA,NA,,NA,,
...
...
...
16717,Haitaka no Psychedelica,PSV,2016,Adventure,Idea Factory,0,0,0.01,0,0.01,NA,NA,,NA,,
16718,Spirits & Spells,GBA,2003,Platform,Wanadoo,0.01,0,0,0,0.01,NA,NA,,NA,,
16719,Winning Post 8 2016,PSV,2016,Simulation,Tecmo Koei,0,0,0.01,0,0.01,NA,NA,,NA,,"""
```

That is, each video game's data is separated in the string by a newline `'\n'` character, and each individual datum within each video game data is separated by a comma `','` character.

Write a function called `extract_data()` that accepts this string as its only parameter and **returns a list of 
each of these video games' information (as lists)**. The information we want to include will be:

- Name
- Platform
- Year of release
- Genre
- Publisher
- Developer

So, if our string only contained information on those first 10 video games, our output would be:

```python
[
    ['Wii Sports', 'Wii', '2006', 'Sports', 'Nintendo', 'Nintendo'],
    ['Super Mario Bros.', 'NES', '1985', 'Platform', 'Nintendo', ''],
    ['Mario Kart Wii', 'Wii', '2008', 'Racing', 'Nintendo', 'Nintendo'],
    ['Wii Sports Resort', 'Wii', '2009', 'Sports', 'Nintendo', 'Nintendo'],
    ['Pokemon Red/Pokemon Blue', 'GB', '1996', 'Role-Playing', 'Nintendo', ''],
    ['Tetris', 'GB', '1989', 'Puzzle', 'Nintendo', ''],
    ['New Super Mario Bros.', 'DS', '2006', 'Platform', 'Nintendo', 'Nintendo'],
    ['Wii Play', 'Wii', '2006', 'Misc', 'Nintendo', 'Nintendo'],
    ['New Super Mario Bros. Wii', 'Wii', '2009', 'Platform', 'Nintendo', 'Nintendo'],
    ['Duck Hunt', 'NES', '1984', 'Shooter', 'Nintendo', '']
]
```

You can use the list multi-line string included in [**ExtractData.py**](ExtractData.py) to get started.