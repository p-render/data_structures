#test_linked.py

import pytest
import linked


items = linked.Linked_List()
"""
items.insert(5)
items.insert(4)
items.insert(3)
"""

def test_node_created():
    #assert value == 
    #assert self.next == ?
    pass


def test_linked_list_created():
    pass
        
def test_insert(value):
    items.insert(1)
    assert items.value == 1
    items.insert(None)
    assert items.value == None
    items.insert('words')
    assert items.value == 'words'


def test_pop_front():
    items.insert(3)
    items.pop_front()
    assert items.pop_front() == 3

def test_list_size():
    items.insert(5)
    items.insert(4)
    items.insert(3)
    items.list_size()
    assert items.list_size == 3

def test_search(value):
    iitems.insert(5)
    items.insert(4)
    items.insert(3)
    node = items.search(4)
    assert items.search(node) == 4

def test_remove_node(node):
    items.insert(5)
    items.insert(4)
    items.insert(3)
    items.list_size()
    assert items.list_size == 3
    items.remove_node(5)
    items.list_size()
    assert items.list_size == 2


def test_print_list():
    items.insert(5)
    items.insert(4)
    items.insert(3)
    x = items.test_print_list()
    assert str(x) == "(3, 4, 5)"