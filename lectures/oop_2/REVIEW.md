<h2 align=center>Lecture 24</h2>

<h1 align=center>Object-Oriented Programming</h1>

### 9 Frimaire, CCXXXI

***Song of the day***: _[**White Awakening**](https://youtu.be/YAFRdQ4lzBY) by Les Rallizes Dénudés (1960s)._

---

### Part 1: _OOP Review_

#### _The `__init__()` Method_

Create a **class** called **`Song`** that will be created by the user with the following attributes:

| **Attribute**       | **Type** |
|---------------------|----------|
| `song_title`        | _`str`_  |
| `artist`            | _`str`_  |
| `album`             | _`str`_  |
| `genre`             | _`str`_  |
| `length_in_seconds` | _`int`_  |

<sub>**Table 1**: Attributes passed in by the user to create a **`Song`** object.</sub>

See the following sample behavior below showing the creation of a **`Song`** object called `a_random_song`:

```python
a_random_song = Song("The Girls Are Alright!", "saya", "The Girls Are Alright! — EP", "Indie", 271)
```

In addition to these 5 variables, inside the **`Song`** class's **`__init__`**, define a 6th attribute called `play_count`. The user needn't pass this variable in, as all songs begin with a play count of 0. Once your **`__init__`** is properly implemented, your class should behave as follows:

```python
a_random_song = Song("The Girls Are Alright!", "saya", "The Girls Are Alright! — EP", "indie", 271)
print(a_random_song.song_title)
print(a_random_song.artist)
print(a_random_song.album)
print(a_random_song.genre)
print(a_random_song.length_in_seconds)
print(a_random_song.play_count)
```
Output:
```text
The Girls Are Alright!
saya
The Girls Are Alright! — EP
Indie
271
0
```

#### _The `play()` Method_

Then, then define a method called `play()`. Quite simply, when this method is called, object's `play_count` will be increased by 1. It does not accept any parameters:

```python
a_random_song = Song("The Girls Are Alright!", "saya", "The Girls Are Alright! — EP", "indie", 271)
num_of_plays = 10 
for time in range(num_of_plays):
    a_random_song.play()

print(a_random_song.play_count)
```
Output:
```text
10
```