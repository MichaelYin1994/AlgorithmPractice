# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:22:41 2018

@author: XPS13
"""

###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/17
Mail: zhuoyin94@163.com
Title: 后进先出(LIFO)堆栈：链表实现
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
-------------------------------------------------------------------------------
'''
###############################################################################
# 链表结点的定义
class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

###############################################################################
# Node_0(Node wait to be added) --> Node_1 --> Node_2 --> Node_3
class StackLinkedList:
    def __init__(self):
        self._head = None
        self._stackSize = 0
    
    def __len__(self):
        return self._stackSize
    
    def __iter__(self):
        return _StackIterator(self._head)
    
    def push(self, item):
        self._head = StackNode(item, self._head)
        self._stackSize += 1
        
    def pop(self):
        assert self._stackSize != 0, "Pop an element from a empty stack!"
        popNode = self._head
        self._head = popNode.next
        self._stackSize -= 1
        return popNode.item
    
    def is_empty(self):
        return self._stackSize == 0

###############################################################################
# 构建堆栈的迭代器
class _StackIterator():
    def __init__(self, head):
        self._currNode = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._currNode is None:
            raise StopIteration
        elif self._currNode is not None:
            item = self._currNode.item
            self._currNode = self._currNode.next
            return item
        
###############################################################################
if __name__ == "__main__":
    testData = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66]
    b = StackLinkedList()
    for i in testData:
        b.push(i)
    
    res = []
    for i in b:
        res.append(i)