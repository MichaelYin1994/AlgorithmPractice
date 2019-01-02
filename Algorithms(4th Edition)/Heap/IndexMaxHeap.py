# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:48:07 2018

@author: XPS13
"""

###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Create Date: 2018/12/24
Modified Date: 2019/1/2
Mail: zhuoyin94@163.com
Title: 最大索引堆(Indexed Maximum Heap)的实现。
-------------------------------------------------------------------------------
self.__init__(self, maxSize):
    初始化相关参数，需要提供堆的最大尺寸。而self._count代表目前的优先队列队尾的位置。

self.__len__(self):
    返回堆的大小(self._count)。

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

self.capacity(self):
    返回堆的最大容量。

self.extract_min(self):
    提取堆中的最小元素。

self.contains(self, key):
    是否包含索引为key的元素。是返回True，否则返回False。空堆抛出异常。

self.max_key_index(self):
    返回堆中最大元素的索引(key)。

self.delete(self, key):
    删除堆中索引为key的元素。

self.change(self, key, value):
    修改键值对，并恢复堆序。
-------------------------------------------------------------------------------
'''
###############################################################################
class IndexMaxHeap(object):
    def __init__(self, maxSize):
        self._values = [None] * maxSize
        self._node2key = [None] * maxSize
        self._key2node = [None] * maxSize
        self._count = 0
    
    def capacity(self):
        return len(self._values)
    
    def contains(self, key):
        assert self._count > 0, "Empty heap!"
        return self._values[key] != None
    
    def key_value(self, key):
        assert self._count > 0, "Empty heap!"
        return self._values[key]

    def is_empty(self):
        return self._count == 0
    
    def insert(self, key, value):
        assert self._count < self.capacity(), "Cannot add an element to a full heap."
        self._values[key] = value
        self._node2key[self._count] = key
        self._key2node[key] = self._count
        self.swim(self._count)
        self._count += 1
    
    def decrease_key(self, key, value):
        if self.less(value, self._values[key]):
            self._values[key] = value
        self.swim(self._key2node[key])
    
    def increase_key(self, key, value):
        if self.less(self._values[key], value):
            self._values[key] = value
        self.sink(self._key2node[key])
    
    def max_key_index(self):
        assert self._count > 0, "Empty heap!"
        return self._key2node[self._node2key[0]]
    
    def delete(self, key):
        assert key >= 0 and key < self._count, "Key is out of range !"
        nodePos = self._key2node[key]
        self.exchange(nodePos, self._count-1)
        self._count -= 1
        
        self.swim(nodePos)
        self.sink(nodePos)
        
        self._key2node[key] = None
        self._values[key] = None
        self._node2key[self._count] = None
    
    def extract_max(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        # 堆中最小元素的key与value
        keyMin, valMin = self._node2key[0], self._values[self._node2key[0]]
        
        # 交换堆中最小元素与堆最后一个元素的位置
        self.exchange(0, self._count-1)
        self._count -= 1
        
        # 下沉0号结点
        self.sink(0)
        self._values[keyMin] = None
        self._key2node[keyMin] = None
        self._node2key[self._count] = None
        return valMin, keyMin
    
    def change(self, key, value):
        assert key >= 0 and key < self._count, "Key is out of range !"
        assert self.contains(key), "Key is not in the heap !"
        self._values[key] = value
        nodePos = self._key2node[key]
        # 存在swim不上去与sink不下去这两种情况，分别sink和swim
        self.sink(nodePos)
        self.swim(nodePos)
    
    def swim(self, pos):
        # 设想[5, 12, 3]这种有3个元素的堆来套问题
        # 孩子在2k+1, 2k+2的位置，(pos-1)//2计算父亲结点位置
        while(pos > 0 and self.less((pos-1) // 2, pos)):
            self.exchange((pos-1) // 2, pos)
            pos = (pos-1) // 2
    
    def sink(self, pos):
        while(2*pos < self._count):
            left = 2 * pos + 1
            right = 2 * pos + 2
            maximum = pos
            # 这里先判断左右孩子是不是存在，再交换值（可能比较的次数会增多）
            if (left < self._count) and (self.less(pos, left)):
                maximum = left
            if (right < self._count) and (self.less(maximum, right)):
                maximum = right
            if maximum == pos:
                break
            else:
                self.exchange(pos, maximum)
                pos = maximum
        
    def exchange(self, pos_1, pos_2):
        # 第一步，交换key2node的存储内容
        self._key2node[self._node2key[pos_1]] = pos_2
        self._key2node[self._node2key[pos_2]] = pos_1
        
        # 第二步，交换heap的node的顺序
        tmp = self._node2key[pos_1]
        self._node2key[pos_1] = self._node2key[pos_2]
        self._node2key[pos_2] = tmp
    
    def less(self, pos_1, pos_2):
        return self._values[self._node2key[pos_1]] < self._values[self._node2key[pos_2]]
###############################################################################
if __name__ == "__main__":
    values = [3.12, 0.32, 2.20, 6.12,
              1.02, 0.03, 0.67, 3.33,
              0.89, 1.12, 0.55, 5.46,
              0.63, 0.67, 0.67, 4.35,
              3.12, 0.03, 0.03, 0.03]
    
    maxSize = 100
    heap = IndexMaxHeap(maxSize)
    for ind, item in enumerate(values):
        heap.insert(ind, item)
    res = {"Values": heap._values,
           "Node2Key":heap._node2key,
           "Key2Node":heap._key2node}
    
#    insertSeq = []
#    for i in heap._node2key:
#        insertSeq.append(heap._values[i])
#    heap.delete(11)
#    heap.change(10, 200)
    minVal = []
    for i in range(len(values)):
        minVal.append(heap.extract_max())