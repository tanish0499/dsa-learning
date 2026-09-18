# Topic 08 - Recursion Exercises

Read [the lesson](../../../../lessons/08_recursion.md), then work in
[recursion.py](recursion.py). There are 20 exercises. Do 2 or 3 per session.

## Stage 1 - One Smaller Number

1. count_down
2. count_up
3. sum_to_n
4. sum_even_to_n

## Stage 2 - Repeat With Different Base Cases

5. factorial
6. power
7. sum_digits
8. count_digits

## Stage 3 - One List Item Per Call

9. sum_values
10. count_target
11. contains_value
12. maximum_value
13. first_index

## Stage 4 - Strings And Comparisons

14. reverse_text
15. count_character
16. remove_character
17. is_palindrome
18. is_sorted

## Stage 5 - Branching Recursion

19. fibonacci
20. count_stair_ways

Delay Stage 5 until you can trace and implement the earlier stages without
copying solutions. Extra advanced problems can wait until these are comfortable.

## Practice Routine

For each problem, write its promise, base case, smaller input, and how answers
combine. Draw the calls downward and returned results upward. An iterative
version can be a useful starting point; then implement the recursive version.
For list/string tasks, helpers with indices are welcome.

At the end of each stage, re-solve one earlier exercise without notes. If the
trace is unclear, repeat that stage before advancing. Tests check output and
input preservation; code review will also check that recursion is being used.

## Run Tests

From the repository root, run only this topic:

```powershell
python -m unittest exercises.python.topic_08_recursion.test_recursion
```

Or run just your current exercise:

```powershell
python -m unittest exercises.python.topic_08_recursion.test_recursion.TestRecursion.test_count_down
```

Unimplemented exercises skip. These tests target the practice file; reviewed
solutions will be stored separately when available.

Start with **count_down** and **count_up** only.
