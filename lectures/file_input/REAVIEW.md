## Lecture 18

# File Input

### 13 Germinal, Year CCXXX

***Song of the day***: _[**La Javanaise**](https://youtu.be/gPICcSvTRv8) by Khatia Buniatishvili (2020)._

---

### Part 1: _Warm-up_

Let's warm up with a quick problem, very similar to the one we did last week.

Let's say we have a list of strings, and each string contained a series of numbers separated by a single blank space:

```python
sample_list = [
    '50.98 82.72 89.18 51.57 23.95 69.82', 
    '57.7 13.08 1.26 6.15 52.09 42.63 39.46', 
    '96.21 43.32 79.45 7.87 10.5 10.92 67.87 21.22', 
    '27.27 40.23 79.09 17.56 75.87 80.38 40.98 6.21 44.72 36.45', 
    '0.07 29.63 97.73 58.01 97.47 24.07 83.46 99.4', 
    '14.03 55.63 31.57 0.01 73.4 91.35 82.06 59.62 2.83 93.04'
]
```

Your goal to create a function, `get_sums()`, that accepts such a list, and returns a list of their sums:

```python
sample_list = [
    '50.98 82.72 89.18 51.57 23.95 69.82', 
    '57.7 13.08 1.26 6.15 52.09 42.63 39.46', 
    '96.21 43.32 79.45 7.87 10.5 10.92 67.87 21.22', 
    '27.27 40.23 79.09 17.56 75.87 80.38 40.98 6.21 44.72 36.45', 
    '0.07 29.63 97.73 58.01 97.47 24.07 83.46 99.4', 
    '14.03 55.63 31.57 0.01 73.4 91.35 82.06 59.62 2.83 93.04'
]

sums = get_sums(sample_list)

print(sums)
```

Output:

```text
[368.22, 212.37, 337.36, 448.76, 489.84, 503.54]
```