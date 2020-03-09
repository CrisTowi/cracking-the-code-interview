"""
  Description: Detect Determine if 2 linked lists are intersected
  and get the intersection node
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

  def append_node_to_tail(self, node):
    current_node = self

    while current_node.next:
      current_node = current_node.next

    current_node.next = node

  def print_linked_list(self):
    current_node = self
    while current_node:
      print(current_node.value)
      current_node = current_node.next


def get_tail_and_length(node):
  current_node = node
  length = 1

  while current_node.next:
    length += 1
    current_node = current_node.next

  return (current_node, length)

def get_bigger_smaller(root_1, root_2, length_1, length_2):
  if length_1 > length_2:
    bigger = root_1
    smaller = root_2
  else:
    bigger = root_2
    smaller = root_1

  return (bigger, smaller)

def are_two_linked_lists_intersected(root_1, root_2):
  tail_1, length_1 = get_tail_and_length(root_1)
  tail_2, length_2 = get_tail_and_length(root_2)

  if tail_1 != tail_2:
    return False

  diff = abs(length_1 - length_2)
  bigger, smaller = get_bigger_smaller(root_1, root_2, length_1, length_2)

  # Move bigger root linked list to the same relative node that smaller
  while diff > 0:
    bigger = bigger.next
    diff -= 1

  # While bigger and smaller are different go through them
  while bigger != smaller:
    bigger = bigger.next
    smaller = smaller.next

  # Now that both pointers are the same just need to return any of them
  return bigger

root_1 = Node(1)
root_2 = Node(2)

node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(8)
node_9 = Node(9)
node_10 = Node(10)

root_1.append_node_to_tail(node_3)
root_1.append_node_to_tail(node_4)
root_1.append_node_to_tail(node_5)
root_1.append_node_to_tail(node_7)


root_2.append_node_to_tail(node_6)
# node_7 is the intersection node
root_2.append_node_to_tail(node_7)

root_1.append_node_to_tail(node_8)
root_1.append_node_to_tail(node_9)
root_1.append_node_to_tail(node_10)

result = are_two_linked_lists_intersected(root_1, root_2)

if result:
  print(result.value)
else:
  print('No intersection found')
