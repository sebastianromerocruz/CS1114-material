<h2 align=center>Lecture 13<h2>

<h1 align=center><strong>Midterm 1 Review</strong>: Read Between The Lines</h1>

### 27 Vendémiaire, Year CCXXXI

***Song of the day:*** _[**Looking For Somebody To Love (Official Live Performance)**](https://youtu.be/ORCNXtnlD38) by The 1975 (2022)._

Let's say you wanted to decode a message that used the following encryption: Starting from the last character of the
sentence, you must read every X-th letter. If the character that you land on is a number, you must skip it. For instance:

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