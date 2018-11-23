# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:18:32 2018

@author: XPS13
"""
def calc_maxium_length(s):
    stringDict = {}
    maxLength = 0
    start = 0
    
    for ind, c in enumerate(s):
        if c in stringDict:
            maxLength = max(maxLength, ind-start)
            start = max(stringDict[c]+1, start)
        stringDict[c] = ind
    return max(maxLength, len(s)-start)
