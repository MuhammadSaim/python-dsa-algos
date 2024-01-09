'''
A doubly linked list node to store data and the addresses of the next/previous node
'''
class Node:
      def __init__(self, data: int) -> None:
            self.prev = None
            self.data = data
            self.next = None
