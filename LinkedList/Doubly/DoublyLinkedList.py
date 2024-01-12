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
      def insert(self, data: int) -> None:

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
      delete tail node in dubly linked list
      '''
      def delete_tail(self) -> int|None:
            if self.count >= 0:
                  tmp_node = self.head

                  while(tmp_node.next.next is not None):
                        tmp_node = tmp_node.next

                  data = tmp_node.data
                  tmp_node.next = None
                  self.count -= 1
                  return data
            else:
                  print('Invalid index')

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
