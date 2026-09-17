# 02 - Hash Maps And Sets Exercises

Open `hash_maps_sets.py` and implement one function at a time.

Run tests from the repo root:

```powershell
python -m unittest discover -s exercises/python
```

Unimplemented functions are shown as `skipped`.

## Warm-Up Visualization

Trace these by hand before coding:

1. For `[2, 5, 2, 9]`, show how a `seen` set changes while checking duplicates.
2. For `"hello"`, show how a character count dictionary changes.
3. For `["dev", "ops", "dev"]`, show how a word count dictionary changes.

## Beginner Exercises

1. `has_duplicate`
2. `count_values`
3. `count_characters`
4. `first_repeated_value`
5. `unique_values`
6. `most_frequent_value`

## Medium Exercises

7. `two_sum`
8. `is_anagram`
9. `group_words_by_first_letter`
10. `first_non_repeating_character`

## Repetition Ladder

Use `practice_ladder.py` between the main exercises:

1. After `has_duplicate`: `contains_all_values`.
2. After `unique_values`: `common_values_once`.
3. After `count_values`: `count_words`, then `values_appearing_once`.
4. Before `is_anagram`: `same_frequencies`.
5. Before `group_words_by_first_letter`: `group_words_by_length`.

These repeat the choice between set membership and dictionary frequencies
before combining those ideas in medium problems.

## How To Think

For each problem, decide first:

```text
Do I need a set or a dictionary?
What is the key?
What is the value?
```

Example for `has_duplicate([2, 5, 2])`:

```text
seen = {}
see 2 -> not present -> add 2
seen = {2}
see 5 -> not present -> add 5
seen = {2, 5}
see 2 -> already present -> return True
```
