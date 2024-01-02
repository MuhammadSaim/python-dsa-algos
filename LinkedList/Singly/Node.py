'''
A singly linked list node to store data and the address of the next node
'''
class Node:
      def __init__(self, data: int, next = None) -> None:
            self.data = data
            self.next = next

      def __str__(self) -> str:
            return '<{data} at {address}>'.format(data=self.data, address=hex(id(self.next)))
