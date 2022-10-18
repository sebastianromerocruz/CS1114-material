<h2 align=center>Lecture 13<h2>

<h1 align=center><strong>Midterm 1 Review</string>: Read Between The Lines</h1>

### 27 Vendémiaire, Year CCXXXI

***Song of the day:*** _[**Looking For Somebody To Love (Official Live Performance)**](https://youtu.be/ORCNXtnlD38) by The 1975 (2022)._

### Sections

1. [**The Problem**](#part-1-the-problem)
2. [**The Solution**](#part-2-the-solution)
    1. [**The Indexing Solution**](#the-indexing-solution)
    2. [**The Slicing Solution**](#the-slicing-solution)

### Part 1: _The Problem_

Let's say you wanted to decode a message that used the following encryption: Starting from the last character of the
sentence, you must read every X-th letter. If the character that you land on is a number, you must skip it. For
instance:

```text
Enter an encoded string: !thnsdosdhdft7g68yyrop
Enter a key: 2
Your message is 'python!'
```

Above, we start at the last character, **`'p'`**, skip 2 (as denoted by the decryption key), and ignore the one numeric character we landed on (**`'6'`**):

```
STEP 0:
!thnsdosdhdft7g68yyrop

STEP 1:
! [th] n [sd] o [sd] h [df] t [7g 6 8y] y [ro] p

STEP 2:
! n o h t y p

STEP 3
!nohtyp

STEP 4:
python!
```

<sub>**Note**: This is just a visualisation of why `python!` is the answer. These are not necessarily the steps that your code would take.</sub>

You may assume that both user inputs will always be valid ones. You may **not** use the **`reverse()`** string method.

### Part 2: _The Solution_

This problem is a tough one, but it's really good practice if you want to get good at indexing, string slicing, or both.

The first thing to recognise here is that your final, decoded message will be an altered, _reversed_ version of the original. This tells us that we'll be using a negative step in either the `range()` function or in string slicing. Let's consider the `range()` alternative first.

#### ***The Indexing Solution***

Since we're not allowed to use the `reverse()` string method, we have to traverse the string backwards. We know that we can generate a sequence of backwards numbers using `range()`. The question is what the arguments are. 

- We know that the _starting point_ is the end of the string, which we can instantly get by using the `len()` function. The only thing to keep in mind is that the starting point is inclusive, so we need to subtract 1 in order to not get an Out-of-Range error. The starting point is thus **`len(encoded_message) - 1`**.
- The ending point will, by the same token, be the beginning of the string. Since the ending point is non-inclusive, we have to make sure that it includes 0, so the ending point should be **`-1`**.
- The step should skip `key` number of characters, and go backwards. In the example, the key is `2`, but this means that we are skipping 2 characters. Using `2` as the step only skips 1 character, so we just need to increase the value of key by 1. The step, thus, is `-1 * (key + 1)`.

Using these as our arguments for the `range()` function, we get the following:

```python
decoded_message = ""

start = len(encoded_message) - 1
end = -1
step = -1 * (key + 1)

for index in range(start, end, step):
    character = encoded_message[index]
    decoded_message += character
```

Let's see what the value of decoded message is if we go about it this way:

```
py6thon!
```

Hm, close. The instructions say that we should ignore numerical characters, so let's just add a simple check inside our `for`-loop:

```python
for index in range(start, end, step):
    character = encoded_message[index]

    if not character.isdigit():
        decoded_message += character
```

Output:

```
python!
```

Perfect. You can find this whole solution [**here**](solution/indexing_solution.py).

### ***The Slicing Solution***

The slicing solution is actually really similar. The first step is to cleanse the encoded message from all numerical characters first:

```python
for char in encoded_message:
    if not char.isdigit():
        decoded_message += char
```

`decoded_message`, after this, looks as follows:

```
!thnsdosdhdftgyyrop
```

From here, we basically use almost the same value we used as arguments for the `range()` function as arguments for our slicing:

```python
start = len(decoded_message) - 1
step = -1 * (key + 1)

decoded_message = decoded_message[start::step]
```

The value of `decoded_message` would thus be:

```
python!
```

If you tries doing `decoded_message[start:-1:step]` instead, you would get the following:

```
''
```

I.e., an empty string. Why? This is a good time to remember that negative numbers in indexing represent _indexing starting from the end of the string_. Therefore, by doing `decoded_message[start:-1:step]`, we're asking it to start _and_ to end at the last index of the string. By leaving the field empty, the slicing mechanism will assume that you want to end at the beginning, which is what we want. We can thus rewrite the slicing as follows:

```python
start = -1              # the negative-first index is the last index of a sequence
step = -1 * (key + 1)   # this step is the same

decoded_message = decoded_message[start::step]
```

You can find this full solution [**here**](solution/slicing_solution.py).