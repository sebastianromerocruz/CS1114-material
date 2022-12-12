<h2 align=center>Lecture 27</h2>

<h1 align=center>Final Exam Review</h1>

### 21 Frimaire, Year CCXXXI

***Song of the day***: _[**fullmoon lullaby**](https://youtu.be/nx-qpEMUzes) by Porter Robinson & WEDNESDAY CAMPANELLA (2021, suggested by Abdulrahman A.)_

---

### _Eeveelutionary Theory_

As you may remember from the review, the Pokémon [**Eevee**](https://bulbapedia.bulbagarden.net/wiki/Eevee_(Pok%C3%A9mon)) has several type-specific [**evolutions**](https://bulbapedia.bulbagarden.net/wiki/Eeveelution). Eevee will evolve into some of these Pokémon depending on which **evolution stone** it is given. For the purposes of this problem, we'll focus on the original three Eeveelutions:

- **Vaporeon** (_`"water"`-type_): If Eevee is given a _Water Stone_ (`"water_stone"` in code).
- **Jolteon** (_`"electric"`-type_): If Eevee is given a _Thunder Stone_ (`"thunder_stone"` in code).
- **Flareon** (_`"fire"`-type_): If Eevee is given a _Fire Stone_ (`"fire_stone"` in code).

Define an `Eevee` class that will accept two parameters: `nickname`, a string containing the nickname given to the `Eevee` object, and `description_filepath`, a string containing the address of a `txt` file containing a short description of this specific `Eevee` object. The file, if it exists, will always look slightly different depending on 
the Eevee's specific stats, but it will always be of the following general format:

```text
Eevee
Nature: friendly
Level: 5
```

The `Eeevee` class will have five instance attributes:

- `nickname`: The nickname passed by the user.
- `eeveelution_status`: The current Eeveelutionary status of the `Eevee` object. The value of this attribute is `None` when the Eevee is un-evolved, or either `"Vaporeon"`, `"Jolteon"`, or `"Flareon"` if it has been evolved. We can assume that all newly instantiated `Eevee` objects start un-evolved.
- `type`: A string containing the current type of the `Eevee` object. We can assume that all newly instantiated `Eevee` objects are of type `"normal"`.
- `nature`: A string containing the nature denoted in the file. Will be `None` if file is not successfully opened.
- `level`: An integer containing this object's level as denoted in the file. Will be `1` if file is not successfully opened.

---

The `Eevee` class will have three instance methods associated to it. The first `can_evolve()` (_**sig**: `str` => `bool`_), will accept one string parameter, `stone_name`, a string containing the name of the evolutionary stone that the user wishes to give to this `Eevee` object. `can_evolve()` will then return `True` **if and only if**:

1. The `Eevee` object is un-evolved,
2. The `stone_name` is one of the three valid evolutionary stones mentioned above.

If either of these conditions is not met, `can_evolve()` will return `False`.

---

Next, define a method called `evolve()` (_**sig**: `str` => `None`_). `evolve()` will accept one parameter, `stone_name`, a string containing the name of the evolutionary stone that the user wishes to give to this `Eevee` object. If the `Eevee` object meets all conditions necessary to evolve, `evolve()` will update the `eeveelution_status`
and `type` of the `Eevee` object to their appropriate new values.

To make this a little simpler, you may assume that the following dictionary is already defined at the top of your file, which you may use if you find it useful (in other words, you **don't** have to use it if you don't find it useful):

```python
INFO_PER_STONE = {
    "water_stone": {
        # Water stone information
        "eeveelution": "Vaporeon",
        "type": "water"
    },
    "thunder_stone": {
        # Thunder stone information
        "eeveelution": "Jolteon",
        "type": "electric"
    },
    "fire_stone": {
        # Fire stone information
        "eeveelution": "Flareon",
        "type": "fire"
    }
}
```

---

Finally, define a `get_stats()` method (_**sig**: `None` => `list`_) that will return a list of the values of all the object's non-`None` attributes. If you can, do this using list comprehension—only then will you become a Python deity.

---

Sample behaviour:

```python
# If the file exists...
camille = Eevee("Camille", "description.txt")
print(camille.get_stats())  # pre-evolution

camille.evolve("thunder_stone")
print(camille.get_stats())  # post-evolution

# If the file doesn't exist...
fryderyk = Eevee("Fryderyk", "not_description.txt")
print(fryderyk.get_stats())  # pre-evolution

fryderyk.evolve("fire_stone")
print(fryderyk.get_stats())  # post-evolution
```

Output:

```text
['Camille', 'friendly', 5, 'normal']
['Camille', 'Jolteon', 'friendly', 5, 'electric']
['Fryderyk', 5, 'normal']
['Fryderyk', 'Flareon', 5, 'fire']
```

---

[**Solution**](solution/eevee.py)