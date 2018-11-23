# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 01:21:38 2018

@author: XPS13
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 需要非常注意Python的内存机制！非常容易出现内存混乱的错误。
class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        
        curNode = head.next
        formerNode = head
        formerNode.next = None
        
        while(curNode):
            tmp = curNode.next
            curNode.next = formerNode
            formerNode = curNode
            curNode = tmp
        return formerNode

if __name__ == "__main__":
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3) 
    p3 = ListNode(4)
    head.next = p1 
    p1.next = p2
    p2.next = p3
    s = Solution()
    node = s.reverseList(head)