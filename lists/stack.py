#!/usr/bin/env python

from linked import Linked_list

class Stack(object):
    def __init__(self):
        self.items = Linked_list()

    def push(self, data):
        self.items.insert(data)

    def pop(self):
        return self.items.pop_front()



