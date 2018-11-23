# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 15:58:57 2018

@author: XPS13
"""
###############################################################################
'''
说明：
使用链表实现堆栈的功能。包括三大功能：
1. push()
2. pop()
3. is_empty()
4. iterator迭代器
'''

# 链表结点的定义
class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

# 使用链表实现堆栈:
# Node_0(Node wait to be added) --> Node_1 --> Node_2 --> Node_3
class Stack:
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
        popNode = self._head
        self._head = popNode.next
        self._stackSize -= 1
        return popNode.item
    
    def is_empty(self):
        if self._head == None:
            print("Stack is empty !")
        else:
            print("Stack is not empty !")

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
    b = Stack()
    for i in testData:
        b.push(i)