# Topic 07 - Linked-List Exercises

Read `lessons/07_linked_lists.md` first.

Implement one function at a time in `linked_lists.py`, then run:

```powershell
python -m unittest discover -s exercises/python
```

Unimplemented functions are skipped.

## Order

Traversal repetitions (move one pointer, change only the answer being tracked):

1. `linked_list_length`
2. `sum_node_values`
3. `contains_value`
4. `count_occurrences`
5. `last_value`
6. `maximum_value`
7. `value_at_index`

Small link changes (draw the old arrow and the new arrow):

8. `prepend_value`
9. `append_value`
10. `insert_after_first`
11. `delete_head`
12. `delete_tail`
13. `delete_first_value`

Repeated link changes:

14. `reverse_linked_list`

Pointer patterns:

15. `middle_value`
16. `merge_sorted_lists`
17. `remove_nth_from_end`
18. `has_cycle`

Start with `linked_list_length` and `sum_node_values`. Draw `current` above
the node it references after every movement. Continue in the order above,
doing 2 or 3 exercises per session.

Before moving to the next section, re-solve one exercise from the current
section without notes and explain why each pointer moves. If that is still
unclear, repeat a similar exercise before adding another pattern.

The eight added exercises are tested in `test_linked_list_repetitions.py`.
All 18 implementations belong in `linked_lists.py`. Unless a question says
otherwise, inputs are finite, acyclic lists; only `has_cycle` includes cycles.
