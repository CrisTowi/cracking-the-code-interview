"""
  Description: Replace all the spaces with %20
  Author: Christian Consuelo
"""

def URLify(string, string_length):
  result = ""

  for c in string:
    if c == " ":
      result += "%20"
    else:
      result += c

  return result

result = URLify("Hello darkness my old friend", 28)
print(result)
