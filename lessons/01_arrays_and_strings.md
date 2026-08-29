# 01 - Arrays And Strings

Arrays are the first structure to master because many DSA patterns are just smarter ways of walking through arrays.

In Python, we usually use `list` for arrays.

```python
nums = [10, 20, 30, 40]
```

Visual:

```text
index:  0   1   2   3
value: 10  20  30  40
```

The index is the position.
The value is the thing stored at that position.

## Basic Operations

### Read By Index

```python
nums[2]  # 30
```

Visual:

```text
index:  0   1   2   3
value: 10  20  30  40
             ^
           nums[2]
```

### Loop Left To Right

```python
for num in nums:
    print(num)
```

Use this when you only care about values.

```python
for i in range(len(nums)):
    print(i, nums[i])
```

Use this when you need the index.

## Common Array Thinking Patterns

### 1. Scan And Track

You walk through the array and remember something.

Examples:

- biggest number so far
- smallest number so far
- sum so far
- count so far
- best answer so far

Visual:

```text
nums = [3, 8, 2, 10, 5]

best = 3
see 3  -> best 3
see 8  -> best 8
see 2  -> best 8
see 10 -> best 10
see 5  -> best 10
```

### 2. Build A New Result

You walk through input and create another list or string.

Example:

```text
nums = [1, 2, 3]
double each number
result = [2, 4, 6]
```

Plain steps:

```text
Create empty result.
For each number, append number * 2.
Return result.
```

### 3. Check A Condition

You walk until you find something true.

Example:

```text
Does the array contain 7?
```

Plain steps:

```text
Look at every number.
If number is 7, return True.
If loop ends, return False.
```

## Strings Are Arrays Of Characters

```python
word = "devops"
```

Visual:

```text
index: 0 1 2 3 4 5
char:  d e v o p s
```

You can loop through strings:

```python
for ch in word:
    print(ch)
```

Strings are immutable in Python, so when building a changed string, collect characters in a list and join them.

```python
chars = []

for ch in word:
    chars.append(ch.upper())

answer = "".join(chars)
```

## Beginner Problem Template

Use this every time:

```text
Input:
Output:
Small example:
Visual trace:
Variables to remember:
Plain English steps:
Code:
```

## When You Are Stuck

Ask:

1. Am I moving through the data left to right?
2. What variable should remember my progress?
3. Do I return immediately, or only after the loop ends?
4. Am I confusing index and value?

