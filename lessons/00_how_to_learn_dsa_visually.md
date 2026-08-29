# 00 - How To Learn DSA Visually

Your current problem is not intelligence. It is missing mental pictures.

When you see a DSA problem, your brain is trying to jump directly from:

```text
problem statement -> code
```

That is too big a jump.

Instead, use this path:

```text
problem statement -> example -> visual trace -> plain English steps -> code
```

## The Core Method

For every problem, write these four things before coding:

1. What data do I have?
2. What answer do I need?
3. What changes step by step?
4. What do I need to remember while looping?

Example:

```text
nums = [4, 2, 7, 1]
Find the biggest number.
```

Visual trace:

```text
current best = 4

index 0 -> value 4 -> best stays 4
index 1 -> value 2 -> best stays 4
index 2 -> value 7 -> best becomes 7
index 3 -> value 1 -> best stays 7
```

Plain English:

```text
Start with the first number as best.
Look at each number.
If this number is bigger than best, replace best.
At the end, return best.
```

Code:

```python
def biggest(nums):
    best = nums[0]

    for num in nums:
        if num > best:
            best = num

    return best
```

## Why Courses Did Not Stick

Watching a full course first often feels clear while watching, but the exercises come too late.

For you, the order should be:

```text
small concept -> tiny visual example -> tiny code -> many exercises
```

Then repeat.

## Your Rule

Never say "I do not know the optimal solution" and stop.

Instead say:

```text
Can I solve it slowly first?
Can I draw the movement?
Can I track one useful variable?
```

Slow correct code is the bridge to better code.

## Practice Habit

For each exercise in this repo:

1. First trace with a small example.
2. Write plain English steps.
3. Write code.
4. Run tests.
5. If stuck, write where your visualization broke.

