#! usr/bin/python

# frames.py

import os
import sys
from abc import abstractmethod
import abc
from Tkinter import *
from ttk import *
import Tkinter
import ttk

def override(func):
    def inner():
        return func
    return inner()


class AbstractFrame(object):
    __metaclass__ = abc.ABCMeta
    
    @abstractmethod
    def create(self, *args):
        Resources.create(self)
        return
    
    @abstractmethod
    def validate(self, *args):
        Resources.validate(self)
        return
    
    @abstractmethod
    def on_invoke(self, source, *args):
        Resources.on_invoke(self, source)
        return
    

class StatusFrame(ttk.Frame, AbstractFrame):
    def __init__(self, parent, *args, **kw):
        self.parent = parent
        self.kw = kw
        self.kw['_args'] = kw
        
    
    @override
    def create(self, *args):
        self.button = ttk.Button(self, text = 'Next >>', command = self.on_invoke)
        self.button.pack(side = 'right')
        
        self.progress = ttk.Progressbar(self, orient = 'Horizontal',
                                        length = 200, mode = 'determinate')
        self.progress.pack(side = 'left')
        self.progress['value'] = int(1/7)
        self.progress['maximum'] = 100
        
        self.current_frame = 1
        
        return
    
    @override
    def validate(self, *args):
        self.progress['value'] = int(self.current_frame / 7)
        if self.current_frame = 4:
            self.button['text'] = 'Install >>'
        else:
            self.button['text'] = 'Next >>'
        
        return
    
    @override
    def on_invoke(self, source, *args):
        self.parent.get_current_child().on_invoke(source, args)
        self.parent.event_notify_all(source)
        self.parent.load_next_frame()
    
class WelcomeFrame(ttk.Frame, AbstractFrame):
    def __init__(self, parent, *args, **kw):
        super().__init__(self, parent, args, kw)
        self.parent = parent
        self.kw = kw
        self.kw['_args'] = args
        
        
    @override
    def create(self, *args):
        self.message = Tkinter.Text(self)
        self.message['bd'] = 0
        self.message['exportselection'] = 0
        self.message['wrap'] = Tkinter.WORD
        self.message.insert(
            Resources.get_welcome_message())
        
        return
        
    
    
    @override
    def validate(self, *args):
        pass
    
    @override
    def on_invoke(self, source, *args):
        if source is 'next_button':
            pass
        return
    

class OverviewFrame(ttk.Frame, AbstractFrame):
    def __init__(self, parent, *args, **kw):
        super().__init__(self, parent, args, kw)
        
        
        
        
    @override
    def create(self, *args):
        pass
    
    @override
    def validate(self, *args):
        pass
    
    @override
    def on_invoke(self, source, *args):
        pass
    

    
