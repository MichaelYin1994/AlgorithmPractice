# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:00:58 2018

@author: XPS13
"""

# 使用两个堆栈构成队列，关键点：只能使用列表的pop操作，或者访问列表尾部元素
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._first = []
        self._second = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._first.append(x)

    def pop(self):
        firstSize = len(self._first)
        secondSize = len(self._second)
        
        if firstSize == 0 and secondSize == 0:
            return None
        # 队列的尾部应该是第二个栈的最后一个元素，若第二个栈不是空栈
        # 不应该执行将第一个栈的元素出栈的操作。
        elif secondSize == 0:
            while(self._first):
                self._second.append(self._first.pop())
        ret = self._second.pop()
        return ret
        
    def peek(self):
        firstSize = len(self._first)
        secondSize = len(self._second)
        
        if firstSize == 0 and secondSize == 0:
            return None
        elif secondSize == 0:
            while(self._first):
                self._second.append(self._first.pop())
        return self._second[-1]
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if len(self._second) == 0 and len(self._first) == 0 else False
