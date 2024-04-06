#!/usr/bin/env python3

""" 
COUNTING SUBSTRING IN THE GIVEN STRING:
We can find the number of occurrences of substring present in the given string by using count() method.
- s.count(substring) -> It will search through out the string.
- s.count(substring, bEgin, end) -> It will search from bEgin index to end-1 index.
"""

s = "abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,7))
