"""
  Description: Check if an string is a permutation of a palindome
  Author: Christian Consuelo
"""

def palindrome_permutation(string):
  chars = {}
  odd_numbers = 0

  # Stores every character grouped in the chars dict
  for c in string:
    c = c.lower()
    if c != " ":
      if not c in chars:
        chars[c] = 1
      else:
        chars[c] += 1

  # The rule to have a palindrome permutation is that
  # there are only even number of repetitions on each
  # character or at most 1 odd repetition that will be
  # the middle pivot
  for c in chars:
    if chars[c] % 2 != 0:
      odd_numbers += 1

  return odd_numbers <= 1

result = palindrome_permutation("Anita lava la tina")
print(result)
