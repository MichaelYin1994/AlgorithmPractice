# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:09:29 2018

@author: XPS13
"""
###############################################################################
'''
说明：
包含两种背包的实现：一种是背包的链表实现，一种是背包的List实现。
'''

# 背包的List的实现
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
        if len(self._itemList) == 0:
            print("The bag is empty !")
        else:
            print("The bag is not empty.")
    
    def size(self):
        print("Bag contains {} elements.".format(len(self._itemList)))
    
    # 自己写的程序，为什么背包会有二分查找？
    def __binarySearch(self, target):
        low = 0
        high = len(self._itemList)-1
        
        while(low <= high):
            mid = low + (high - low) // 2
            if (self._itemList[mid] <  target):
                low = mid + 1
            if (self._itemList[mid] >  target):
                high = mid - 1
            if (self._itemList[mid] ==  target):
                return self._itemList[mid]
        return None
    
    def contains(self, target):
        res = self.__binarySearch(target)
        if res != None:
            print("Element in bag !")
        else:
            print("Not in bag !")

###############################################################################
# 背包的LinkedList的实现
class BagLinkedList:
    def __init__(self):
        self._head = None
        self._bagSize = 0
        self._currItem = 0
    
    def __len__(self):
        return self._bagSize
    
    def __contains__(self, target):
        currNode = self._head
        while (currNode != None) and (currNode.item != target):
            currNode = currNode.next
        if currNode is not None:
            print("In bag.")
        else:
            print("Not in bag.")
    
    def __iter__(self):
        return _BagIterator(self._head)
    
    def add(self, item):
        newNode = _BagLinkedNode(item)
        #将头结点赋值给新节点所指向的下一个节点，类似于堆栈添加元素的方式
        newNode.next = self._head 
        # 新节点的地址赋值给头节点
        self._head = newNode
        self._bagSize += 1
    
    def remove(self, item):
        predNode = None
        currNode = self._head
        
        while (currNode != None) and (currNode.item != item):
            predNode = currNode
            currNode = currNode.next
        assert currNode is not None, "The item is not in bag !"
        
        if predNode == None:
            self._head = currNode.next
        else:
            predNode.next = currNode.next
        self._bagSize -= 1
        
class _BagLinkedNode():
    def __init__(self, item):
        self.item = item
        self.next = None

class _BagIterator():
    def __init__(self, linkedListHead):
        self._currNode = linkedListHead
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._currNode is None:
            raise StopIteration
        else:
            print(self._currNode.item)
            item = self._currNode.item
            self._currNode = self._currNode.next
            return item
###############################################################################
if __name__ == "__main__":
    testData = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66]
    b = BagLinkedList()
    for i in testData:
        b.add(i)