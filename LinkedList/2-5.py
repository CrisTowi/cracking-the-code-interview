"""
  Description: Sum two numbers reprensented by a linked list
  representing each digit by a node value
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


def sum_lists(root_1, root_2):
  result = None
  current_list_node_1 = root_1
  current_list_node_2 = root_2
  remaining = 0

  while current_list_node_1 or current_list_node_2:
    r = 0

    if current_list_node_1 and current_list_node_2:
      r = current_list_node_1.value + current_list_node_2.value + remaining
      current_list_node_1 = current_list_node_1.next
      current_list_node_2 = current_list_node_2.next

    elif current_list_node_1:
      r = current_list_node_1.value + remaining
      current_list_node_1 = current_list_node_1.next

    elif current_list_node_2:
      r = current_list_node_1.value + remaining
      current_list_node_2 = current_list_node_2.next

    remaining = 0

    if r > 9:
      r = r % 10
      remaining = 1

    if not result:
      result = Node(r)
    else:
      result.append_to_tail(r)

  if remaining > 0:
    result.append_to_tail(remaining)

  return result

root_1 = Node(1)
root_1.append_to_tail(5)
root_1.append_to_tail(7)
root_1.append_to_tail(8)
root_1.append_to_tail(9)

root_2 = Node(5)
root_2.append_to_tail(1)
root_2.append_to_tail(2)
root_2.append_to_tail(4)
root_2.append_to_tail(5)

sum_lists(root_1, root_2).print_linked_list()
