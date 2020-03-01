"""
  Description: Detect if a linked list is a loop and detect the first node
  that represents the beginning of the loop
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


def loop_detection(root):
  current_node = root
  current_node_runner = root

  while current_node and current_node_runner.next:
    current_node = current_node.next
    current_node_runner = current_node_runner.next.next

    if current_node == current_node_runner:
      break

  if not current_node or not current_node_runner:
    return False

  current_node = root

  while current_node != current_node_runner:
    current_node = current_node.next
    current_node_runner = current_node_runner.next

  return current_node_runner

root = Node(1)

node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(8)
node_9 = Node(9)
node_10 = Node(10)

root.append_node_to_tail(node_2)
root.append_node_to_tail(node_3)
root.append_node_to_tail(node_4)
root.append_node_to_tail(node_5)
root.append_node_to_tail(node_6)
root.append_node_to_tail(node_7)
root.append_node_to_tail(node_8)
root.append_node_to_tail(node_9)
root.append_node_to_tail(node_10)
root.append_node_to_tail(node_4)

result = loop_detection(root)

print(result.value)
