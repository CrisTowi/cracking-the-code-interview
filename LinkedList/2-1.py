"""
  Description: Remove a duplicated element on a linked list
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

  def remove_dups(self):
    dups = {}
    current_node = self
    prev_node = None

    while current_node:
      if not current_node.value in dups:
        prev_node = current_node
        dups[current_node.value] = True
        current_node = current_node.next
      else:
        prev_node.next = current_node.next
        current_node = current_node.next

root = Node(1)

root.append_to_tail(2)
root.append_to_tail(10)
root.append_to_tail(3)
root.append_to_tail(3)
root.append_to_tail(10)

root.remove_dups()

root.print_linked_list()
