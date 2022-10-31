## Lecture 16

# Python Lists

### 9 Brumaire, Year CCXXXI

***Song of the day:*** _[**ひとりぼっち東京 (Lonesome Tokyo)**](https://youtu.be/MSnLgdQFk1c) by Kessoku Band (2022)._

### Sections

1. [**Background**](#background)
2. [**Your Starting Code**](#your-starting-code)
3. [**The `get_health_bar_length()` Function**](#the-get_health_bar_length-function)
4. [**The `get_health_bar()` Function**](#the-get_health_bar-function)
5. [**The `get_colour_coded_string()` Function**](#the-get_colour_coded_string-function)
6. [**The `diplay_health()` Function**](#the-display_health-function)

## _Parameters and `return` review_

### _Background_

Health points (HP) are one of the most important and ubiquitous elements of tabletop and video games, representing the
amount of damage a user or a player can take before they lose a life or lose consciousness. Being as important as it is
displaying a user's health in a way that is simple and effective is an important part of a video game's UI.

A [**health bar**](https://en.wikipedia.org/wiki/Health_(game_terminology)#/media/File:Video_game_health_bar.svg) is one
of the many ways to represent a player's health in video games. For example, we could "draw" a simple one in our shell
/ terminal by doing the following:

```text
HP: 65 / 100
[=======   ]
```

<sub>**Figure 1**: A simple health bar, where the `'='` character represents one of the 10 "health bits" a player can 
have. Notice that each health bit here represents 10 HP.</sub>

This helps the player a ton with knowing how much health they have left, since just seeing the string `65 / 100` might
lead the to believe that they have less (or more) health than they actually do; in general, visual representations are
much more effective than numerical ones.

Another way of improving your UX experience is by adding colour to your UI. For example, if the user has a "high" amount
of health, the health UI could be drawn in <span style="color:green; font-weight: bold">green</span>, whereas when the
player has a critically low amount of health, it could be drawn in 
<span style="color:red; font-weight: bold">red</span>. We will be creating a program that executes both effects by 
breaking our code down into simple, short functions.

<sub>**NOTE**: If you're using IDLE, the colour feature might unfortunately not work. I will show examples below of how
colouring appears in IDLE so that you know if what you are coding up is correct. Running this on any kind of terminal,
including PyCharm's, should actually display colour.</sub>

### _Your starting code_

In the [**display_health.py**](display_health.py) file, I have included the following lines of code to get you started:

```python
from textColour import TextColour, colour
from random import randrange

GREEN = TextColour.GREEN
YELLOW = TextColour.YELLOW
RED = TextColour.RED
MIN_HEALTH = 0
MAX_HEALTH = 100

"""
WRITE YOUR FUNCTIONS BELOW
"""



"""
WRITE YOUR FUNCTIONS ABOVE
"""

def main():
    curr_health = randrange(MIN_HEALTH, MAX_HEALTH)
    # display_health(curr_health)  # uncomment to test


main()
```

<sub>**Code Block 1**: Your starting code. Since the `display_health()` function has yet to be defined, I have commented
its invocation out inside the `main()` function. Feel free to uncomment it when you are ready to test it.</sub>

As usual, you do not need to worry about how any unfamiliar modules and constants work, just know that:

- The `colour()` function **accepts** an `str` and a `TextColour` (i.e. `GREEN`, `YELLOW`, and `RED`) as its two 
position arguments, and **returns** the contents of that string in the colour that was passed.

```python
text = "Hello, world!"
print(colour(text, YELLOW))
```

Output:

> <span style="color:yellow; font-family:Courier">Hello, world!</span>

- `GREEN`, `YELLOW`, `RED` are `TextColour` objects that you can pass into the `colour()` function as arguments.
- `MIN_HEALTH` and `MAX_HEALTH` are, as their names imply, the minimum and maximum health our players will have.

Note that you **must** have the [**textColour.py**](textColour.py) file in the same directory in order for this program 
to work.

Please don't hesitate to raise your hand if you have any questions about how these work!

### _The `get_health_bar_length()` function_

Write a function `get_health_bar_length()` that accepts a single parameter: `health`, an integer that represents the 
user's current health. The same way we scaled `65 / 100` to seven health bits in **figure 1**, we will be scaling our 
own health bar. The only difference here is that, instead of scaling by a factor of 10, we will be scaling by a factor
of 5 (that is, our health bar will measure one fifth of the user's current health).

Sample executions (feel free to pose these examples in your `main()` to test):

```python
print(get_health_bar_length(100))
print(get_health_bar_length(67))
print(get_health_bar_length(44))
print(get_health_bar_length(29))
print(get_health_bar_length(2))
```

Output:

```text
20
14
9
6
1
```

Note that the amount of health bits are being **rounded** up, so that a player with `2` HP will still display one 
remaining health bit.

### _The `get_health_bar()` function_

Your next function will accept one parameter: `health`, also an integer that represents the user's current health. This
function will return a string that contains a health bar similar to the one in **figure 1**. You must, of course, use 
`get_health_bar_length()` inside of it in order to determine how many health bits it will contain. You should use the
`'['` and `']'` characters to represent the beginning and end of the bar, and the `'='` character to represent a health
bit.

Sample executions:

```python
print(get_health_bar(100))
print(get_health_bar(67))
print(get_health_bar(44))
print(get_health_bar(29))
print(get_health_bar(2))
```

Output:

```text
[====================]
[==============      ]
[=========           ]
[======              ]
[=                   ]
```

Notice that the second "section" of the health bar is shown as being "depleted" by using a space character `' '` instead
of a `'='`; every health bar returned by `get_health_bar()` must be the same length.

---

#### _The `get_colour_coded_string()` function_

This function will accept two position parameters:

- `health`: An integer representing the user's current health.
- `string`: A UI-related string (i.e. health bar, etc.)

And will return a colour-coded equivalent of the same `string` according to the player's current HP (all ranges are
inclusive on both ends):

- **`0` - `33`**: <span style="color:red; font-weight:bold">red</span>
- **`34` - `66`**: <span style="color:yellow; font-weight:bold">yellow</span>
- **`67` - `100`**:  <span style="color:green; font-weight:bold">green</span>

Sample executions:

```python
print(get_colour_coded_string(100, "Status"))
print(get_colour_coded_string(67, "Status"))
print(get_colour_coded_string(44, "Status"))
print(get_colour_coded_string(29, "Status"))
print(get_colour_coded_string(2, "Status"))
```

Output:

> <span style="color:green; font-family:Courier">Status</span>

> <span style="color:green; font-family:Courier">Status</span>

> <span style="color:yellow; font-family:Courier">Status</span>

> <span style="color:red; font-family:Courier">Status</span>

> <span style="color:red; font-family:Courier">Status</span>

Naturally, you will have to  make use of the `colour()` function included in your file here.

**NOTE**: If you're using IDLE, you might get the following output instead:

```text
[92mStatus[0m
[92mStatus[0m
[93mStatus[0m
[91mStatus[0m
[91mStatus[0m
```

This is unfortunate, but just know that if you see the strings `[92m` (for green), `[93m` (for yellow), and 
`[91m` (for red), and the string `[0m` at the end of your output lines, you're doing this correctly. It's just 
another instance of IDLE being a buzzkill.

### _The `display_health()` function_

Finally, the `display_health()`, which will accept the `health` integer parameter as its only parameter, will use our
other functions to print both a numerical and a visual health UI.

Sample executions:


```python
display_health(92)
display_health(54)
display_health(6)
```

Terminal output:


> <span style="color:green; font-family:Courier">HP: 92 / 100</span>
> 
> <span style="color:green; font-family:Courier">[===================&nbsp;]</span>

> <span style="color:yellow; font-family:Courier">HP: 54 / 100</span>
> 
> <span style="color:yellow; font-family:Courier">[===========&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</span>

> <span style="color:red; font-family:Courier">HP: 6 / 100</span>
> 
> <span style="color:red; font-family:Courier">[==&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</span>

IDLE output:

```text
[92mHP: 92 / 100[0m
[92m[=================== ][0m
[93mHP: 54 / 100[0m
[93m[===========         ][0m
[91mHP: 6 / 100[0m
[91m[==                  ][0m
```