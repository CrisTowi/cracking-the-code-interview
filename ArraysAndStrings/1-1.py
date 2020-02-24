"""
  Description: Determines if a string has all unique characters
  Author: Christian Consuelo
"""

# Using a hash table or python dict
def is_unique_with_hash(string):
  chars = {}

  for c in string:
    if c in chars:
      return False
    else:
      chars[c] = True

  return True

# Brute force approach
def is_unique_without_hash(string):
  for i, c1 in enumerate(string):
    for j, c2 in enumerate(string[:i]):
      if c1 == c2:
        return False

  return True

input_string = "hOla mundO"

result_1 = is_unique_with_hash(input_string)
result_2 = is_unique_without_hash(input_string)

print(result_1)
print(result_2)
