from LinkedList.Doubly.Node import Node

'''
A doubly linked list and its all operations
'''
class DoublyLinkedList:

      # a class construtor
      def __init__(self) -> None:
            self.count: int = -1
            self.head: Node = None

      '''
      insert node at the end of the list
      '''
      def insert(self, data: int) -> None:

            new_node: Node = Node(data)

            if self.head:
                  current_node: Node = self.head
                  while(current_node.next):
                        current_node = current_node.next
                  current_node.next = new_node
                  new_node.prev = current_node
                  self.count += 1
            else:
                  self.head = new_node
                  self.count += 1

      '''
      insert into a specific position of a linked list
      '''
      def insert_at(self, index: int, data: int) -> int|None:
            if self.count >= 0 or self.count <= index:
                  new_node: Node = Node(data)
                  if index == 0:
                        new_node.next = self.head
                        self.head = new_node
                        self.count += 1
                        return new_node.data

                  tmp_node: Node = self.head
                  for i in range(index - 1):
                        tmp_node = tmp_node.next
                        if tmp_node is None:
                              break

                  next_node: Node = tmp_node.next
                  new_node.prev = tmp_node
                  new_node.next = next_node
                  tmp_node.next = new_node
                  self.count += 1
                  return new_node.data
            else:
                  print('Invalid index')


      '''
      delete head of the linked list
      '''
      def delete_head(self) -> int|None:
            if self.head:
                  data: int = self.head.data
                  self.head = self.head.next
                  return data
            else:
                  print("Linked list is not initialized yet")

      '''
      delete tail node in dubly linked list
      '''
      def delete_tail(self) -> int|None:
            if self.count >= 0:
                  tmp_node: Node = self.head

                  while(tmp_node.next.next is not None):
                        tmp_node = tmp_node.next

                  data: int = tmp_node.data
                  tmp_node.next = None
                  self.count -= 1
                  return data
            else:
                  print('Invalid index')

      '''
      delete node in a linked list at specific position
      '''
      def delete_at(self, index: int) -> int|None:
            if self.count >= 0:
                  tmp_node: Node = self.head

                  if index == 0:
                        data: int = self.head.data
                        self.head = self.head.next
                        self.count -= 1
                        return data

                  for i in range(index - 1):
                        tmp_node = tmp_node.next
                        if tmp_node is None:
                              break

                  data: int = tmp_node.next.data
                  next: Node = tmp_node.next.next
                  tmp_node.next = next
                  next.prev = tmp_node
                  self.count -= 1
                  return data

            else:
                  print('Linked list not created yet.')

      '''
      A bsic search or you can a squetial search implementation on a
      DoublyLinkedList
      '''
      def search(self, value: int) -> None:
            if self.count > 0:
                  tmp_head: Node = self.head
                  flag: bool = False
                  index: int = 0

                  while(tmp_head):
                        index += 1
                        if tmp_head.data == value:
                              flag = True
                              break
                        else:
                              flag = False
                        tmp_head = tmp_head.next

                  if(flag):
                        print(f"{value} is found at {index} index")
                  else:
                        print("No Value found")

            else:
                  print("Linked list is empty not able to perform search.")


      '''
      A display method to display all the data of the linkedlist
      '''
      def display(self) -> None:
            if self.count > 0:
                  tmp_head: Node = self.head
                  while(tmp_head):
                        print(tmp_head.data, end=" ")
                        if tmp_head.next:
                              print("⇄", end=" ")
                        tmp_head = tmp_head.next
                  print("")
            else:
                  print("LinkedList is empty.")
