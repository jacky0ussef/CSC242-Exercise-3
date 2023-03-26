'''
Jack Youssef
2/20/23

Contains Node class from Student Files.
'''

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next