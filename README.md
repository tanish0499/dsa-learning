# DSA Learning Project

This repo is your slow, practical path into data structures and algorithms.

The focus is not memorizing LeetCode tricks. The focus is:

1. Visualize what the data structure is doing.
2. Explain the steps in plain English.
3. Convert those steps into small code.
4. Practice enough that the pattern becomes familiar.

Default practice language: Python.

If you prefer JavaScript, Java, Go, or C++, we can convert the exercises later.

## How To Use This Project

For each topic:

1. Read the lesson in `lessons/`.
2. Do the warm-up visualization exercises.
3. Solve beginner coding exercises first.
4. Run the tests for feedback.
5. Only then move to medium exercises.

Do not jump to LeetCode hard problems early. That creates frustration without building the mental model.

## Repository Layout

```text
lessons/    Visual explanations for each topic
exercises/  Clean problem stubs used for practice and revision
attempts/   Original code written during learning sessions
solutions/  Cleaned and reviewed reference implementations
tricks/     Short technique-selection and visualization guides
tools/      Small repository maintenance utilities
```

Keeping attempts and reviewed solutions separate makes progress visible without
turning the exercise files into an answer sheet.

## Current Track

| Step | Topic | Status |
| --- | --- | --- |
| 00 | How to learn DSA visually | Ready |
| 01 | Arrays and strings | Ready |
| 02 | Hash maps and sets | Ready |
| 03 | Two pointers | Ready |
| 04 | Sliding window | Ready |
| C1 | Mixed foundations checkpoint | Complete |
| 05 | Stack | Complete (solution sync pending) |
| 06 | Queue | Complete (solution sync pending) |
| 07 | Linked list | Ready |
| 08 | Recursion | Planned |
| 09 | Trees | Planned |
| 10 | Binary search | Planned |
| 11 | Heap / priority queue | Planned |
| 12 | Graphs | Planned |
| 13 | Dynamic programming basics | Planned |

See `roadmap.md` for the full staged plan and revision schedule.

## Daily Routine

A good 45 to 60 minute session:

1. 10 minutes: revise yesterday's visual notes.
2. 15 minutes: trace examples by hand.
3. 25 minutes: solve 2 to 4 small exercises.
4. 5 minutes: write what pattern you used in `progress.md`.

The important part is repetition. Since you forget fast right now, we will use spaced revision and small problems instead of long theory sessions.

## Running Tests

To test your current work in `exercises/`:

```powershell
python -m unittest discover -s exercises/python
```

Unimplemented functions are skipped, so you can work on one function without
errors from later exercises.

To validate all reviewed solutions:

```powershell
$env:DSA_TEST_TARGET = "solutions"
python -m unittest discover -s exercises/python
Remove-Item Env:DSA_TEST_TARGET
```

GitHub Actions runs this solution mode automatically on pushes and pull requests.

## Quick Decision Guides

When you are unsure which technique or structure fits, check `tricks/`.
These are short references such as sliding-window `if` versus `while`, and set
versus dictionary. We will keep adding guides when a reusable confusion appears.
