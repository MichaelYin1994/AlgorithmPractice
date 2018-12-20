# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:09:29 2018

@author: XPS13
"""
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/19
Mail: zhuoyin94@163.com
Title: 背包(Bag)的链表实现。
-------------------------------------------------------------------------------
self.__init__(self):
    初始化相关参数，输入参数为None，内部初始化self._head, self._tail等相关参数。

self.__len__(self):
    返回背包的大小。

self.__iter__(self):
    背包的迭代器，返回一个可迭代的对象。

self.__contains__(self, target):
    测试元素是否位于背包中，是返回True，否则返回False。
    
self.add(self, item):
    为背包添加一个元素。

self.remove(self, item):
    移除背包中的某个元素，若不在背包中则抛出异常。

self.is_empty(self):
    检测背包是否为空。
-------------------------------------------------------------------------------
'''
###############################################################################
class _BagLinkedNode():
    def __init__(self, item):
        self.item = item
        self.next = None
        
###############################################################################
class BagLinkedList:
    def __init__(self):
        self._head = None
        self._bagSize = 0
        self._currItem = 0
    
    def __len__(self):
        return self._bagSize
    
    def __contains__(self, target):
        currNode = self._head
        while (currNode != None) and (currNode.item != target):
            currNode = currNode.next
        if currNode is not None:
            return True
        else:
            return False
    
    def __iter__(self):
        return _BagIterator(self._head)
    
    def add(self, item):
        newNode = _BagLinkedNode(item)
        #将头结点赋值给新节点所指向的下一个节点，类似于堆栈添加元素的方式
        newNode.next = self._head 
        # 新节点的地址赋值给头节点
        self._head = newNode
        self._bagSize += 1
    
    def remove(self, item):
        predNode = None
        currNode = self._head
        
        while (currNode != None) and (currNode.item != item):
            predNode = currNode
            currNode = currNode.next
        assert currNode is not None, "The item is not in bag!"
        
        if predNode == None:
            self._head = currNode.next
        else:
            predNode.next = currNode.next
        self._bagSize -= 1
    
    def is_empty(self):
        return self._bagSize == 0

class _BagIterator():
    def __init__(self, linkedListHead):
        self._currNode = linkedListHead
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._currNode is None:
            raise StopIteration
        else:
            print(self._currNode.item)
            item = self._currNode.item
            self._currNode = self._currNode.next
            return item
###############################################################################
if __name__ == "__main__":
    testData = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66]
    b = BagLinkedList()
    for i in testData:
        b.add(i)