## Review: _Game Programming 101_

In game programming, your standard game loop looks as follows:

```
INITIALISE the game

WHILE user hasn't QUIT:
    ASK for user input
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