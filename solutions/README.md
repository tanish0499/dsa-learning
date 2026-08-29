# Reference Solutions

These are cleaned and reviewed solutions for completed topics. Try each problem
in `exercises/` before reading its reference implementation.

To validate all completed reference solutions from the repository root:

```powershell
$env:DSA_TEST_TARGET = "solutions"
python -m unittest discover -s exercises/python
Remove-Item Env:DSA_TEST_TARGET
```

Some checkpoint problems include both `_brute_force` and optimized functions so
the repeated work removed by the optimized technique remains visible.
