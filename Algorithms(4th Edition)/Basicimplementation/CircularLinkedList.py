# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:29:28 2018

@author: XPS13
"""

"""
说明：
循环链表的Python实现，参见网址[1]。实现以下的功能：
1. traversal：从前往后与从后往前遍历链表
2. push：往头结点添加元素

处理的时候主要注意，根据链表是否为空链表，对head与tail进行处理；处理好了head与tail，
则注意处理好链表桥接的时候的prev与next的问题。
[1] https://www.geeksforgeeks.org/circular-linked-list-set-2-traversal/
"""

###############################################################################
class DoublyListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class CircularDoublyLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def push(self, val):
        if val == None:
            print("Invalid value !")
            return
        
        # LinkedList is empty.
        # LinkedList is not empty.
        newNode = DoublyListNode(val)
        if self._head == None:
            newNode.prev = newNode
            newNode.next = newNode
            self._tail = newNode
        else:
            newNode.next = self._head
            self._head.prev = newNode
            newNode.prev = self._tail
            self._tail.next = newNode
            
        self._head = newNode
        self._size += 1
        
    def remove(self, node):
        if node == None:
            print("Error input !")
            return
        
        if node == self._head:
            node.prev.next = node.next
            node.next.prev = node.prev
            self._head = node.next
        elif node == self._tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            self._tail = node.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            
        self._size -= 1
        return
    
    def traversal(self):
        if self._size == 0:
            print("Empty linked list !")
            return
        
        print("Forward traversal:")
        currNode = self._head
        while(True):
            print(currNode.val)
            currNode = currNode.next
            if currNode == self._head:
                break
            
        print("\nBackward traversal:")
        currNode = self._tail
        while(True):
            print(currNode.val)
            currNode = currNode.prev
            if currNode == self._tail:
                break
    
if __name__ == "__main__":
    cList = CircularDoublyLinkedList()
    
    # 12 --> None --> 12
    cList.push(12)
    
    # 56 --> 12 --> None --> 56
    cList.push(56)
    
    # 2 --> 56 --> 12 --> None --> 56 --> 2
    cList.push(2)
    
    # 11 --> 2 --> 56 --> 12 --> None --> 56 --> 2 --> 11
    cList.push(11)
    
    # 2 --> 56 --> 12 --> None --> 56 --> 2
    cList.remove(cList._head)
    
    cList.traversal()