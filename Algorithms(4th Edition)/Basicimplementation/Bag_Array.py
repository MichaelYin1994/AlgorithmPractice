# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:48:46 2018

@author: XPS13
"""
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/19
Mail: zhuoyin94@163.com
Title: 背包(Bag)的数组实现。
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
class BagList:
    def __init__(self):
        self._itemList = []
        self._currentItem = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._currentItem < len(self._itemList):
            val = self._itemList[self._currentItem]
            self._currentItem += 1
            return val
        else:
            raise StopIteration
        
    def add(self, item):
        self._itemList.append(item)
    
    def is_empty(self):
        return len(self._itemList) == 0
    
    def size(self):
        return len(self._itemList)
    
    def contains(self, target):
        res = self.__binarySearch(target)
        if res != None:
            return True
        else:
            return False
#    # 自己写的程序，为什么背包会有二分查找？
#    def __binarySearch(self, target):
#        low = 0
#        high = len(self._itemList)-1
#        
#        while(low <= high):
#            mid = low + (high - low) // 2
#            if (self._itemList[mid] <  target):
#                low = mid + 1
#            if (self._itemList[mid] >  target):
#                high = mid - 1
#            if (self._itemList[mid] ==  target):
#                return self._itemList[mid]
#        return None
    
    