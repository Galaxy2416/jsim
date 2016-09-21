# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:48:43 2016

@author: xsun
"""

from hspice_yacc import HspiceParser
from raw import top


s =  '''
        .title HandsomeJack 
        .param p = 10
        .param p1 = p
        
         r r1(vcc, gnd) = p
         c c1(vcc, gnd) = p1/100
        '''


def main():
    hparser = HspiceParser()
    hparser.build()
    hparser.parse_to_raw(s)
    print (top)

 # raw_input('calc > ')
# hlex.print_lex(s)


if __name__ == "__main__":
    main()