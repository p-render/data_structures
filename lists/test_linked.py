#!/usr/bin/env python

import pytest
from linked import Node, Linked_list


items = Linked_list()
"""
items.insert(5)
items.insert(4)
items.insert(3)
"""

def test_print_list():
    items.insert(5)
    items.insert(4)
    items.insert(3)
    x = items.print_list()
    assert str(x) == "(3, 4, 5)"
        
def test_insert():
    items.insert(1)
    assert items.first.value == 1
    items.insert(None)
    assert items.first.value == None
    items.insert('words')
    assert items.first.value == 'words'

def test_pop_front():
    items.insert(3)
    items.insert(4)
    items.pop_front()
    assert items.pop_front() == 3

def test_list_size():
    items.list_size()
    assert items.list_size() == 6

def test_search():
    items.insert(5)
    items.insert(4)
    items.insert(3)
    node = items.search(4)
    assert node.value == 4

def test_remove_node():
    assert items.remove_node(1) == None 

