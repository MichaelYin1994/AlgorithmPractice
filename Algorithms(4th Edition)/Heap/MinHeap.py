# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:47:28 2018

@author: XPS13
"""

###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/23
Mail: zhuoyin94@163.com
Title: 最小堆(Minimum Heap)的实现。
-------------------------------------------------------------------------------
self.__init__(self, maxSize):
    初始化相关参数，需要提供堆的最大尺寸。而self._count代表目前的优先队列队尾的位置。

self.__len__(self):
    返回堆的大小(self._count)。

self.__iter__(self):
    堆的迭代器，返回一个可迭代的对象。层序遍历堆元素。

self.is_empty(self):
    检测堆是否为空，为空则返回True，否则返回False。

self.insert(self, item):
    为堆插入一个元素。

self.exchange(self, pos_1, pos_2):
    交换堆中的两个元素的位置。
    
self.less(self, pos_1, pos_2):
    比较堆中两个元素的大小。

self.sink(self, pos):
    对堆中pos位置的元素进行下沉。
    
self.swim(self, pos):
    对堆中pos位置的元素进行上浮。

def capacity(self):
    返回堆的最大容量。

def extract_min(self):
    提取堆中的最大元素。
-------------------------------------------------------------------------------
'''
import random
###############################################################################
class MinHeap():
    def __init__(self, maxSize):
        # Count扮演了堆目前的最大尺寸的角色
        self._elements = maxSize * [None]
        self._count = 0
        self._maxSize = maxSize
        
    def __len__(self):
        return self._count
    
    def less(self, pos_1, pos_2):
        return self._elements[pos_1] < self._elements[pos_2]
    
    def is_empty(self):
        return self._count == 0
    
    def exchange(self, pos_1, pos_2):
        tmp = self._elements[pos_1]
        self._elements[pos_1] = self._elements[pos_2]
        self._elements[pos_2] = tmp
        
    def capacity(self):
        return len(self._elements)
    
    def sink(self, pos):
        while(2*pos < self._count):
            left = 2 * pos + 1
            right = 2 * pos + 2
            minimum = pos
            # 这里先判断左右孩子是不是存在，再交换值（可能比较的次数会增多）
            if (left < self._count) and (self.less(left, pos)):
                minimum = left
            if (right < self._count) and (self.less(right, minimum)):
                minimum = right
            if minimum == pos:
                break
            else:
                self.exchange(pos, minimum)
                pos = minimum
                
    def swim(self, pos):
        # 设想[5, 12, 3]这种有3个元素的堆来套问题
        # 孩子在2k+1, 2k+2的位置，(pos-1)//2计算父亲结点位置
        while(pos > 0 and self.less(pos, (pos-1) // 2)):
            self.exchange((pos-1) // 2, pos)
            pos = (pos-1) // 2
    
    def insert(self, value):
        assert self._count < self.capacity(), "Cannot add an element to a full heap."
        self._elements[self._count] = value
        self.swim(self._count)
        self._count += 1
    
    def extract_min(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        val = self._elements[0]
        self._elements[0] = self._elements[self._count - 1]
        self._elements[self._count - 1] = None
        self._count -= 1
        self.sink(0)
        return val
###############################################################################
if __name__ == "__main__":
    testCase = random.sample(range(0, 100, 1), 80)
    testCase = [4, 231, 5, 123, 90, 66, -1]
    #testCase.extend([4, 231, 5, 123, 90, 66, -1])
    
    maxSize = 100
    heap = MinHeap(maxSize)
    for i in testCase:
        heap.insert(i)
    elements = heap._elements.copy()
    print("Extract results:")
    res = []
    for i in range(len(testCase)):
        res.append(heap.extract_min())
    print(res)