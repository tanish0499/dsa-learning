# 01 - Arrays And Strings Exercises

Open `arrays_strings.py` and implement the functions one by one.

Run tests from the repo root:

```powershell
python -m unittest discover -s exercises/python
```

Unimplemented functions are shown as `skipped`. That is normal.

After implementing one function, you should expect something like:

```text
OK (skipped=11)
```

That means your implemented function passed and the remaining functions are waiting for later.

To run only one function's test, use:

```powershell
python -m unittest exercises.python.topic_01_arrays_and_strings.test_arrays_strings.TestArraysAndStrings.test_sum_numbers
```

Replace `test_sum_numbers` with the test you want.

## Warm-Up Visualization

Before coding, trace these by hand:

1. For `[5, 1, 9, 2]`, show how `best` changes when finding the maximum.
2. For `[1, 2, 3]`, show how `result` changes when doubling each number.
3. For `"hello"`, show each character and its index.

## Beginner Exercises

1. `sum_numbers`
2. `count_even_numbers`
3. `find_maximum`
4. `contains_value`
5. `double_numbers`
6. `count_character`
7. `reverse_string`
8. `only_positive_numbers`

## Medium Exercises

9. `second_largest`
10. `move_zeroes_to_end`
11. `is_palindrome`
12. `compress_repeated_chars`

## How To Think

For every function, write a short trace before coding.

Example for `count_even_numbers([2, 5, 8])`:

```text
count = 0
see 2 -> even -> count = 1
see 5 -> odd  -> count = 1
see 8 -> even -> count = 2
return 2
```
