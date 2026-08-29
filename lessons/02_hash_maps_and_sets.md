# 02 - Hash Maps And Sets

Hash maps and sets are used when you need to remember things while scanning.

In Python:

```python
counts = {}       # hash map / dictionary
seen = set()      # set
```

## The Mental Picture

An array is like numbered boxes:

```text
index:  0   1   2
value: 10  20  30
```

A hash map is like labeled boxes:

```text
key      value
"a"  ->  3
"b"  ->  1
"c"  ->  5
```

A set is like a bag of unique things:

```text
seen = {"a", "b", "c"}
```

You do not care how many times something appears in a set. You only care whether it exists.

## When To Use A Set

Use a set when the question is:

```text
Have I seen this before?
Does this value exist?
Are there duplicates?
```

Example:

```python
def has_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

Visual trace:

```text
nums = [3, 1, 4, 3]

seen = {}
see 3 -> not seen -> add 3 -> {3}
see 1 -> not seen -> add 1 -> {3, 1}
see 4 -> not seen -> add 4 -> {3, 1, 4}
see 3 -> already seen -> return True
```

## When To Use A Hash Map

Use a hash map when the question is:

```text
How many times?
What value belongs to this key?
Can I group things by some label?
```

Example:

```python
def count_letters(text):
    counts = {}

    for ch in text:
        if ch not in counts:
            counts[ch] = 0

        counts[ch] += 1

    return counts
```

Visual trace:

```text
text = "banana"

see b -> {"b": 1}
see a -> {"b": 1, "a": 1}
see n -> {"b": 1, "a": 1, "n": 1}
see a -> {"b": 1, "a": 2, "n": 1}
see n -> {"b": 1, "a": 2, "n": 2}
see a -> {"b": 1, "a": 3, "n": 2}
```

## Most Common Beginner Patterns

### 1. Seen Set

```text
Create empty set.
Loop through values.
If value is already in set, use that information.
Otherwise add it.
```

### 2. Frequency Map

```text
Create empty dictionary.
Loop through values.
If key is missing, create it with 0.
Add 1 to that key.
```

### 3. Lookup Map

```text
Store useful information by key.
Later, ask the dictionary for that key quickly.
```

## The Important Difference

Set:

```text
Do I have this?
```

Dictionary:

```text
What value is connected to this key?
```

## Tiny Syntax Reference

```python
seen = set()
seen.add("a")
"a" in seen
```

```python
counts = {}
counts["a"] = 1
counts["a"] += 1
"a" in counts
counts["a"]
```

## Stuck Questions

Ask:

1. Do I only need existence? Use a set.
2. Do I need a count or stored value? Use a dictionary.
3. What should the key be?
4. What should the value be?

