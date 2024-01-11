from LinkedList.Doubly.Node import Node

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
                  while(current_node.next):
                        current_node = current_node.next
                  current_node.next = new_node
                  new_node.prev = current_node
                  self.count += 1
            else:
                  self.head = new_node
                  self.count += 1

      '''
      A display method to display all the data of the linkedlist
      '''
      def display(self) -> None:
            if self.count > 0:
                  tmp_head = self.head
                  while(tmp_head):
                        print(tmp_head.data, end=" ")
                        if tmp_head.next:
                              print("⇄", end=" ")
                        tmp_head = tmp_head.next
                  print("")
            else:
                  print("LinkedList is empty.")
