from .Node import Node

'''
A singly linked list and its all operations
'''
class SinglyLinkedList:
      # a class construtor
      def __init__(self) -> None:
            self.head = None

      '''
            An insert method for the linked list
            responsible for the insert data at the end of the linkedlist
      '''
      def insert(self, data: int) -> None:
            new_node = Node(data)

            # check head is empty or not
            if self.head:
                  current_node = self.head
                  while(current_node.next):
                        current_node = current_node.next
                  current_node.next = new_node
            else:
                  self.head = new_node

      '''
      A display method to display all the data of the linkedlist
      '''
      def display(self) -> None:
            tmp_head = self.head
            while(tmp_head):
                  print(tmp_head.data, end=" ")
                  if tmp_head.next:
                        print("->", end=" ")
                  tmp_head = tmp_head.next
            print("")

      '''
      A delete function to delete the Head node from the list and
      make next head node
      '''
      def delete_head(self) -> int:
            current_head = self.head
            self.head = current_head.next
            return current_head.data
