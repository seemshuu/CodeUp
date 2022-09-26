# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:54:37 2021

@author: Seamus
"""

def isLeapYear(n):
    #century years
    if n % 100 == 0 and n % 400 == 0:
        return True
    elif n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False