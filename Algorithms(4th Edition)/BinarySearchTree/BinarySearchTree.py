# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:52:56 2018

@author: XPS13
"""
class TreeNode:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = None
        self._right = None
        
class BinarySearchTree():
    def __init__(self):
        self._root = None
        self._bstSize = 0
    
    # BST的contains特殊方法，判断某个key是否存在于BST中，存在则返回所在位置的node
    # 的地址，否则返回None
    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None
    
    # 获取某个key对应的值，若key不存在，则返回None
    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Invalid key !"
        return node.values
    
    # 二叉搜索树的主要方法，输入一个node的地址与想要查找的key，返回查到的node的地址
    def _bstSearch(self, node, target):
        if node == None:
            return None
        elif node._key > target:
            return self._bstSearch(node._left)
        elif node._key < target:
            return self._bstSearch(node._right)
        else:
            return node
    
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
    
    # Important
    def _bstFloor(self, node, target):
        if node == None:
            return None
    
    def _bstCeiling(self):
        pass
    
    def minimum(self):
        node = self._bstMinimum(self._root)
        return node.val if node is not None else None
    
    def maximum(self):
        node = self._bstMaximum(self._root)
        return node.val if node is not None else None
    
    def insert(self, key, value):
        res = self._bstSearch(self._root, key)
        if res != None:
            res.val = value
            return False
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True
        
if __name__ == "__main__":
    pass
        