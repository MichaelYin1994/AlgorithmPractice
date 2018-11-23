# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 00:21:48 2018

@author: XPS13
"""

class QueueNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Queue(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._queueSize = 0
    
    def __len__(self):
        return self._queueSize
    
    def is_empty(self):
        return self._queueSize == 0
    
    def enqueue(self, item):
        if self._head == None:
            self._tail = QueueNode(item, None)
        self._head = QueueNode(item, self._head)
        self._queueSize += 1
        
    def dequeue(self, item):
        dequeueItem = self._tail.item
    