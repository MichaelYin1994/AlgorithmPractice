# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 00:21:48 2018

@author: XPS13
"""

'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/17
Mail: zhuoyin94@163.com
Title: 先进先出(FIFO)队列，链表实现
-------------------------------------------------------------------------------
self.__init__(self):
    初始化相关参数，输入参数为None，内部初始化self._head, self._tail等相关参数。

self.__len__(self):
    返回队列的大小。

self.__iter__(self):
    队列的迭代器，返回一个可迭代的对象。

self.is_empty(self):
    检测队列是否为空，为空则返回True，否则返回False。

self.enqueue(self, item):
    为队列添加一个元素。

self.deqeue(self):
    队尾元素出队，队列为空则抛出异常。
-------------------------------------------------------------------------------
'''
###############################################################################
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

###############################################################################
class QueueLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._queueSize = 0
    
    def __len__(self):
        return self._queueSize
    
    def __iter__(self):
        return _QueueIterator(self._head)
    
    def is_empty(self):
        return self._queueSize == 0
    
    def enqueue(self, item):
        # (self._head)1 --> 2 --> 3(self._tail) (4入队)
        # (self._head)1 --> 2 --> 3 --> 4(self._tail)
        newNode = Node(item)
        if self._head == None:
            self._head = newNode
            self._tail = self._head
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._queueSize += 1 
        
    def dequeue(self):
        assert self._queueSize != 0, "Can not dequeue from an empty queue !"
        res = self._head.item
        self._head = self._head.next
        self._queueSize -= 1
        return res
    
###############################################################################
# 构建队列的迭代器
class _QueueIterator(object):
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
# 单元测试
if __name__ == "__main__":
    queue = QueueLinkedList()
    for i in range(10):
        queue.enqueue(i)
    
    iterRes = []
    for i in queue:
        iterRes.append(i)
    
    res = []
    for i in range(queue.__len__()):
        res.append(queue.dequeue())