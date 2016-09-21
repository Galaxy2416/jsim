# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:39:39 2016

@author: xsun
"""
from model import model_dict
import sys

class raw_node(object):
    name = ''
    
class raw_param(object):
    name = ''
    value = ''
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):      
        return '$ Parameter : %s(name) = %s(value) ' % (self.name, self.value)
        
class raw_command(object):       
    title = ''

    def __str__(self):      
        return 'Title :  %s' % (self.title)
        
class raw_circuit(object):
    commands = raw_command()
    name = ''
    port_list = [] # string 
    ins_list = [] # device
    xins_list = [] # subckt inst
    param_list = []
    
    def __init__(self, name):
        self.name = name
        
    def add_port(self, name):
        self.port_list.append(name)
        
    def add_port_list(self, port_list):
        self.port_list = self.port_list + port_list
    
    def add_ins(self, instance):
        self.ins_list.append(instance)
        
    def add_xins(self, xins):
        self.xins_list.append(xins)   
        
    def add_param(self, param):
        self.param_list.append(param)
        
    def __str__(self):
        s = ''
        s += self.commands.__str__()
        s += 'Name : %s \n' % self.name
        s += '\nThe Port Number is %d \n' % len(self.port_list)
        for i in self.port_list:
            s += i 
            s += ' , '
        s += '\nThe Instance Number is %d \n' % len(self.ins_list)
        for i in self.ins_list:
            s += i.__str__()
            s += '\n'
        s += '\nThe X - Instance Number is %d\n' % len(self.xins_list)
        for i in self.xins_list:
            s += i.__str__()    
            s += '\n'
        s += '\nThe Parameter Number is %d\n' % len(self.param_list)
        for i in self.param_list:
            s += i.__str__()  
            s += '\n'
        return s
            
class raw_instance (object):
    name = ''
    model = ''
    port_list = []
    value = ''
    def set_up_model(self, model_name):
        if not model_dict.has_key(model_name):
            print(" The model %s is not exsited " % model_name)
            sys.exit()
        self.model = model_name
    
    def add_port(self, name):
        self.port_list.append(name)

    def add_port_list(self, port_list):
        self.port_list = self.port_list + port_list
        
    def add_value(self, value):
        self.value = value
        
    def __str__(self):      
        s = '@ Device :  %s(model) %s(name) = %s(value)\n' % (self.name, self.model, self.value)
        s += 'Ports: '
        for i in self.port_list:
            s += i
            s += ' , '
        return s
        
    def __init__(self, name, model_name, value):
        if not model_dict.has_key(model_name):
            print("The model %s is not exsited " % model_name)
            sys.exit()
        self.name = name
        self.model = model_name
        self.value= value
        

class raw_xinstance (object):
    name = ''
    subckt_name= 0
    
    def set_up_circuit(self, subckt_name):
        # TODO
        self.subckt_name = subckt_name
        
    def __init__(self, name, subckt_name):
        self.name = name
        self.subckt_name = subckt_name
        
        # TODO

top = raw_circuit('top') 
