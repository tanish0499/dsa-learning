# DSA Quick Tricks

This folder contains short decision guides for moments when you understand the
individual structures but are unsure which one fits a problem.

Read these as checklists, not as formulas to memorize blindly.

## Guides

1. [`01_sliding_window_if_vs_while.md`](01_sliding_window_if_vs_while.md)
   - Fixed-size versus condition-based windows
   - When one removal is enough
   - When the left pointer must move repeatedly
2. [`02_set_vs_dictionary.md`](02_set_vs_dictionary.md)
   - Membership versus frequency
   - Why sets lose duplicate information
   - Which structure fits common window problems
3. [`03_visualizing_sliding_windows.md`](03_visualizing_sliding_windows.md)
   - A paper-tracing method using one row per pointer movement
   - How expansion and shrinking alternate
   - A reusable table to complete before writing code

For a new problem, first say what information must remain true about the
current state. Then choose the structure that can represent that information.
