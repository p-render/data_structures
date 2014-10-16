#linked.py

class Node(object):
    """creates a node with a value and connection to the next
        value in a linked list."""
    def __init__(self, value, next1):
        self.value = value
        self.next1 = next1


class Linked_list(object):
    """collection of methods for implementing a linked list."""
    def __init__(self):
        self.first = None
        
    def insert(self, value):
        """inserts the value at the head of the list"""
        new_node = Node(value, self.first)
        new_node.next1 = self.first
        self.first = new_node

    def pop_front(self):
        """pop the first value off the head of the list and return it."""
        if self.first != None:
            val_returned = self.first.value
            self.first = self.first.next1
            return val_returned

    def print_list(self):
        """print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')" """
        list_tuple = ()
        node_copy = self.first
        while node_copy != None:
            list_tuple += (node_copy.value,)
            node_copy = node_copy.next1
        print list_tuple
        return list_tuple

    def list_size(self):
        """returns the length of the list"""
        node_copy = self.first
        count = 0
        while node_copy != None:
            node_copy = node_copy.next1
            count += 1
        return count

    def search(self, value):
        """returns the node containing 'value' in the list, 
        if present, else None"""
        node_copy = self.first
        while node_copy != None:
            if node_copy.value == value:
                return node_copy
            node_copy = node_copy.next1
        return None    
        #if it's not there return None.   
        
    def remove_node(self, node):
        '''removes the given node from the list, wherever 
        it might be (node must be an item in the list)'''
        #if the first node is the one reset self.first to the next one.
        if self.first == node:
            pop_front()
        #traverse list to find node and reset previous.next to following.first
        else:
            current = self.first
            previous = None
            while current != None:
                if current != node:
                    previous = current
                    current = current.next1
                else:
                    previous.next1 = current.next1
                    return    


