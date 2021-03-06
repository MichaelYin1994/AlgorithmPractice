# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:00:47 2018

@author: XPS13
"""
# 这道题的关键在于，要么保证其中一个队列为空，要么保证队列2为空。
class MyStack(object):

    def __init__(self):
        self._queue_1 = []
        self._queue_2 = []

    def push(self, x):
        self._queue_1.append(x)

    def pop(self):
        if len(self._queue_1) != 0:
            while(len(self._queue_1) != 1):
                self._queue_2.append(self._queue_1.pop(0))
            return self._queue_1.pop(0)
        elif len(self._queue_2) != 0:
            while(len(self._queue_2) != 1):
                self._queue_1.append(self._queue_2.pop(0))
            return self._queue_2.pop(0)
        else:
            return False
        
    def top(self):
        if len(self._queue_1) != 0:
            while(len(self._queue_1) != 1):
                self._queue_2.append(self._queue_1.pop(0))
            return self._queue_1[0]
        elif len(self._queue_2) != 0:
            while(len(self._queue_2) != 1):
                self._queue_1.append(self._queue_2.pop(0))
            # 保证队列2为空
            tmp = self._queue_2.pop(0)
            self._queue_1.append(tmp)
            return tmp
        else:
            return False
        
    def empty(self):
        if len(self._queue_1) == 0 and len(self._queue_2) == 0:
            return True
        else:
            return False