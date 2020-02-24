"""
  Description: Generate a compresed version of a string by replacing
  repeated characters with the character followed by the number of
  repetitions
  Author: Christian Consuelo
"""

def string_compression(string):
  if not string:
    return ""

  result = ""
  streak = 1

  for index, c in enumerate(string):
    if index == len(string) - 1:
      result += c + str(streak)
    else:
      next_c = string[index + 1]
      if c != next_c:
        result += c + str(streak)
        streak = 0
    
    streak += 1

  if len(result) >= len(string):
    return string

  return result

print(string_compression("aaaabbbbcccddddde"))
print(string_compression("aabcccccaaa"))
print(string_compression("abcdefg"))
