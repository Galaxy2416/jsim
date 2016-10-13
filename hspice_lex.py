# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 23:51:41 2016

@author: xsun
"""
import ply.lex as lex
from ply.lex import TOKEN
# import copy  

class HspiceLexer(object):
    # List of token names.   This is always required
    digit            = r'([0-9])'
    nondigit         = r'([_A-Za-z])'
    name             = r'([a-zA-Z_][a-zA-Z0-9_]*)'
    identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)' 
    expr             = r'([a-zA-Z0-9+-\\*/() \t]+)'
       
    tokens = ( 
       'TITLE',
       'NUMBER',
       'NAME',
#       'EXPR',
       'PARAM',
    )
    
    # Regular expression rules for simple tokens

    literals = [ '+','-','*','/', '(' ,')', '{', '}', '=', ',']
    
    states = (
    ('title','exclusive'),
    ('param','exclusive'),
    ('expr','inclusive'),
    )
    
    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_PARAM(self, t):
        r'\.param | \.parameter'
        t.lexer.begin('param')
        return t
        
    def t_TITLE(self, t):
        r'\.title | \.TITLE'
        t.lexer.begin('title')
        return t;
    
    def t_title_NAME(self, t):
        r'([a-zA-Z0-9_]+)'
        return t
    
    @TOKEN(name)
    def t_param_INITIAL_NAME(self, t):
        return t


#    @TOKEN(expr)
#    def t_expr_EXPR(self, t):
#        t.value = str(t.value).replace(' ','') # strip the space
#        return t      

    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t
    
    @TOKEN(name)
    def t_NAME(self, t):
        return t
        
    def t_param_INITIAL_EQUAL(self,t):
        r'='
        t.type = '='      # Set token type to the expected literal
        t.lexer.begin('expr')
        return t

    # Define a rule so we can track line numbers
    def t_ANY_newline(self,t):
        r'\n+'
        t.lexer.begin('INITIAL')
        t.lexer.lineno += len(t.value)
        
    # A string containing ignored characters (spaces and tabs)
    t_ANY_ignore  = ' \t'

    # Error handling rule
    def t_ANY_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    # Test it output
    def print_lex(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: 
                 break
             print(tok)

# Build the lexer and try it out
# Test it