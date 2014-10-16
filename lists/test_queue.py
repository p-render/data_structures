#!/usr/bin/env python

import pytest
from queue import Node, Queue

items = Queue()

def test_size():
    i = items.size()
    assert i == 0

def test_enqueue():
    items.enqueue(9)
    items.enqueue(10)
    items.enqueue(11)
    items.enqueue('This one goes to 11')  
    assert items.head.value == 9

def dequeue():
    items.enqueue(1)
    items.enqueue(2)
    front = items.dequeue()
    assert front == 1

