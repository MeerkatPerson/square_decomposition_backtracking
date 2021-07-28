
# Decomposing an integer number into square numbers using backtracking.

A square number is an integer with an integer square root (0, 1, 4, 9, 16, 25, ... are square numbers). Interestingly, the spacing between pairs of square numbers is the ascending sequence of odd numbers: 1 - 0 = 1, 4 - 1 = 3, 9 - 4 = 5, 16 - 9 = 7 and so on.

This program provides all unique decompositions of an integer into square numbers, so that these add up to the provided number. 

Sample execution: `python3 square_decomposition_backtracking.py 25` (25 being the number to compute the decomposition for).

The applied algorithmic principle is backtracking, consisting of the following main steps: 

```
Start with an empty solution
Recursion:
    Generate candidates for the next step in the current partial solution (1)
    For each candidate:
        Execute step (2) (here: add number)
        If this results in a solution, save/print (3)
        Enter recursion for next step
        Undo step if necessary (4) (not necessary in this scenario) 
```

Not efficient for larger numbers due to exponential growth (backtracking traverses a search space exhaustively).