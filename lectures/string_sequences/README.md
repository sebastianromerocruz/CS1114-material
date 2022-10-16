## Lecture 10

# Loop Review and Strings as Sequences

### 19 Vendémiaire, Year CCXXXI

***Song of the day***: _[**So What**](https://youtu.be/zqNTltOGh5c) by Miles Davis (1959)._

### Sections

1. [**Review: _Game Programming 101_**](#part-0-review-game-programming-101)
2. [**Strings As Sequences**](#part-1-strings-as-sequences)
3. [**String Comparison**](#part-2-string-comparison)
4. [**The `in` Operator**](#part-3-the-in-operator)
5. [**Special Characters And `print`'s `end` Parameter**](#part-4-special-characters-and-prints-end-parameter)

### Part 0 (Review): _Game Programming 101_

In game programming, your standard game loop looks as follows:

```
INITIALISE the game

WHILE user hasn't QUIT:
    ASK for user
    PROCESS user input
    DISPLAY results of process

SHUT DOWN the game
```

We're going to create a simple mental math game that will follow this general structure. The goal of the game is for us to be able to calculate the average of a given set of random numbers in our heads. The user will decide:

- The upper limit of the randomly generate numbers (the lower limit will always be 1)
- What the tolerance of their answer should be (i.e. if the tolerance is 1, and the answer is 7, then all answers between 6 and 8 are considered correct)
- How many random numbers will be averaged.

The user will also have the ability to decided whether they want to play the game again after guessing the answer, or simply quit. Here's a sample execution of how the whole game would look like (you can format your output however you like as long as the mechanics of the game work the same):

```
|————————WELCOME TO THE NUMBER GUESSING GAME————————|
> ENTER THE UPPER LIMIT OF THE GENERATED NUMBERS (must be higher than 0): 10
> ENTER THE TOLERANCE OF YOUR ANSWER: 0.5
> READY? (press any key to begin) 
> HOW MANY NUMBERS WOULD YOU LIKE TO AVERAGE? 5
> ADDING 6 TO THE SUM...
> ADDING 4 TO THE SUM...
> ADDING 1 TO THE SUM...
> ADDING 9 TO THE SUM...
> ADDING 9 TO THE SUM...
> WHAT IS THE AVERAGE OF THESE 5 NUMBERS? 6
CORRECT! THE EXACT ANSWER WAS 5.8. WOULD YOU LIKE TO PLAY AGAIN? (press any key for yes, 'q' for no) 
> HOW MANY NUMBERS WOULD YOU LIKE TO AVERAGE? 2
> ADDING 6 TO THE SUM...
> ADDING 8 TO THE SUM...
> WHAT IS THE AVERAGE OF THESE 2 NUMBERS? 7
CORRECT! THE EXACT ANSWER WAS 7.0. WOULD YOU LIKE TO PLAY AGAIN? (press any key for yes, 'q' for no) q
GAME OVER.
```

<sub>Note here that the numbers `6`, `4`, `1`, `9`, and `9` in the first run of the game are being automatically generated and added to the sum without input from the user. The correct answer is 5.8 here, and the user entered 6. This is considered correct because the tolerance of the game is 0.5. Therefore, any number between 5.2 and 6.4 is considered correct.</sub>

This program has several parts, so let's tackle it section by section.

#### ***Initialising The Game***

We want the intialisation process of the game to do the following:

1. Welcome the user to the game
2. Ask what tolerance of the correct answer they want? (you can assume that they will enter a non-zero positive number)
3. Ask the user what the upper limit of the generated numbers will be (you can assume that they will enter an integer)
    - If the user enters a number for the upper limit that is _lower than or equal_ to the 0, your program must ask them to enter another number again until they enter a number that is higher than the 0
5. Ask the user if they are ready to begin, and have them enter any key to begin the game

A sample execution of this section will behave as follows:

```commandline
|————————WELCOME TO THE NUMBER GUESSING GAME————————|
> ENTER THE UPPER LIMIT OF THE GENERATED NUMBERS (must be higher than 0): 10
> ENTER THE TOLERANCE OF YOUR ANSWER: 0.5
> READY? (press any key to begin) 
```

Make sure to get this part to work before moving on!

#### ***One Run Of The Game***

Before we get started with the actual game loop, try to get the game to run just once. So, forget about asking the user if they want to play again—just pretend that they're going to play once, and that's it.

If this is the case, your job is to:

1. Ask the user how many randomly generated numbers they want.
2. Generate that many random numbers and add them together.
3. Calculate the average.
4. Ask the user to guess that average.
    1. If they guess within the plus/minus tolerance of the correct answer, then the game ends (make sure to tell them use that they were correct).
    2. If they don't guess within that range, the game asks them to enter an answer again.

A sample execution of the game up to this point would look like this:

```
|————————WELCOME TO THE NUMBER GUESSING GAME————————|
> ENTER THE UPPER LIMIT OF THE GENERATED NUMBERS (must be higher than 0): 10
> ENTER THE TOLERANCE OF YOUR ANSWER: 0.5
> READY? (press any key to begin) 
> HOW MANY NUMBERS WOULD YOU LIKE TO AVERAGE? 5
> ADDING 6 TO THE SUM...
> ADDING 4 TO THE SUM...
> ADDING 1 TO THE SUM...
> ADDING 9 TO THE SUM...
> ADDING 9 TO THE SUM...
> WHAT IS THE AVERAGE OF THESE 5 NUMBERS? 6
CORRECT! THE EXACT ANSWER WAS 5.8.
```

Make sure to get this part to work before moving on!

#### ***A proper game loop***

Finally, get your program to ask the user if they want to play again. You already know how to make your program run once. So what do we do to code that we want to run endlessly until the user tells us to stop?

Take a look at the first sample execution to see how your game should behave.

### Part 1: _Strings as Sequences_

Remember that a `for`-loop iterates through every member of a sequence?

```python
for number in range(0, 10):
    print("Sequence member '", number, "'", sep="")
```

Output:

```text
Sequence member '0'
Sequence member '1'
Sequence member '2'
Sequence member '3'
Sequence member '4'
Sequence member '5'
Sequence member '6'
Sequence member '7'
Sequence member '8'
Sequence member '9'
```

So, in this case, our sequence is every whole number between and including 0 and 9:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

It turns out that, in Python, sequences aren't limited to being numerical—they can also be alpha-numerical:

```python
alpha_seq = "Adachi and Shimamura"

for character in alpha_seq:
    print(character)
```

Output:

```text
A
d
a
c
h
i
 
a
n
d
 
S
h
i
m
a
m
u
r
a
```

So is a string a sequence? Technically. It can basically be used in sequence-like ways, which makes it very handy for 
programmers, since a good amount of user-input that we receive is in string form. The ability to be able to consider 
characters one-by-one is will prove to be indispensable.

---

What are other cool, sequence-like things we can do with strings?

Well, what if we wanted to access any individual letter in a string? Let's say we have the following activity log in a
chat-room:

```text
[A]: hey
[A]: whats up
[B]: Please leave me alone
```

In this case, it's pretty clear that the `"A"` and `"B"` characters represent two members of a chat-room. Moreover, we
know that both `"A"` and `"B"` are always the second character in the whole line. We can use this information to our 
advantage by using something called ***indexing***.

Let's say we wanted to find out whether user A or user B sent the message:

```python
ID_LOCATION = 1

message = "[B]: Please leave me alone"
user_id = message[ID_LOCATION]

print("User", user_id, "sent this message.")
```

Output:

```text
User B sent this message.
```

So, what did we do? The key line here is:

```python
user_id = message[ID_LOCATION]
```

Since `ID_LOCATION` is equal `1`, we could read this line as:

> Take the **first** character from the string variable `message` and store it inside a variable called `user_id`.

Why is it the first character if `A` and `B` always appear after the `[`? General speaking, all programming languages 
start counting from `0` instead of `1`. That's actually why the `range()` function's default starting value is `0`—it's
an inherent characteristic of most programming languages. So if you wanted to refer to the `[` in the strings above, 
you'd say:

> In the string `"[B]: Please leave me alone"`, the **0th** (zeroth) element is `[`.

So with this knowledge, we can now print each of the characters of a string in two ways:

```python
BOOK_TITLE = "In Search of Lost Time"
LENGTH = 22

# using sequences
for letter in BOOK_TITLE:
    print(letter)

# using indices
for index in range(LENGTH):
    letter = BOOK_TITLE[index]
    print(letter)
```

---

One quick other (***very***) important thing about strings is that they are ***immutable***. That is, once you define
the value of a string, you **cannot** change it. The only way to do something similar is to create a whole new string
using the value of the old string:

```python
first_name = "Élisabeth Louise"
last_name = "Vigée Le Brun"
full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Élisabeth Louise Vigée Le Brun
```

Here, it is very important to recognize that the string `full_name` is _not_ `first_name` with the strings `" "` and 
`last_name` appended to it. Instead, it is a **completely** different string, existing in a completely different place 
in memory. This new string will simply happen to have the contents of `first_name`, `" "`, and `last_name` put together
in that order—and only because we asked Python to create it in such a way.

Mutability / immutability is a huge topic in this class and computer science in general, so don't forget the words.
We'll see them again soon enough.

### Part 2: _String Comparison_

If we have a variable called `string`, and it has a value of `"abc"`. What does the following expression evaluate to?

```python
>>> string == "abc"
```

Well, let's check the output:

```python
>>> string == "abc"
True
```

Makes sense; the comparison operator `==` checks whether two Python objects are equal in value. Since the value of 
`string` is `"abc"`, it is indeed equal to the string `"abc"`.

So, if we can check for the equality of strings, can we check for inequality?

```python
>>> string != "not abc lol"
True
```

Makes sense; these strings are not at all the same in value. These are both pretty intuitive operations, but what about
comparing them using `>`, `<`, `>=`, and `<=`?

```python
>>> string >= "not abc lol"
False

>>> string < "bcd"
True
```

Clearly, these operations are not causing errors, so how do they work? When comparing string, Python uses their 
**lexicographical order** in order to determine whether one is larger than the other. Lexicographical order simply means
applying a value of, say, 1 to `"a"`, 2 to `"b"`, 3 to `"c"`, etc. (the numerical equivalent of `"a"` is actually `97`, 
but don't worry about that for now).

This means that:

```python
>>> "a" > "b"
False
>>> "a" < "b"
True
>>> "A" < "b"
True
```

Notice that these operations are not case-sensitive—a very rare exception in programming.

What about comparisons using strings of different lengths? Python basically goes in order:

```python
>>> "Paris" > "Parthenon"
False
```

1. Is the `"P"` from `"Paris"` equal to the "`P`" from `"Parthenon"`? Yes, so move on to the next character.
2. Is the `"a"` from `"Paris"` equal to the "`a`" from `"Parthenon"`? Yes, so move on to the next character.
3. Is the `"r"` from `"Paris"` equal to the "`r`" from `"Parthenon"`? Yes, so move on to the next character.
4. Is the `"i"` from `"Paris"` equal to the "`t`" from `"Parthenon"`? No, so apply the `>` operation.
5. Is `"i"` > `"t"`? `"i"` has a lower lexicoogical value than `"t"` (i.e. it appears earlier in the alphabet), so this
operation evaluates to `False`.
6. The whole operation evaluates to `False`

What about this?

```python
>>> "Car" >= "Cartagena"
False
```

1. Is the `"C"` from `"Car"` equal to the "`C`" from `"Cartagena"`? Yes, so move on to the next character.
2. Is the `"a"` from `"Car"` equal to the "`a`" from `"Cartagena"`? Yes, so move on to the next character.
3. Is the `"r"` from `"Car"` equal to the "`r`" from `"Cartagena"`? Yes, so move on to the next character.
4. Since `"Car"` has no more values to compare with `"Cartagena"`, `"Cartagena"` is by default of larger value.
5. The operation, thus, evaluates to `False`.

Here are more examples:

```python
>>> "Sonny Boy" < "SONNY BOY"
False

>>> "Nozomi" >= "Mizuho"
True

>>> "Napoleon I" > "Napoleon III"
False

>>> "!!!" <= "   "
False
```

That last one is a bit of a toughie if you don't know about ASCII values and how to find them, but don't worry—it's not
important for now. We'll get there eventually.

### Part 3: _The `in` Operator_

Yay, a new operator! `in` is actually kind of heaven-sent if you come from a Java/C++ background. `in` is what is called
a **membership** operator, and it evaluates to either `True` or `False`:

```python
>>> "Car" in "Cartagena"
True

>>> "PARIS" in "Parisian"
False
```

The above operations can be described in English as follows:

>> The string `Car` exists as a sub-string of the exact same value somewhere in the string `Cartagena`.
> 
>> The string `PARIS` does not exist as a sub-string of the exact same value somewhere in the string `Parisian`.

That's why it's called a membership operator: it checks for the membership of an object inside another object. You can 
also check for non-membership:

```python
>>> "Prague" not in "Czechia"
True

>>> "1" in "onetwothree"
False

>>> "net" not in "onetwothree"
False
```

---

### Part 4: _Special Characters and `print()`'s `end` Parameter._

There are a few "special characters" in programming that we should be aware of. The two that we'll need in this course
are `"\n"` and `"\t"`.

`\n` is the **newline operator**:

```python
information = "NAME: Alice Sara Ott\nOCCUPATION: Pianist\nBIRTHPLACE: München, West Germany"
print(information)
```

Output:

```text
NAME: Alice Sara Ott
OCCUPATION: Pianist
BIRTHPLACE: Munich, West Germany
```

And `\t` is the **tab, or indentation, operator**:

```python
first_half = "Jan\tFeb\tMar\tApr\tMay\tJun\t"
second_half = "Jul\tAug\tSep\tOct\tNov\tDec\t"

print(first_half)
print(second_half)
```

Output:

```text
Jan	Feb	Mar	Apr	May	Jun	
Jul	Aug	Sep	Oct	Nov	Dec	
```