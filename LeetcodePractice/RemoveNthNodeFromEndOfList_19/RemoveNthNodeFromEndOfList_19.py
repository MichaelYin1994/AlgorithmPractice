# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:15:43 2018

@author: XPS13
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None:
            return []
        curr = head
        pioneer = head
        prev = ListNode(None)
        prev.next = curr
        while(pioneer != None and n != 0):
            pioneer = pioneer.next
            n -= 1
            
        while(pioneer != None):
            pioneer = pioneer.next
            curr = curr.next
            prev = prev.next
        
        # 分情况讨论，有可能移除的是头结点，返回下一个结点就好了
        # 其他的情况就是正常操作
        if curr == head:
            return curr.next
        else:
            prev.next = curr.next
            return head