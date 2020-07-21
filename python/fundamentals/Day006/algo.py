class Node(object):
  def __init__(self, value):
    self.val = value
    self.next = None

class SLL(object):
  def __init__(self):
    self.head = None

my_list = SLL()
print(my_list)

my_first_node = Node(4)
print(my_first_node)
