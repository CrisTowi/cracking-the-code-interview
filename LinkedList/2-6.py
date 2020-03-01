"""
  Description: Detect if a linked list is a palindrome
  Author: Christian Consuelo
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def append_to_tail(self, value):
    new_node = Node(value)
    current_node = self

    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node

  def print_linked_list(self):
    current_node = self
    while current_node:
      print(current_node.value)
      current_node = current_node.next


def is_palindrome(root):
  stack = []

  current_node = root

  while current_node:
    stack.append(current_node.value)
    current_node = current_node.next

  current_node = root

  while current_node and stack.pop() == current_node.value:
    current_node = current_node.next
  
  return len(stack) == 0

root = Node(1)
root.append_to_tail(5)
root.append_to_tail(7)
root.append_to_tail(8)
root.append_to_tail(8)
root.append_to_tail(8)
root.append_to_tail(7)
root.append_to_tail(5)
root.append_to_tail(1)

print(is_palindrome(root))
