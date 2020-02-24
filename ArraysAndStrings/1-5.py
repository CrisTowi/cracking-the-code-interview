"""
  Description: Identify if we can make 2 strings the same by applying
  one single edit operation (insert 1 char, remove a char, replace a char)
  Author: Christian Consuelo
"""

def one_way(string_1, string_2):
  pivot_1 = 0
  pivot_2 = 0
  diff = 0
  flag = False

  s1, s2 = None

  if len(string_1) > len(string_2):
    s1 = string_1
  else len(string_1) < len(string_2):
    s1 = 

  while (diff <= 2 and not flag):
    if pivot_1 == len(string_1) and pivot_2 == len(string_2):
      flag = True
    elif pivot_1 == len(string_1) and pivot_2 <= len(string_2):
      diff += len(string_2) - pivot_2
    elif pivot_2 == len(string_2) and pivot_1 <= len(string_1):
      diff += len(string_1) - pivot_1
    else:

      


result = one_way("pale", "ale")
print(result)
