#! /usr/bin/python

# __init__.py

# import stuff, create variables from files, store all the data here. Get platform details - Platform checks in next release?

__doc__ = """
Ease of use to provide all resources and data necessary for operation.
"""

import sys
import platform
import os

base_path = os.path.dirname(os.path.abspath(__file__))

license, eula, welcome_text = read_file_data()
    
def read_file_data():
    with open(os.path.join(base_path, 'license.txt') as f:
        license = f.read()
    with open(os.path.join(base_path, 'eula.txt') as f:
        eula = f.read()
    with open(os.path.join(base_path, 'welcome_text.txt') as f:
        welcome_text = f.read()
        
    return license, eula, welcome_text
    
