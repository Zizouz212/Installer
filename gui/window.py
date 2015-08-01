#! /usr/bin/python

# window.py

__doc__ = """
This module holds a single class that will be the main toplevel window for the application.
"""

from Tkinter import *
from ttk import *
import Tkinter
import ttk

class Window(Tkinter.Tk):
    def __init__(self):
        super().__init__()
        self._children = []
        
        
    def add_child(self, child) -> int:
        """Makes the child known to the window. Returns the index of the child. 
        The index can be known as the id."""
        
        length = len(self._children)
        
        # We will be returning the length because indexing starts at 0
        
        self._children.append(child)
        return length
        
    
    def get_child(self, index) -> object:
        """Returns the child at the specific index return by the add_child index."""
        
        return self._children[index]
        
if __name__ is '__main__':
    window = Window()
    window.mainloop()
    window.destroy()
