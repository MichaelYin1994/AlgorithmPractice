# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:52:56 2018

@author: XPS13
"""

###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/24
Mail: zhuoyin94@163.com
Title: 二叉搜索树(Binary Search Tree)的实现。
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
'''
###############################################################################
class TreeNode:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = None
        self._right = None
        self._size = None
        
###############################################################################
class BinarySearchTree():
    def __init__(self):
        self._root = None
        self._bstSize = 0
    
    # BST的contains特殊方法，判断某个key是否存在于BST中，存在则返回所在位置的node
    # 的地址，否则返回None
    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None
    
    # 获取某个key对应的值，若key不存在，则返回None
    def value_of(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Invalid key !"
        return node.values
    
    def _bstMinimum(self, node):
        if node == None:
            return None
        elif node.left == None:
            return node
        else:
            return self._bstMinimum(node.left)
    
    def _bstMaximum(self, node):
        if node == None:
            return None
        elif node.right == None:
            return node
        else:
            return self._bstMaximum(node.right)
    
    # Important
    def floor(self, node, target):
        if node == None:
            return None
    
    def ceil(self):
        pass
    
    def minimum(self):
        node = self._bstMinimum(self._root)
        return node.val if node is not None else None
    
    def maximum(self):
        node = self._bstMaximum(self._root)
        return node.val if node is not None else None
    
    def insert(self, key, value):
        # 搜索书中存不存在键为key的结点
        res = self._bstSearch(self._root, key)
        # 若存在，则更新key对应的值，否则插入一个结点
        if res != None:
            res.val = value
            return False
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True
        
    # 二叉搜索树的递归搜索方法，输入一个node的地址与想要查找的key，返回查到的node的地址
    def _bstSearch(self, node, target):
        if node == None:
            return None
        elif node._key > target:
            return self._bstSearch(node._left)
        elif node._key < target:
            return self._bstSearch(node._right)
        else:
            return node
    
    # 插入方法输入的是结点的地址，并且接受将要插入结点的key和value，插入过程采用
    # 递归的方式，当结点为None时候，已经到达底部，便新建一个结点。否则递归的寻找
    # 应该插入的地方。
    def _bstInsert(self, node, key, value):
        if node == None:
            node = TreeNode(key, value)
        elif key < node.val:
            node.left = self._bstInsert(node.left, key, value)
        elif key > node.val:
            node.right = self._bstInsert(node.right, key, value)
        return node
###############################################################################
if __name__ == "__main__":
    values = [3.12, 0.32, 2.20,
              1.02, 0.03, 0.67,
              0.89, 1.12, 0.55,
              0.63, 0.67, 0.67,
              3.12, 0.03, 0.03, 0.03]
    bst = BinarySearchTree()
    
    for ind, item in enumerate(values):
        bst.insert(item, ind)