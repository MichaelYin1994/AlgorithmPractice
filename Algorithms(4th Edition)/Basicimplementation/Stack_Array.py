# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:22:20 2018

@author: XPS13
"""
###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/17
Mail: zhuoyin94@163.com
Title: 后进先出(LIFO)堆栈的数组实现，实现了动态堆栈数组大小调整。
-------------------------------------------------------------------------------
self.__init__(self):
    初始化相关参数，需要输入参数为None，内部初始化self._head, self._stackSize等
    相关参数。

self.__len__(self):
    返回堆栈的大小(self._stackSize)。

self.__iter__(self):
    堆栈的迭代器，返回一个可迭代的对象。

self.is_empty(self):
    检测堆栈是否为空，为空则返回True，否则返回False。

self.push(self, item):
    为队列添加一个元素。

self.pop(self):
    栈顶元素出栈，栈为空则抛出异常。

self.resize(self, newSize=None):
    重新调整stack数组的大小，避免对象游离(Java)。
-------------------------------------------------------------------------------
'''
###############################################################################
class StackArray():
    def __init__(self, arraySize):
        # 初始化栈，栈为数组定容栈，栈的大小初始化时固定
        # stackMemorySize代表堆栈数组所占的内存大小(数组长度)，stackSize代表堆栈包含
        # 的元素的个数，arraySize赋值0会索引越界!!!
        assert arraySize, "Invalid stack size!"
        self._stack = [None] * arraySize
        self._stackMemorySize = len(self._stack)
        self._stackSize = 0
        
    def __len__(self):
        return self._stackSize
    
    def __iter__(self):
        pass
    
    def pop(self):
        assert self._stackSize, "Pop an element from a empty stack!"
        res = self._stack[self._stackSize - 1]
        print("\nPop {}".format(res))
        self._stack[self._stackSize - 1] = None
        self._stackSize -= 1
        
        # Dangerous!!!
        if self._stackSize == self._stackMemorySize // 4:
            self.resize(self._stackMemorySize // 2)
        return res
        
    def push(self, item):
        # 堆栈数组内存不够，加倍堆栈数组
        if self._stackSize == self._stackMemorySize:
            self.resize(self._stackSize * 2)
        print("\nPush {}".format(item))
        self._stack[self._stackSize] = item
        self._stackSize += 1
    
    def is_empty(self):
        return self._stackSize == 0
    
    def resize(self, newSize=None):
        assert newSize, "Invalid stack size!"
        newStack = [None] * newSize
        i = 0
        while(i != self._stackSize):
            newStack[i] = self._stack[i]
            i += 1
        self._stack = newStack
        self._stackMemorySize = len(newStack)
        
    def print_stack_info(self):
        print("---------------------------------------------------")
        print("Stack memory size: {}.".format(self._stackMemorySize))
        print("Stack size: {}.".format(self._stackSize))
        print("Stack: {}".format(self._stack))
        print("---------------------------------------------------")
        
###############################################################################
if __name__ == "__main__":
    stack = StackArray(8)
    res = []
    # 6
    stack.push(6)
    stack.print_stack_info()
    
    # 7 --> 6
    stack.push(7)
    stack.print_stack_info()
    
    # 1 --> 7 --> 6
    stack.push(1)
    stack.print_stack_info()
    
    # 4 --> 1 --> 7 --> 6
    stack.push(4)
    stack.print_stack_info()
    
    # 1 --> 7 --> 6
    res.append(stack.pop())
    stack.print_stack_info()
    
    # 7 --> 6
    res.append(stack.pop())
    stack.print_stack_info()
    
    # 12 --> 6 --> 4
    stack.push(12)
    stack.print_stack_info()
    
    # 6 --> 4
    res.append(stack.pop())
    stack.print_stack_info()
    
    # 4
    res.append(stack.pop())
    stack.print_stack_info()
    
    # None
    res.append(stack.pop())
    stack.print_stack_info()
    
    # 6
    stack.push(6)
    stack.print_stack_info()
    
    # 7 --> 6
    stack.push(7)
    stack.print_stack_info()
    
    # 1 --> 7 --> 6
    stack.push(1)
    stack.print_stack_info()