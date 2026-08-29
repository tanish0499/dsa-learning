# Set Or Dictionary?

## Fast Rule

```text
Need to know whether a value exists?       Use a set.
Need to know how many copies exist?        Use a dictionary.
```

## What A Set Remembers

A set remembers membership only:

```python
window = {"a", "b"}
```

Adding `"a"` again changes nothing:

```python
window.add("a")
# still {"a", "b"}
```

This is not mainly an ordering problem. The set has lost occurrence
information: it cannot tell whether the window contains one `"a"` or three.

Use a set when the question is:

- Have I seen this value?
- Is this value already in the valid window?
- Does an intersection contain this value?

Examples:

- `has_duplicate`;
- `first_repeated_value`;
- `has_nearby_duplicate` when we return as soon as a duplicate is found;
- `longest_unique_substring`, because the maintained valid window has one copy
  of each character.

## What A Dictionary Remembers

A frequency dictionary remembers membership and count:

```python
counts = {"a": 2, "b": 1}
```

When one `"a"` leaves:

```python
counts["a"] -= 1
# {"a": 1, "b": 1}
```

The dictionary correctly remembers that another `"a"` remains.

Use a dictionary when the question is:

- How many times does each value occur?
- Can duplicates remain while the window continues sliding?
- Must one outgoing copy be removed while another copy stays?
- Must two frequency collections be compared?
- How many distinct keys are currently present?

Examples:

- character counts and anagram checks;
- `count_distinct_windows`;
- `find_anagram_indices`;
- longest window with at most `k` distinct values;
- longest repeating substring after replacements.

## Why A Set Fails For Some Windows

Consider the window `"aba"`:

```text
Actual characters: a, b, a
Set:               {a, b}
Dictionary:        {a: 2, b: 1}
```

If the left `"a"` leaves, another `"a"` remains.

Removing `"a"` from the set produces `{b}`, which is wrong. Decreasing the
dictionary count produces `{a: 1, b: 1}`, which is correct.

## What About Order?

Use the input scan or a result list to preserve order. A set can help prevent
duplicates while the list stores output order:

```python
seen = set()
result = []

for value in values:
    if value not in seen:
        seen.add(value)
        result.append(value)
```

The set answers membership; the list preserves order.

## Decision Checklist

```text
Only membership matters?
    Set.

Counts matter or duplicates may coexist?
    Dictionary.

Output order matters too?
    Keep a list for output, plus a set or dictionary for state.
```
