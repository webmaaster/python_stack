class Node(object):
    def __init__(self):
      self.head = None 

      self.next = None

class SLL(object):
    def __init__(self):
        self.head= None

    def display_values(self):
        runner = my_list.head 
        while(runner != None)
          print(runner.val)
          runner = runner.next

    def find_max(self):
        max = my_list.head
        runner = my_list.head
        while(runner != None)
          print(runner.val)
          if max.val < runner.val:
            max = runner
            runner = runner.next
          else:
            runner = runner.next
        print("*"*20)
        print(max.val)
        print("*"*20)

    def lenth(self):
        #return  the number of nodes in the list

# creating the SSL
my_list = SSL()
print(my_list)

my_list_node = my_first_node
print(my_list.head)

my_second_node = Node(3)
print(my_second_node)
my_first_node.next = my_second_node
print(my_list.head.next)




    

 