# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 00:21:48 2018

@author: XPS13
"""
###############################################################################
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
###############################################################################
class Queue(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._queueSize = 0
    
    def __len__(self):
        return self._queueSize
    
    def __iter__(self):
        return _QueueIterator(self._head)
    
    def is_empty(self):
        return self._head == None
    
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
        assert self._head, "Can not dequeue from an empty queue !"
        res = self._head.item
        self._head = self._head.next
        self._queueSize -= 1
        return res

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
if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    
    for i in queue:
        print(i)
