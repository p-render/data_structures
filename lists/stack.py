#!/usr/bin/env python

from linked import Linked_list

class Stack(object):
    def __init__(self):
        self.items = Linked_list()

    def push(self, data):
        self.items.insert(data)

    def pop(self):
        return self.items.pop_front()





"""
Add an implementation of a Stack (Links to an external site.) to your 
data-structures repository.  This class should implement two methods:

push(data) - Adds a data element to the stack
The parameter is the data element to add to the stack.

pop() - Removes a data element from the stack and returns the value of 
that data element.  If the stack is empty, attempts to call pop should 
raise an appropriate Python exception class.

Your implementation is not allowed to use the built-in Python list, 
tuple or dictionary.  Nor are you allowed to use any of the native 
implementations of stack/queue/dequeue from the queue python standard 
library module.

Your implementation must include unit tests.  For each method on your 
stack class, including the constructor, write your tests first, then 
implement the methods that will support them. Be thorough in your tests, 
test failure modes as well as successes.

Update the repository README with information about the Stack you 
implemented, including any resources or collaborations you used.
"""
