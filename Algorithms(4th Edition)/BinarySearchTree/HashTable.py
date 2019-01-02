# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:23:14 2018

@author: XPS13
"""

'''
-------------------------------------------------------------------------------
Author: Michael Yin
Create Date: 2018/12/29
Modified Date: 2018/12/29
Mail: zhuoyin94@163.com
Title: 散列表(Hash Table)的实现。
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

-------------------------------------------------------------------------------
'''
###############################################################################
# 代表Hash Table中的元素。若是Hash Table中的元素没有被访问，则代表为None；若是之前被
# 访问过，后来被删除，则为MapEntry的实例，实例的key和value为None。
class MapEntry():
    def __init__(self, key, value):
        self.key = key
        self.value = value

###############################################################################
class HashTable():
    def __init__(self):
        self._hashTable = [None] * 100
        self._count = 0
        self._maxCount = len(self._hashTable) - len(self._hashTable) // 3
        
        self.UNUSED = None
        self.EMPTY = MapEntry(None, None)
        
    def __len__(self):
        return self._count
    
    def __contains__(self, key):
        slot = self.findSlot(key, False)
        return slot is not None
    
    def add(self, key, value):
        slot = self.find_slot(key, True)
        if slot is None:
            pass
        else:
            pass
        
    
    # Probing function
    def find_slot(self, key, forInsert=True):
        slot = self._hash_1(key)
        step = self._hash_2(key)
    
        hashTableSize = len(self._hashTable)
        while self._hashTable[slot] is not self.UNUSED: # USED
            # 找到一个空的slot，空的slot可以是UNUSED，也可以是EMPTY
            if forInsert and (self._hashTable[slot] is self.UNUSED or self._hashTable[slot] is self.EMPTY):
                return slot
            # 查询Hash键值对，仅仅为了查询，所以slot必定要有key与value的pair
            elif not forInsert and (self._table[slot] is not self.UNUSED and self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step) % hashTableSize
  
    def value_of(self, key):
        slot = self.find_slot(key, False)
        assert slot is not None, "Invalid map key !"
        return self._hashTable[slot]
        
    def remove(self):
        pass
    
    def rehash(self):
        pass
    
    def _hash_1(self, key):
        return abs(hash(key)) % len(self._hashTable)
    
    def _hash_2(self, key):
        return 1 + abs(hash(key)) % (len(self._hashTable) - 2)
