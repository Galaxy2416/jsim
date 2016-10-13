# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:58:31 2016

@author: xsun
"""

# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from hspice_lex import HspiceLexer
tokens = HspiceLexer.tokens

from raw import *

cir_now = top


def p_statments(p):
    ''' statments :  command_stm statments 
            | device_stm statments
            | param_stm statments
            | empty
    '''

def p_command(p):
    'command_stm : title_stm'

def p_title(p):
    'title_stm : TITLE NAME'
    top.commands.title = p[2]

def p_device_expr(p):
    '''device_stm : NAME NAME '(' NODELIST ')' '=' expr'''
    device = raw_instance(p[2], p[1], p[7])
    device.add_port_list(p[4])
    cir_now.add_ins(device)

def p_nodelist_list(p):
    '''
    NODELIST : NODELIST ',' NAME
    '''
    p[1].append(p[3])
    p[0] = p[1]

def p_nodelist_name(p):
    '''
    NODELIST : NAME
    '''
    p[0] = [p[1]]

    
def p_param_stm(p):
    '''
    param_stm : PARAM NAME '=' expr
    '''    
    param = raw_param(p[2])
    param.value = p[4][0]
    param.parse_tree = p[4][1]
    cir_now.add_param(param)
    
def p_expr(p):
     '''
     expr : expr '+' term
     | expr '-' term
     | term
     '''
     if (len(p) == 4):
        if p[2] == '+':
            p[0] = (p[1][0] + p[3][0], ('+',p[1][1],p[3][1]))
        elif p[2] == '-':
            p[0] = (p[1][0] - p[3][0], ('-',p[1][1],p[3][1]))
     elif (len(p) == 2):
        p[0] = p[1]
        
def p_term(p):
    '''
    term : term '*' factor
    | term '/' factor
    | factor
    '''
    if (len(p) == 4):
        if p[2] == '*':
            p[0] = (p[1][0] * p[3][0], ('*',p[1][1],p[3][1]))
        elif p[2] == '/':
            p[0] = (p[1][0] / p[3][0], ('/',p[1][1],p[3][1]))
    elif (len(p) == 2):
        p[0] = p[1]    

def p_factor_num(p):
    '''
    factor : '-'  NUMBER
    | NUMBER
    '''   
    if (len(p) == 3):
        p[0] = (-p[2],(('NUM',-p[2])))    
    elif (len(p) == 2):
        p[0] = (p[1],(('NUM',p[1])))   
        
def p_factor_name(p):
    '''
    factor : '-'  NAME
    | NAME
    '''   
    if (len(p) == 3):
        par = cir_now.param_dir[p[2]] # TODO : if not find?
        p[0] = (-par.value,('NUM','-'+ par.name)) 
    elif (len(p) == 2):
        par = cir_now.param_dir[p[1]] # TODO : if not find?
        p[0] = (par.value,('NUM',par.name)) 
       
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")



class HspiceParser(object):
    # Build the parser
    lexer = HspiceLexer()
    def build(self):
        self.set_lexer()
        self.parser = yacc.yacc()
    def set_lexer(self):
        self.lexer.build()           # Build the lexer
    def parse_to_raw(self, s):
        self.parser.parse(s,lexer=self.lexer.lexer)
         