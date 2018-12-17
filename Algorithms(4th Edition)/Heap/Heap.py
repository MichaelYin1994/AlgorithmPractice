# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 23:04:07 2018

@author: XPS13
"""
import random
class MaxHeap():
    def __init__(self, maxSize):
        # Count扮演了堆目前的最大尺寸的角色
        self._elements = maxSize * [None]
        self._count = 0
        self._maxSize = maxSize
    def __len__(self):
        return self._count
    
    def less(self, pos_1, pos_2):
        return self._elements[pos_1] < self._elements[pos_2]
    
    def exchange(self, pos_1, pos_2):
        tmp = self._elements[pos_1]
        self._elements[pos_1] = self._elements[pos_2]
        self._elements[pos_2] = tmp
        
    def capacity(self):
        return len(self._elements)
    
    def sink(self, pos):
        while(2*pos <= self._maxSize):
            left = 2 * pos + 1
            right = 2 * pos + 2
            largest = pos
            # 这里先判断左右孩子是不是存在，再交换值（可能比较的次数会增多）
            if (left < self._count) and (self.less(pos, left)):
                largest = left
            if (right < self._count) and (self.less(largest, right)):
                largest = right
            if largest == pos:
                break
            else:
                self.exchange(pos, largest)
                pos = largest
                
    def swim(self, pos):
        # 设想[5, 12, 3]这种有3个元素的堆来套问题
        while(pos > 0 and self.less((pos-1) // 2, pos)):
            self.exchange((pos-1) // 2, pos)
            pos = (pos-1) // 2
    
    def insert(self, value):
        assert self._count < self.capacity(), "Cannot add an element to a full heap."
        self._elements[self._count] = value
        self.swim(self._count)
        self._count += 1
    
    def extract_max(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        val = self._elements[0]
        self._elements[0] = self._elements[self._count - 1]
        self._elements[self._count - 1] = None
        self._count -= 1
        self.sink(0)
        return val

if __name__ == "__main__":
    testCase = random.sample(range(0, 1000, 1), 80)
    #testCase = [4, 231, 5, 123, 90, 66]
    maxSize = len(testCase)
    heap = MaxHeap(maxSize)
    for i in testCase:
        heap.insert(i)
    elements = heap._elements
    print("\nExtract results:")
    res = []
    for i in range(maxSize):
        res.append(heap.extract_max())
    print(res)
