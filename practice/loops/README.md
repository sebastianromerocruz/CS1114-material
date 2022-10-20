<h2 align=center>Review<h2>

<h1 align=center>Loops and Strings</h1>

[***Solutions***](SOLUTIONS.md)

### 1. What will be printed by the following code snippets?

```python
string = "new york university"

for i in range(len(string)):
    print(string[i], end='')
```
```python
string = "NYU"

for i in range(len(string)):
    print(string[i] * i, end='')
```
```python
string = "NYU Tandon"

for i in range(len(string)):
    print(string[i // 2], end='')
```
```python
string = "New York University"

for i in range(len(string)):
    if i % 2 == 0:
        print(string[-1 * i], end='')
```
```python
string = "Brooklyn"

for i in range(len(string) // 2):
    for j in range(i):
        print(string[j] * i, end='')
```
```python
string = "NYU"

index = len(string) - 1

while index > 0:
    for i in range(index):
        print(string[i], end='')
    index //= 2
```
```python
word = "kandinsky"
index = len(word)

for i in word:
    print(i + str(index), end='')
    index -= 1
```

### 2. What is the final value of `word` in each of these situations?

```python
word = "nyu"
word.capitalize()
```
```python
word = "nyu"
word = word.upper()
```
```python
word = "brooklyn"
word = word[len(word) // 2]
```
```python
word = "new york university"
word[::-1]
```
```python
word = "NYU Tandon"
word = word[len(word) // 2::2]
```
```python
word = "New York University"
word = word[len(word) - 1::-3]
```
```python
word = "brooklyn"
vowels = "aeiou"
temp = ""

for i in range(len(word)):
    if word[i] in vowels:
        print(i)
    elif word[i] == 'y':
        print('y' * i)
    else:
        temp += word[i]

word = temp[::-1]
```
```python
word = "word"
word = len(word) * word[:len(word) // 2]
```
```python
word = "lswaswedeRfrt;poloNkisjuIhyegtmfrideT"
word = word[len(word) - 1::-3]
```

### 3.

