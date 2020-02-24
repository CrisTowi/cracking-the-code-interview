"""
  Description: Given 2 strings, decide if one is a permutation of the other
  Author: Christian Consuelo
"""

# Using a chars hash table or python dict to add
# every single character and its count for the first
# string. Then with the second string rest the number
# of characters and check if the result is 0.
def is_permutation(string_1, string_2):
  chars = {}

  for c in string_1:
    if not c in chars:
      chars[c] = 1
    else:
      chars[c] += 1

  for c in string_2:
    if not c in chars:
      return False
    else:
      chars[c] -= 1

  for c in chars:
    if chars[c] != 0:
      return False

  return True

result_1 = is_permutation("christian", "naitsirhc")

print(result_1)
