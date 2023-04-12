<h2>Lecture 19</h2>

<h1>Dictionary Methods and Iteration</h1>

### 18 Brumaire, Year CCXXXI

***Song of the day***: _[**Purple Rose Minuet**](https://youtu.be/A6bdVuHarKo) by Susumu Yokata (2005)._

### Part 1: _Review_

Alright, let's do a simple dictionary problem to review how they work. Let's pretend we have a short CSV file that saves our preferences in various fields. Again, for now, we'll store these contents inside of a multi-line string, since we haven't covered files yet:

```csv
Field,Preference
Colour,Bleu de France
Movie,Liz and the Blue Bird
Composer,Debussy
Writer,Marcel Proust
Programming Language,ASM 6502
City,Kyoto
```

```python
PREFERENCES = """Field,Preference
Colour,Bleu de France
Movie,Liz and the Blue Bird
Composer,Debussy
Writer,Marcel Proust
Programming Language,ASM 6502
City,Kyoto"""
```

_**Figure and Code Block 1**: Contents of file [**preferences.csv**](preferences.csv) and their multi-line Python string equivalent. Feel free to change it to your own preferences._

Write a function, `extract_preferences()`, that creates a dictionary which saves a key-value pair for each line. The zeroth element of each line should be used as the key, and the first should be used as the value. Once properly implemented, you should see the following happen:

```python
from pprint import pprint

PREFERENCES = """Field,Preference
Colour,Bleu de France
Movie,Liz and the Blue Bird
Composer,Debussy
Writer,Marcel Proust
Programming Language,ASM 6502
City,Kyoto"""


def main():
    preferences = extract_preferences(data=PREFERENCES)
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

You may assume that all data in the file, if opened, will be valid. Your function must accept the multi-line string as it's single parameter.