"""
  Description: Creates a stack that has the functionality min wich gets
  the minimun value in a O(1) complexity
  Author: Christian Consuelo
"""

class Node:
  def __init__(self, value, min):
    self.value = value
    self.min = min

class Stack:
  def __init__(self):
    self.data = []

  def push(self, value):
    if self.is_empty():
      self.data.append(Node(value, value))
    else:
      if value < self.peak().min:
        self.data.append(Node(value, value))
      else:
        self.data.append(Node(value, self.peak().min))

  def pop(self):
    if self.is_empty():
      return None

    return self.data.pop()

  def peak(self):
    if len(self.data) > 0:
      return self.data[-1]

    return None

  def is_empty(self):
    return len(self.data) == 0

  def min(self):
    if self.is_empty():
      return None
    
    return self.peak().min

stack = Stack()

stack.push(10)
stack.push(1)
stack.push(7)
stack.push(4)
stack.push(-2)

print(stack.min())

