# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:56:00 2018

@author: XPS13
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 注意curr指针一直指向当前有值结点，自己开始的想法是让curr指向的结点值是待填的None        
class Solution:
    def addTwoNumbers(self, l1, l2):
        carryFlag = 0
        dummyNode = ListNode(None)
        dummyNode = curr = ListNode(None)
        while (l1 != None or l2 != None or carryFlag != 0):
            l1_val = l2_val = 0
            if l1 != None:
                l1_val = l1.val
                l1 = l1.next
            if l2 != None:
                l2_val = l2.val
                l2 = l2.next
            carryFlag, currVal = divmod(l1_val + l2_val + carryFlag, 10)
            # 关键一步，curr指向有值结点
            curr.next = ListNode(currVal)
            curr = curr.next
            
        return dummyNode.next