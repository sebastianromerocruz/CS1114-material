<h2 align=center>Lecture 22</h2>

<h1 align=center>Midterm 2 Review</h1>

### 29 Brumaire, Year CCXXXI

***Song of the day***: _[**Milk**](https://youtu.be/IFXIjI1ZZQs) by The 1975 (2017)._

### _Review_

Wed Anderson films are know, among [**other things**](https://youtu.be/ba3c9KEuQ4A), are known for their reoccurring cast members—that is, he likes to work with a specific group of actresses and actors, so they often appear as difference characters in each of his movies. Let's say we wanted to learn in which movies two specific actresses/actors have co-starred in. Let's say we have the following two constants defined at the top of your file:

```python
CAST_SAMPLE = [{"id": 11111, "name": "Léa Seydoux"}, {"id": 11112, "name": "Adrien Brody"}]
MOVIES = {
    "The French Dispatch": {
        "genre": "Anthology / Comedy", 
        "cast": ["Owen Wilson", "Benicio del Toro", "Léa Seydoux", "Adrien Brody", "Frances McDormand", "Timothée Chalamet", "Lyna Khoudri", "Jeffrey Wright", "Stephen Park", "Bill Murray"] 
    },
    "The Grand Budapest Hotel": {
        "genre": "Comedy / Drama",
        "cast": ["Ralph Fiennes", "Tony Revolori", "Adrien Brody", "Willem Dafoe", "Saoirse Ronan", "Léa Seydoux"]
    },
    'Moonrise Kingdom': {
        "genre": "Coming of Age / Comedy / Drama",
        "cast": ["Jared Gilman", "Kara Hayward", "Bruce Willis", "Edward Norton", "Bill Murray"]
    },
    "The Royal Tenenbaums": {
        "genre": "Comedy / Drama",
        "cast": ["Gene Hackman", "Anjelica Huston", "Danny Glover", "Ben Stiller", "Luke Wilson", "Gwyneth Paltrow", "Bill Murray"]
    }
}
```
Given this information, write a function `get_costarred()` (_sig. `list, dict, –> list[str]`_) that accepts the list of actors (`CAST_SAMPLE`) and a dictionary of movie information (`MOVIES`) as arguments and returns a list of movie titles where both cast members star together.

Sample behaviour:

```python
print(get_costarred(ACTORS_LIST, MOVIES_DICT))
```

Output:

```
['The French Dispatch', 'The Grand Budapest Hotel']