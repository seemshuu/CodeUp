# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:34:43 2021

@author: Seamus
"""

### fibonaci

def fibonacci(n):
    count = 0
    n1, n2 = 0, 1
    while count < n:
        nth = n1 + n2
        n1, n2 = n2, nth
        count += 1
        if count == n:
            print(n1)
    