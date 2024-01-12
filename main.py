from LinkedList.Singly.SinglyLinkedList import SinglyLinkedList
from LinkedList.Doubly.DoublyLinkedList import DoublyLinkedList

singly_linkedlist = SinglyLinkedList()
doubly_linkedlist = DoublyLinkedList()

doubly_linkedlist.display()
doubly_linkedlist.insert(5)
doubly_linkedlist.insert(7)
doubly_linkedlist.insert(2)
doubly_linkedlist.display()
doubly_linkedlist.delete_tail()
doubly_linkedlist.display()
