# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:45:36 2019

@author: XPS13
"""

import sys
import os

def split_file_name(name):
    name = name.split("_")
    try:
        name = [name[0]] + name[1].split(".")
        if name[1].isdigit():
            return name[1] + "_" + name[0] + ".py"
        else:
            return name[0] + "_" + name[1] + ".py"
    except:
        return name[0]

os.chdir('.//LeetcodePractice//')
fileName = os.listdir(os.getcwd())

for foldName in fileName:
    os.chdir(".//" + foldName + "//")
    pyFileName = os.listdir(os.getcwd())[0]
    newName = split_file_name(pyFileName)
    os.rename(pyFileName, newName)
    os.chdir("..//")