"""
  Description: Partition a linked list in elements lower than
  the pivot to the left and bigger or equal to the pivot to 
  the right
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


def partition(root, pivot):
  current_node = root
  left_root = None
  right_root = None

  while(current_node):
    if current_node.value < pivot:
      if not left_root:
        left_root = Node(current_node.value)
        current_left_node = left_root
      else:
        left_root.append_to_tail(current_node.value)
        current_left_node = current_left_node.next
    else:
      if not right_root:
        right_root = Node(current_node.value)
      else:
        right_root.append_to_tail(current_node.value)
        
    current_node = current_node.next

  current_left_node.next = right_root

  return left_root

root = Node(1)

root.append_to_tail(5)
root.append_to_tail(7)
root.append_to_tail(8)
root.append_to_tail(9)
root.append_to_tail(1)
root.append_to_tail(2)
root.append_to_tail(4)
root.append_to_tail(5)

partition(root, 5).print_linked_list()
