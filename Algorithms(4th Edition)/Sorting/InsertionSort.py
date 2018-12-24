# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:31:42 2018

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
class InsertionSort(Sort):
    def __init__(self, array):
        super(InsertionSort, self).__init__(array)
    
    def sort(self):
        start = time.clock()
        for i in range(1, self._arraySize):
            for j in range(i, 0, -1):
                if self.less(j, j-1):
                    self.exchange(j-1, j)
        end = time.clock()
        print("=======================================================")
        print("Sorting results : ^^^", self.check())
        print("Running time is {}.".format(end-start))
        print("Total array access is {}.".format(self._arrayAccess))
        print("Total compares is {}.".format(self._compares))
        print("=======================================================")
        return self._array

