<h2 align=center>Lecture 14</h2>

<h1 align=center>Function Review and Function Parameters</h1>

### 2 Brumaire, Year CCXXXI

***Song of the day:*** _[**Body Talk**](https://youtu.be/Oo_NIdBUzMU) by Red Velvet (2017)._

### Sections

1. [**The Super Entertaining and Basic (S.E.B) Calculator**](#part-1-the-super-entertaining-and-basic-seb-calculator)
    1. [**Introduction**](#introduction)
    2. [**`add()`, `subtract()`, `multiply()`, and `divide()`**](#step-1-add-subtract-multiply-and-divide)
    3. [**`do_arithmetic()`**](#step-2-do_arithmetic)
    3. [**Our Driver Function, `main()`**](#step-3-our-driver-function-main)
    4. [**Run The Program**](#step-4-run-the-program)

### Part 1: _The Super Entertaining and Basic (S.E.B) Calculator._

#### ***Introduction***

Our goal is to create a calculator that will function as follows:

```text
Welcome to the S.E.B Calculator!

Would you like to calculate (y), or shut down (n)? y

Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. add
ERROR: Please enter a valid operator (i.e. +, -, *, /).
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. addition
ERROR: Please enter a valid operator (i.e. +, -, *, /).
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. +
Enter a number: 42
Enter another number: 42
42.0 + 42.0 = 84.0
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. /
Enter a number: 42
Enter another number: 0.42
42.0 / 0.42 = 100.0
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. *
Enter a number: 5
Enter another number: 0.77
5.0 * 0.77 = 3.85
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. DONE

Would you like to continue operation? [y/n] y

Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. +
Enter a number: 4
Enter another number: 5
4.0 + 5.0 = 9.0
Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. DONE
Would you like to continue operation? [y/n] n
```

<sub>**Note**: Your output need not look exactly like mine.<sub>

That is, a program that will:

1. Ask the user if they want to perform arithmetic operations, or shut down. Here, and only here, you can assume that the
user will enter either `'y'` for "yes" and `'n'` for "no".
2. If the user chooses "yes", the calculator will ask them to enter the operator that they want to use between **two** 
numerical operands. Here, the user is **limited to `'+'`, `'-'`, `'*'`, `'/'`, and `"DONE"` (to stop arithmetic 
operations).** If the user enters anything else, the program should ask them for input again until they enter a valid 
operator.
3. Once a valid operator has been entered, the program will prompt the user to enter two numerical values (here, you can
assume that the user will always enter real, valid numerical values). The program will then print the result of such
operation.
4. The program will then ask the user if they want to perform another arithmetic operation (i.e. step 2).
5. If the user chooses not to continue (`"DONE"`), the program will ask the user if they want to continue or shut down 
(i.e. step 1).

As you can see, we have a couple of program loops going on here, and it super complicated, but let's break each of these
steps down into small functions to help us organize better.

---

#### ***Step 1***: `add()`, `subtract()`, `multiply()`, and `divide()`

Define four simple functions, `add()`, `subtract()`, `multiply()`, and `divide()`. Each of these functions will do the
following:

1. Ask the user for two numerical inputs.
2. Perform the relevant arithmetic operation.
3. Print the result.

That's it. Make sure to get these four functions down before moving on!

---

#### ***Step 2***: `do_arithmetic()`

Define a function called `do_arithmetic()`. This function will perform the instructions from step 2 above:

1. The calculator will ask them to enter the operator that they want to use between **two** numerical operands.
2. If the user enters anything other than a valid operator, the program should ask them for input again until they enter
a valid operator.
3. Once they do, your program must **perform a function call** to either `add()`, `subtract()`, `multiply()`, and 
`divide()` depending on what operator was chosen. If `"DONE"` was chosen, this marks the end of your function.

<sub>**Note**: Make sure to actually use `add()`, `subtract()`, `multiply()`, and `divide()` in this step! We're trying
to get used to breaking programs down into functions. Since it's our first time doing this, don't worry if you struggle 
with it—just follow the instructions and give it your best shot.</sub>

---

#### ***Step 3***: Our driver function, `main()`

The function that will run this whole program will be called, by convention, `main()`. This function will perform the
instructions from step 1 in our introduction:

1. Ask the user if they want to perform arithmetic operations, or shut down. Here, and only here, you can assume that 
the user will enter either `'y'` for "yes" and `'n'` for "no".
2. If they say "yes", run `do_arithmetic()`. If they say "no". Your `main()` function can end.

---

#### ***Step 4***: Run the program.

At the end, make a call to your `main()` function to run the whole thing!