#!/usr/bin/env python


import pytest

from stack import Stack

def test_init():
    stack = Stack()
    assert stack.items.first is None

def test_push():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(789)
    assert stack.items.first.value == 789
    stack.push("Meaning of Life")
    stack.push("Life of Bwyan")
    assert stack.items.first.value == "Life of Bwyan"

def test_pop():
    stack = Stack()
    stack.push("Holy Grail")
    stack.push("And Now for Something Completely Different")
    p = stack.pop()

    assert p == "And Now for Something Completely Different"
    