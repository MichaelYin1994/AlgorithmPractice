# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:39:38 2018

@author: XPS13
"""
"""
(1)说明：
双链表的Python实现，参见网址[1]。实现以下的功能：
1. traversal：从前往后与从后往前遍历链表
2. push：在首部增加一个节点
3. append：在尾部增加一个节点
4. insert_after：在指定节点后面插入一个节点
5. remove：移除指定节点
6. reverse_linked_list：链表翻转
7. empty_linked_list: 清空链表

(2)Tips: 
处理的时候主要注意，根据链表是否为空链表，对head与tail进行处理；处理好了head与tail，
则注意处理好链表桥接的时候的prev与next的问题。

[1] https://www.geeksforgeeks.org/doubly-linked-list/
"""
###############################################################################
class DoublyListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def traversal(self):
        if self._head == None:
            print("Linked list is empty !")
            return
        
        print("\nTraversal forward:")
        currNode = self._head
        while(currNode != None):
            print(currNode.val)
            currNode = currNode.next
        
        print("\nTraversal backward:")
        currNode = self._tail
        while(currNode != None):
            print(currNode.val)
            currNode = currNode.prev
        print("Linked List Size is {}".format(self._size))
        return
        
    def push(self, val):
        # 增加一个新的结点到链表的首部
        # Step 1: 新建一个节点
        newNode = DoublyListNode(val)
        
        # Step 2: 改变头结点
        # 1. 头结点为None，为空链表，newNode就是新的头结点与尾结点
        # 2. 头结点不为None，改变头结点
        newNode.next = self._head
        if self._head != None:
            self._head.prev = newNode
        else:
            self._tail = newNode
            
        # Step 3: 更新头结点与链表的大小
        self._head = newNode
        self._size += 1
        return
    
    def append(self, val):
        # 将一个新的元素附加到链表尾部
        # Step 1: 新建立一个节点
        newNode = DoublyListNode(val)
        
        # Step 2: 分两种情况讨论：
        # 1. 头结点为None，为空链表，newNode就是新的头结点与尾结点
        # 2. 头结点不为None，则尾结点一定存在，需要对尾结点进行操作
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            newNode.prev = self._tail
            self._tail = newNode
            
        self._size += 1
        return
            
    def insert_after(self, prevNode, val):
        # 始终注意检查输入条件
        if prevNode == None or val == None:
            print("Error input !")
            return
        
        newNode = DoublyListNode(val)
        # Step 2: 对prevNode分情况讨论：
        # 1. prevNode是尾结点，则需要更新尾结点
        # 2. prevNode是普通股结点，则不需要做其他操作
        if prevNode.next == None:
            prevNode.next = newNode
            newNode.prev = prevNode
            self._tail = newNode
        else:
            newNode.next = prevNode.next
            prevNode.next = newNode
            newNode.prev = prevNode
            # 更新新节点的下一个结点的prev结点的地址
            newNode.next.prev = newNode
        self._size += 1
        return
    
    def remove(self, node):
        if node == None:
            print("Error input !")
            return
        
        # Node是尾结点
        if node.next == None and node.prev != None:
            node.prev.next = None
            self._tail = node.prev
        # Node是头结点
        elif node.next != None and node.prev == None:
            node.next.prev = None
            self._head = node.next
        # LinkedList只有一个节点
        elif node.prev == None and node.next == None:
            self._head = None
            self._tail = None
        # Node节点就是普通节点
        elif node.next != None and node.prev != None:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self._size -= 1
        return
    
    def reverse_linked_list(self):
        pass
    
    def empty_linked_list(self):
        pass

###############################################################################
if __name__ == "__main__":
    dLinkedList = DoublyLinkedList()
    '''
    # 6 --> None
    dLinkedList.push(6)
    
    # None
    dLinkedList.remove(dLinkedList._tail)
    
    dLinkedList.traversal()
    '''
    '''
    # 7 --> 6 --> None
    dLinkedList.push(7)
    
    # 7 --> 6 --> 8 --> None
    dLinkedList.insert_after(dLinkedList._head.next, 8)
    
    dLinkedList.traversal()
    '''
    
    # 6 --> None
    dLinkedList.append(6)
    
    # 7 --> 6 --> None
    dLinkedList.push(7)
    
    # 1 --> 7 --> 6 --> None
    dLinkedList.push(1)
    
    # 1 --> 7 --> 6 --> 4 --> None
    dLinkedList.append(4)
    
    # 1 --> 7 --> 8 --> 6 --> 4 --> None
    dLinkedList.insert_after(dLinkedList._head.next, 8)
    
    # 7 --> 8 --> 6 --> 4 --> None
    dLinkedList.remove(dLinkedList._head)
    
    # 8 --> 6 --> 4 --> None
    dLinkedList.remove(dLinkedList._head)
    
    # 8 --> 6 --> None
    dLinkedList.remove(dLinkedList._head.next.next)
    
    # 8 --> 6 --> 12 --> None
    dLinkedList.append(12)
    
    # 8 --> 12 --> None
    dLinkedList.remove(dLinkedList._head.next)
    
    # Error input
    dLinkedList.remove(dLinkedList._head.next.next)
    
    dLinkedList.traversal()
