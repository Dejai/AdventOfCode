# Advent of Code - 2023

Private leader board: https://adventofcode.com/2023/leaderboard/private/view/1403088 

This year, wil use a single folder/package for helpers. Makes it easier to re-use each day & modify in one place if need-be

To do this, I did the following:

* Add a folder for the helper .py files
* Add a single (empty) .py file == "\__init__.py"
* Add the different helper module .py files
* Add path to the mypackage folder in the PYTHONPATH env variable

## Packages

Some packages that I've found useful when doing AoC problems

* from functools import cmp_to_key
* from collections import deque
* from collections import counter   # Can be used to get frequency count of items in a string, list, etc.
* import math
