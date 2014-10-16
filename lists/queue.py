#!/usr/bin/env python

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)

class Queue:
    """ Initialize a queue data structure with methods

    Size: returning the size of the queue
    Enqueue: adds items to the queue
    Dequeue: removes items from the queue
     """
    def __init__(self):
        self.length = 0
        self.head = None

    def size(self):
        """return the size of the queue"""
        return self.length

    def enqueue(self, value):
        """adds value to the queue"""
        node_value = Node(value)
        node_value.next = None
        if self.head == None:
            self.head = node_value
        else:
            last = self.head
            while last.next: 
                last = last.next
            last.next = node_value
        self.length = self.length + 1

    def dequeue(self):
        """removes the correct item from the queue and returns its value"""
        node_value = self.head.value
        self.head = self.head.next
        self.length = self.length - 1
        return node_value


i_queue = Queue()
i_queue.enqueue(45)
i_queue.enqueue('frogs')
i_queue.enqueue(1)
print i_queue.size()
print i_queue.dequeue()


