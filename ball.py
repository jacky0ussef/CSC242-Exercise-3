'''
Jack Youssef
02/20/2023

Contains the Ball class, which represents a ball with a color and shape.
'''

class Ball(object):
    """ A ball that maintains a color and shape. """

    # Constructor
    def __init__(self, color, shape):
        """ Sets the initial state of Ball, which includes the color and shape."""
        self._color = color
        self._shape = shape
        
    def __str__(self):
        """ String representation of a Ball, formatted: 'color: color, shape: shape' """
        return f'color: {self._color}, shape: {self._shape}'
    
    