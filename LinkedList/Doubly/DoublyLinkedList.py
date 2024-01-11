from .Node import Node

'''
A doubly linked list and its all operations
'''
class DoublyLinkedList:

      # a class construtor
      def __init__(self) -> None:
            self.count = -1
            self.head = None

      '''
      insert node at the end of the list
      '''
      def insert(self, data) -> None:

            new_node = Node(data)

            if self.head:
                  current_node = self.head
                  while(current_node):
                        current_node = current_node.next
                  current_node.next = new_node
                  new_node.prev = current_node
            else:
                  self.head = new_node
