from .Node import Node

'''
A singly linked list and its all operations
'''
class SinglyLinkedList:
      # a class construtor
      def __init__(self) -> None:
            self.count: int = -1
            self.head: Node = None

      '''
            An insert method for the linked list
            responsible for the insert data at the end of the linkedlist
      '''
      def insert(self, data: int) -> None:
            new_node: Node = Node(data)

            # check head is empty or not
            if self.head:
                  current_node: Node = self.head
                  while(current_node.next):
                        current_node = current_node.next
                  current_node.next = new_node
            else:
                  self.head = new_node

            self.count += 1

      '''
      An insert method for the linked list
      responsible for the insert data at the given position of the linkedlist
      '''
      def insert_at(self, index, data) -> None:
            if self.count >= index:
                  tmp: Node = self.head

                  # check position is at start
                  if index == 0:
                        new_node: Node = Node(data)
                        new_node.next = tmp
                        self.head = new_node
                        self.count += 1
                        return

                  # loop through the list to find the index
                  for idx in range(index - 1):
                        tmp = tmp.next
                        if tmp is None:
                              break

                  new_node: Node = Node(data)
                  next = tmp.next
                  new_node.next = next
                  tmp.next = new_node
                  self.count += 1
            else:
                  print("Undefined location.")

      '''
      A display method to display all the data of the linkedlist
      '''
      def display(self) -> None:
            if self.count > 0:
                  tmp_head: Node = self.head
                  while(tmp_head):
                        print(tmp_head.data, end=" ")
                        if tmp_head.next:
                              print("->", end=" ")
                        tmp_head = tmp_head.next
                  print("")
            else:
                  print("LinkedList is empty.")

      '''
      A delete function to delete the Head node from the list and
      make next head node
      '''
      def delete_head(self) -> int|None:
            if self.count > 0:
                  current_head: Node = self.head
                  self.head = current_head.next
                  self.count -= 0
                  return current_head.data
            else:
                  print("Not able to delete linked list is empty")

      '''
      delete the node at the end of the linkedlist
      '''
      def delete_tail(self) -> int|None:
            if self.count > 0:
                  tmp_head: Node = self.head
                  while(tmp_head.next.next is not None):
                        tmp_head = tmp_head.next
                  data: int = tmp_head.data
                  tmp_head.next = None
                  self.count -= 1
                  return data
            else:
                  print("Not able to delete linked list is empty")

      '''
      delete the node at given index
      '''
      def delete_at(self, index) -> int|None:
            if self.count >= index:
                  tmp: Node = self.head

                  # check if position is 0 remove the head
                  if index == 0:
                        self.head = tmp.next
                        return tmp.data

                  # loop through the indexes less then given index to get the our point
                  for idx in range(index - 1):
                        tmp = tmp.next
                        if tmp is None:
                              break

                  next: Node = tmp.next.next
                  data: int = tmp.next.data
                  tmp.next = None
                  tmp.next = next
                  self.count -= 1
                  return data

            else:
                  print("Location is undefined.")


      '''
      A bsic search or you can a squetial search implementation on a
      SinglyLinkedList
      '''
      def search(self, value) -> None:
            if self.count > 0:
                  tmp_head: Node = self.head
                  flag: bool = False
                  index: int = 0
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
            else:
                  print("Linked list is empty not able to perform search.")
