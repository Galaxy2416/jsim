# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:50:31 2016

@author: xsun
"""

import sys

class model(object):
    _name = ''
    def __init__(self, name):
        self._name = name
    def setup_nodes(self):
        pass


model_dict = {}

class model_r(model):
    a = 0
    b = 0
    def setup_nodes(self, nodelist):
        if len(nodelist) != 2:
            print(" the r node number should be 2")
            sys.exit()

        
r = model('r')
model_dict[r._name] = r

class model_c(model):
    a = 0
    b = 0
    def setup_nodes(self, nodelist):
        if len(nodelist) != 2:
            print(" the r node number should be 2")
            sys.exit()
        
c = model('c')
model_dict[c._name] = c
