Some Data Structures in Python
===============

Examples of common data structures implemented in Python.  Each will include two
files, one with the implementation and a second test file to be run with Py Test.

Currently includes:

These scripts naknowledgement to the latter chapters of 
[How to Think Like a Computer Scientist](http://www.openbookproject.net/thinkcs/python/english2e/ch18.html), by Jeffrey Elkner, Allen B. Downey, 
and Chris Meyers.  The relevent code block is extremely similar but uses a list.


###linked.py (test_linked.py)
implements a linked list without using the Python list type.

###stack.py (test_stack.py)
implements a last in, first out stack based on the linked list module.  

###queue.py (test_queue.py)
A queue implementation with help from the above title and [Princeton](http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html).

###parens.py (test_parens.py) 
takes some text and returns 1, 0, -1 depending on 
if the parentheses in the text are closed correctly or not.


