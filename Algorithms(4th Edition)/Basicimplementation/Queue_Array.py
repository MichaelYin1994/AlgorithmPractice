# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:33:27 2018

@author: XPS13
"""
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/19
Mail: zhuoyin94@163.com
Title: 先进先出(FIFO)队列的数组实现，其中数组大小动态调整。这里使用数组来模拟队列。
使用的则是循环队列进行模拟。
-------------------------------------------------------------------------------
self.__init__(self):
    初始化相关参数，输入参数为None，内部初始化self._head, self._tail等相关参数。

self.__len__(self):
    返回队列的大小。

self.__iter__(self):
    队列的迭代器，返回一个可迭代的对象。

self.is_empty(self):
    检测队列是否为空，为空则返回True，否则返回False。

self.is_full(self):
    检测队列是否为满。

self.enqueue(self, item):
    为队列添加一个元素。若是队列将满，扩大一倍队列数组。

self.deqeue(self):
    队尾元素出队，队列为空则抛出异常。先元素出队，若是出队后队列数组四分之一为空，
    调整队列数组大小为原来二分之一。

self.print_queue_info(self):
    打印队列数组信息。
-------------------------------------------------------------------------------
[1] https://blog.csdn.net/wangsiyu34567/article/details/82822766
[2] https://www.cnblogs.com/chenliyang/p/6554141.html
-------------------------------------------------------------------------------
'''
###############################################################################
class QueueArray():
    def __init__(self, arraySize):
        # 初始化队列，队列为数组定容，队列的大小初始化时固定
        # queueMemorySize代表堆栈数组所占的内存大小(数组长度)，queueSize代表堆栈包含
        # 的元素的个数
        assert arraySize, "Invalid queue size!"
        self._queue = [None] * arraySize
        self._queueArraySize = len(self._queue)
        self._queueSize = 0
        
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item):
        print("\nEnqueue {}".format(item))
        if self.is_full():
            self.resize(self._queueArraySize * 2)
        self._queue[self._tail] = item
        self._tail = (self._tail + 1) % self._queueArraySize
        self._queueSize += 1
        
    def dequeue(self):
        assert self._queueSize, "Dequeue from an empty queue!"
        # 元素出队
        res = self._queue[self._head]
        self._queue[self._head] = None
        print("\nDequeue {}".format(res))
        
        # 更新头指针，并防止self._head索引溢出
        self._head = (self._head + 1) % self._queueArraySize
        self._queueSize -= 1
        
        # 若是队列大小为数组的四分之一，缩小数组大小到原来的二分之一
        if self._queueSize > 0 and self._queueSize == self._queueArraySize // 4:
            self.resize(self._queueArraySize // 2)
        return res
    
    def is_empty(self):
        if self._head == self._tail:
            return True
        else:
            return False
    
    def is_full(self):
        # self._tail所指的元素永远是空元素，若是下一个元素是head，则队满
        if (self._tail + 1) % self._queueArraySize == self._head:
            return True
        else:
            return False
    
    def queue_size(self):
        # 解决self._tail在self._head之前的问题
        queueSize = (self._tail - self._head + self._queueArraySize) % self._queueArraySize
        return queueSize
    
    def resize(self, newSize=None):
        assert newSize, "Invalid queue size!"
        newQueue = [None] * newSize
        
        # 从头指针开始复制队列数组元素
        headTmp = self._head
        i = 0
        while(headTmp != self._tail):
            newQueue[i] = self._queue[headTmp]
            headTmp = (headTmp + 1) % self._queueArraySize
            i += 1
            
        self._tail = self._queueSize
        self._head = 0
        self._queue = newQueue
        self._queueArraySize = len(newQueue)
        
    def print_queue_info(self):
        print("---------------------------------------------------")
        print("Queue memory size: {}.".format(self._queueArraySize))
        print("Queue size: {}.".format(self._queueSize))
        print("Queue: {}".format(self._queue))
        print("Queue head: {}.".format(self._head))
        print("Queue tail: {}.".format(self._tail))
        print("Queue is empty: {}.".format(self.is_empty()))
        print("---------------------------------------------------")
###############################################################################

if __name__ == "__main__":
    queue = QueueArray(1)
    res = []
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
    queue.enqueue(6)
    queue.print_queue_info()
    
    res.append(queue.dequeue())
    queue.print_queue_info()
    
#    # 6
#    queue.enqueue(6)
#    queue.print_queue_info()
#    
#    # 6 --> 7
#    queue.enqueue(7)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 4
#    queue.enqueue(4)
#    queue.print_queue_info()
#    
#    # 7 --> 1 --> 4
#    res.append(queue.dequeue())
#    queue.print_queue_info()
#    
#    # 1 --> 4
#    res.append(queue.dequeue())
#    queue.print_queue_info()
#    
#    # 1 --> 4 --> 12
#    queue.enqueue(12)
#    queue.print_queue_info()
#    
#    # 4 --> 12
#    res.append(queue.dequeue())
#    queue.print_queue_info()
#    
#    # 12
#    res.append(queue.dequeue())
#    queue.print_queue_info()
#    
#    # None
#    res.append(queue.dequeue())
#    queue.print_queue_info()
#    
#    # 6
#    queue.enqueue(6)
#    queue.print_queue_info()
#    
#    # 6 --> 7
#    queue.enqueue(7)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 1 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 1 --> 1 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 1 --> 1 --> 1 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
#    
#    # 6 --> 7 --> 1 --> 1 --> 1 --> 1 --> 1 --> 1
#    queue.enqueue(1)
#    queue.print_queue_info()
