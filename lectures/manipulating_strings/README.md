## Lecture 11

# Manipulating Strings

### 12 Ventôse, Year CCXXX

***Song of the day:*** _[**Heart Attack**](https://youtu.be/BVVfMFS3mgc) by LOONA/Chuu (2017)._

---

### Part 0: _Character Representation (Continued)_

Recall our conversation on the ASCII table:

![ascii](assets/ascii-table-alpharithms-scaled.jpg)


<sub>**Figure 1**: ASCII Table ([**Source**](https://www.alpharithms.com/ascii-table-512119/)). </sub>

ASCII stands for _American Standard Code for Information Interchange_, and is a means of encoding characters for digital
communications. It was originally developed in the early 1960s as early networked communications were being developed.

Strangely, this table was developed to encode characters in 7-bits, so it contains a maximum of (1111111)<sub>2</sub>, 
or (127)<sub>10</sub>, characters.

Now, as a good number of us are not from Anglophone countries, this table will seem restrictive—and it is. Romance 
and other Germanic languages contain a good number of accent marks, for instance (etc. `señal`, `coração`, `straße`).
Even worse, more than half of the world population doesn't even use a Latin-based alphabet in daily communication—the 
[**cyrillic**](https://en.wikipedia.org/wiki/Cyrillic_script#Letters) and 
[**Greek**](https://en.wikipedia.org/wiki/Greek_alphabet#Letters) alphabets, syllabaries like the ingenious Korean
[**hangul**](https://en.wikipedia.org/wiki/Hangul), let alone the topographic 
[**hànzì, kanji, and hanja**](https://en.wikipedia.org/wiki/Chinese_family_of_scripts) of China, Japan, and Korea, are
completely ignored.

Now, of course, we have what is known as [**unicode**](https://en.wikipedia.org/wiki/Unicode), which can encode 
characters in 8-, 16-, and even 32-bits to accommodate to these important sets of characters.

---

So how do we use this information in Python—and what is it good for?

To find out a character's ASCII equivalent, we use the `ord()`, or **ordinal**, function:

```python
>>> ord("a")
97

>>> ord("A")
65

>>> ord("ñ")
241

>>> ord("疲")
30130

>>> ord("δ")
948
```

And, conversely, to find the corresponding character to any given positive integer, we use `chr()`:

```python
>>> chr(123)
'{'

>>> chr(42)
'*'

>>> chr(512)
'Ȁ'
```

### Part 1: _String Traversal (Continued)_

Let's continue our conversation on strings with a quick program. Write a program that asks the user for two strings 
`first_string` and `second_string`. Then, your program will print all the characters from the first string that appear 
in the second string. Write three versions of this program:

1. Using `for`-loop string sequencing.
2. Using `for`-loop string indexing.
3. Using string indexing, but with a `while`-loop.

Here's a sample
output of how your program could behave:

```text
Enter a string: Rickenbacker 4000C Bass Guitar
Enter a second string: Rickenbacker 330 Electric Guitar
R
i
c
k
e
n
b
a
c
k
e
r
 
0
 
e
c
t
r
i
c
 
G
u
i
t
a
r
```

There are two ways we could approach this. The quickest and perhaps more intuitive one is use the second string as a
sequence, and then check for membership of each of its letters in the first string. We do this by using `in`, the 
membership operator:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

for letter in second_string:
    if letter in first_string:
        print(letter)
```

<sub>**Code Block 1**: Checking for membership by treating `second_string` as a sequence.</sub>

If we didn't want to use `second_sentence` as a sequence, and instead wanted to use indices, our `for`-loop would look 
something like this instead:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)

for index in range(second_string_length):
    letter = second_string[index]
    if letter in first_string:
        print(letter)
```

<sub>**Code Block 2**: Checking for membership by using indices. Note the use of `len()`.</sub>

Both ways work and are actually equally efficient. Which one to use depends largely on your use case. If you need to 
know, use, or keep track of the position of an element within a sequence (e.g. _"Find the x-th element of the string"_),
then using indices is the way to go.

Finally, the `while`-loop version will look as follows:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)
index = 0

while index < second_string_length:
    letter = second_string[index]
    if letter in first_string:
        print(letter)

    index += 1
```

Check out the code here [**membership.py**](membership.py) with the configuration `Membership`.

### Part 2: _The `str` Object_

We've been spending a fair amount of time using strings now, so we should probably dive in a little deeper into their 
behavior.

Objects in general (not just `str` objects) have a set of values and operations associated to them. In technical jargon,
we would say that objects have **reference attributes bound to them**. The values associated with objects are called
**attributes** (similar to variables), and the operations associated with objects are called **methods** (similar to 
functions):

>> **Attribute**: A _variable_ associated to an object of a certain type/class.
> 
>> **Method**: A _function_ associated to an object of a certain type/class.

Both of these terms will make more sense when we get to object-oriented programming, but just learn to recognise this
behavior when I say things like "this is a _method_ of a `str` object", for example.

Let's take a look at some examples:

```python
>>> string = "the tale of the heike"
>>> string.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> string.__class__
<class 'str'>
```

In this case, `__doc__` is an **attribute** associated to the string object `string`, which prints out a bunch of 
technical information that you don't need to worry about. `__class__` is another such attribute, which tells us the name
of the class of the current object (in this case, it's a `str` object).

Let's take a look now at a couple of **methods**:

```python
>>> string = "the tale of the heike"
>>> string.capitalize()
'The tale of the heike'
>>> string.upper()
'THE TALE OF THE HEIKE'
```

In this case, `capitalize()` is ***returns*** a string with its first character capitalized (if the first character is
not a lower-case letter, it will simply return the same string). By the same token, `upper()` ***returns*** a string
with the original string's letters capitalized.

This is important. **Strings are immutable**; none of their methods that appear to be mutating them in any way, but 
rather creating an entirely new string object based on the contents of the original:

```python
>>> example = "Mineral water"
>>> example.upper()
'MINERAL WATER'
>>> example
'Mineral water'
>>> example_upper = example.upper()
>>> example_upper
'MINERAL WATER'
```

The value of example didn't change when its `upper()` method was invoked.

Here are some examples of methods from the `str` class that we'll be making heavy use of in this class:

| **Method**  | **Example**                                                                                                                | **Description**                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `find()`    | `"abc".find("a")` returns `0` `"abc".find("z")` returns `-1`                                                               | Returns the index of **first** occurrence of the argument in a string object.              |
| `format()`  | `"Hi, my name is {}, and I love {}.".format("Sebastian", "Zelda")` returns `"Hi, my name is Sebastian, and I love Zelda."` | Formats string into nicer output.                                                          |
| `isalnum()` | `"1978".isalpha()`  returns  `False`  `"The1975".isalpha()`  returns  `True`                                               | Returns `True` if all the characters in a `str` object are alphanumeric.                   |
| `isalpha()` | `"1978".isalpha()` returns `False`  `"TheNineteenSeventyFive".isalpha()` returns `True`                                    | Returns `True` if all the characters in a `str` object are alphabetic.                     |
| `isdigit()` | `"1978".isdigit()`  returns  `False`  `"The1975".isalpha()`  returns  `False`                                              | Returns `True` if all the characters in a `str` object are numeric.                        |
| `islower()` | `"The The".islower()` returns `False`                                                                                      | Returns `True` if all the characters in a `str` object are lowercase.                      |
| `isupper()` | `"NYU".isupper()` returns `True`                                                                                           | Returns `True` if all the characters in a `str` object are uppercase.                      |
| `lower()`   | `"Liz and The Blue Bird.".lower()` returns `"liz and the blue bird."`                                                      | Returns a `str` object with all uppercase characters from the original string lower-cased. |
| `upper()`   | `"Liz and The Blue Bird.".upper()` returns `"LIZ AND THE BLUE BIRD."`                                                      | Returns a `str` object with all lowercase characters from the original string upper-cased. |

_**Figure 1**: Some useful `str` methods in this class 
([**Full list**](https://docs.python.org/2.5/lib/string-methods.html))._

There are obviously...a lot of them. But you don't have to memorize all of them. They're all pretty intuitive and self-
explanatory, so it's actually really easy to remember them.

**NOTE**: You may ***not*** yet use `split()` or any other method that returns a `str` object into a `list` object or
any other object that we haven't seen yet. This will be penalized in homework, so please always ask if you are unsure
whether you are allowed to use something or not.

### Part 3: _String Operations_

#### _Concatenation_

Okay, so if you can't modify strings, but your program requires you to put a bunch of strings together, what do we do?

Python makes this extremely easy for us, actually. We can quite literally add two strings together by using the `+` 
operator. This process is called **string concatenation**:

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name

print(full_name)
```
Output:
```commandline
Camille Pissarro
```

Nothing we haven't seen before. We just have a name for it now. Again, remember neither `first_name` nor `last_name` are
being modified in any way here. All Python is doing here is extracting the contents of `first_name` and `last_name` and
creating a completely new string out of them, `full_name`.

What about this example?

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name
age = 73
full_info = full_name + ", " + age

print(full_info)
```

Output:

```commandline
Traceback (most recent call last):
  File "<input>", line 5, in <module>
TypeError: can only concatenate str (not "int") to str
```

Ah-hah. We've seen this error before. You cannot concatenate a `str` and an `int`. So if you want to create a new string
from these components, you have to **explicitly convert all non-`str` components into `str` objects**:

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name
age = 73
full_info = full_name + ", " + str(age)

print(full_info)
```

Output

```commandline
Camille Pissarro, 73
```

We didn't have to do this when we were composing `print()` statements because `print()` takes care fo the type 
conversions for us. But more often than not, we will not be able to rely on `print()` so it's important to know how to
do it yourself.

#### _Slicing_

The second important operation that we can do with strings is _slicing_ them—that is, extracting a specified subsection.

We, of course, already learned how to index a string, which is technically a form of slicing:

```python
>>> "Ahmad Jamal"[4]
'd'
```

But, just like with the `range()` function, we have the power to define our starting, ending, and stepping value using
the following syntax:

```python
>>> "Ahmad Jamal"[2:7]
'mad J'
```

```python
>>> jazz_musician = "Ahmad Jamal"
>>> jazz_musician[2:len(jazz_musician):2]
'mdJml'
```