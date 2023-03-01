# Review: _The Value of Words_

We will be writing a program that will measure the "ASCII value" of a set of user-inputted words. The way we will be 
calculating the ASCII value of any given word is by adding up the ASCII value of all the 
[**letters**](https://www.techonthenet.com/ascii/chart.php) inside that word. For example, if our word were `"Hello"`, 
the ASCII value would be 500, since the ASCII value of `'H'` is 72, `'e'`'s is 101, `'l'`'s is 108, and `'o'`'s is 111:

```commandline
72 + 101 + 108 + 108 + 111 = 500
```

The user should be allowed to input words and/or sentences until they enter the program's end code of `-1`, and the 
program should print the individual ASCII value of each of the user's input besides adding it to the total:

```commandline
Enter a word to measure, or -1 to stop: Adachi and Shimamura
The value of the word(s) 'Adachi and Shimamura' is 1812.
Current total value: 1812

Enter a word or words to measure, or -1 to stop: Bonjour Tristesse
The value of the word(s) 'Bonjour Tristesse' is 1701.
Current total value: 3513

Enter a word or words to measure, or -1 to stop: -1

The final value is 3513
```
```commandline
Enter a word to measure, or -1 to stop: Liz and the Blue Bird
The value of the word(s) 'Liz and the Blue Bird' is 1708.
Current total value: 1708

Enter a word or words to measure, or -1 to stop: Livro do Desassossego
The value of the word(s) 'Livro do Desassossego' is 2002.
Current total value: 3710

Enter a word or words to measure, or -1 to stop: The Margot Affair
The value of the word(s) 'The Margot Affair' is 1492.
Current total value: 5202

Enter a word or words to measure, or -1 to stop: Parangaricutirimicuaro

The final value is 5202
```

Keep the following limitations in mind:

- You can assume that the only non-alphabetic character that the user can include in their input is an empty space 
`' '`.
- Assume that the program enforces a value limitation of `5000`. That is, if the value of the user's input exceeds 
`5000` at any point, the program should stop.
- The exact formatting of your output isn't too important, just make sure you can see the final value at the end of your
program. For example, in my execution, the individual value of `"Parangaricutirimicuaro"` isn't displayed, but the final
total value is.

[**Solution**](value_of_words.py)