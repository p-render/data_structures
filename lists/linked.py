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
        val_returned = self.first
        self.first = self.first.next1
        return val_returned

    def print_list(self):
        """print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')" """
        list_tuple = ()
        while self.first != None:
            list_tuple += (self.first.value,)
            self.first = self.first.next1
        print list_tuple
        return list_tuple

    def list_size(self):
        """returns the length of the list"""
        count = 0
        while self.first != None:
            self.first = self.first.next1
            count += 1
        return count

    def search(self, value):
        """returns the node containing 'value' in the list, 
        if present, else None"""
        while self.first != None:
            self.first = self.first.next1
            if self.first.value = value
                return self.first.value
        #if it's not there return None.
            

    def remove_node(self, node):
        '''removes the given node from the list, wherever 
        it might be (node must be an item in the list)'''
        #if the first node is the one reset self.first to the next one.
        if self.first == node:
            self.first = self.first.next1
        #traverse list to find node and reset previous.next to following.first
        else:
            following = self.first.next1.next1
            previous = self.first
            while self.first.value != node:
                self.first = node.next1
                following = following.next1
        

    

test_list = Linked_list()
test_list.insert(1)
test_list.insert(2)
test_list.insert(3)
test_list.insert(4)
test_list.print_list( )
test_list.search(3)
#test_list.pop_front()
#test_list.list_size()
#test_list.remove_node( 2 )
#test_list.print_list( )
