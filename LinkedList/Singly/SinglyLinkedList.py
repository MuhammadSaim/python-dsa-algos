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

      '''
      delete the node at the end of the linkedlist
      '''
      def delete_tail(self) -> int:
            tmp_head = self.head
            while(tmp_head.next.next is not None):
                  tmp_head = tmp_head.next
            data = tmp_head.data
            tmp_head.next = None
            return data

      '''
      A bsic search or you can a squetial search implementation on a
      SinglyLinkedList
      '''
      def search(self, value) -> None:
            tmp_head = self.head
            flag = False
            index = 0
            # loop through the linkedlist if found the value turn true the flaf
            while(tmp_head):
                  index += 1
                  if tmp_head.data == value:
                        flag = True
                        break
                  else:
                        flag = False
                  tmp_head = tmp_head.next

            if flag:
                  print(f"{value} is found at {index} index")
            else:
                  print("No Value found")
