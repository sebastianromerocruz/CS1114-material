<h2 align=center>Lecture 22</h2>

<h1 align=center>Midterm 2 Review</h1>

### 29 Brumaire, Year CCXXXI

***Song of the day***: _[**Milk**](https://youtu.be/IFXIjI1ZZQs) by The 1975 (2017)._

### Sections

1. [**Review**](#review)
2. [**Solution**](#solution)
	1. [**Strategy**](#strategy)
	2. [**Implementation**](#implementation)

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
```

### _Solution_

#### ***Strategy***

The key thing to think about here is the steps we have to take in order to _access the names of the cast members in both data structures_. For example, in order to access the names of the cast members in `CAST_SAMPLE`, we'd have to access each member of the list, and then use the key `"name"` to access the value:

```python
for cast_member in CAST_SAMPLE:
	cast_member_name = cast_member["name"]
	print(cast_member_name)
```

<sub>**Code Block 1**: Iterating through the cast sample. Love sequences.</sub>

Output:

```
Léa Seydoux
Adrien Brody
```

In the case of `MOVIES`, we'd need a way to _iterate through a dictionary_. For this, dictionary views are the ideal way to go. Let's use, for example, `items()`. In our case, the values of the dictionary are also dictionaries. Each of these nested dictionaries contain a key, `"cast"`, that maps to the cast list. That's our ticket forward:

```python
for movie_info in MOVIES.items():
	movie_title, info = movie_info

	print(movie_info["cast"])
```

<sub>**Code Block 2**: Iterating through a dictionary using the `items()` view. Keep in mind that you can do multiple variable assignment here because we are guaranteed that `movie_info` will only have two values—the key and the value.</sub>

Output:

```
['Owen Wilson', 'Benicio del Toro', 'Léa Seydoux', 'Adrien Brody', 'Frances McDormand', 'Timothée Chalamet', 'Lyna Khoudri', 'Jeffrey Wright', 'Stephen Park', 'Bill Murray']
['Ralph Fiennes', 'Tony Revolori', 'Adrien Brody', 'Willem Dafoe', 'Saoirse Ronan', 'Léa Seydoux']
['Jared Gilman', 'Kara Hayward', 'Bruce Willis', 'Edward Norton', 'Bill Murray']
['Gene Hackman', 'Anjelica Huston', 'Danny Glover', 'Ben Stiller', 'Luke Wilson', 'Gwyneth Paltrow', 'Bill Murray']
['The French Dispatch', 'The Grand Budapest Hotel']
```

So, it looks like we'll have to iterate through _both_ the cast sample _and_ the movie dictionary, meaning that we'll end up with a nested `for`-loop.

#### ***Implementation***

```python
def get_costarred(cast_sample, movies):
	# STEP 1: Since the problem is asking us to return a list of movie titles, let's initialise an empty list
    costarred_movies = []

	# STEP 2: Iterate through all the movies using the items() view
    for movie_info in movies.items():

		# STEP 3: Isolate the movie title and the info dictionary
        movie_title, info = movie_info

		# STEP 4: We want to keep a movie if all cast members starred in it; assume they all were
		is_costarred = True

		# STEP 5: To find out if any of them weren't, iterate through each cast member
        for cast_member in cast_sample:

			# STEP 6: And if a single one of them didn't star in this movie, we know it is not co-starred
            if cast_member['name'] not in info['cast']:
				is_costarred = False

		# STEP 7: Finally, append movie title to our list if is_costarred ended up being true
		if is_costarred:
			costarred_movies.append(movie_title)
    
	# STEP 8: For the love of everything, don't forget to return
    return costarred_movies
```

<sub>**Code Block 3**: Final [**implementation**](solutions/solution.py) of `get_costarred()`.</sub>