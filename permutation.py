'''
Write a Python program to print all permutations with given repetition number of characters of a given string.
'''
from itertools import product
import textwrap
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results
print((all_repeat('xyz', 3))
