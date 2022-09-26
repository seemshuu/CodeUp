# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:42:19 2021

@author: Seamus
"""

def filterString(string):
    count = 0
    ans = []
    # linear scan working
    for i in range(0, len(string)):
        if string[i] == "0":
            ans.append(string[i])
            count += 1
        elif string[i] == "1":
            ans.append(string[i])
            count += 1
        elif string[i] == "2":
            ans.append(string[i])
            count += 1
        elif string[i] == "3":
            ans.append(string[i])
            count += 1
        elif string[i] == "4":
            ans.append(string[i])
            count += 1
        elif string[i] == "5":
            ans.append(string[i])
            count += 1
        elif string[i] == "6":
            ans.append(string[i])
            count += 1
        elif string[i] == "7":
            ans.append(string[i])
            count += 1
        elif string[i] == "8":
            ans.append(string[i])
            count += 1
        elif string[i] == "9":
            ans.append(string[i])
            count += 1
    if count == 0:
        return 0
    else:
        return int(''.join(ans))
        