'''
Jack Youssef
2/20/23

Contains LinkedBag class from Student Files.

Modified to become subclass of AbstractBag.
'''

from node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """A link-based bag implementation that is a subclass of AbstractBag."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

