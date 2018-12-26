# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:52:56 2018

@author: XPS13
"""
import gc
###############################################################################
'''
-------------------------------------------------------------------------------
Author: Michael Yin
Modified Date: 2018/12/25
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
    def __init__(self, key, value, size=1):
        self._key = key
        self._value = value
        self._left = None
        self._right = None
        self._size = size
        
###############################################################################
class BinarySearchTree():
    def __init__(self):
        self._root = None
        self._bstSize = 0
    
    # BST的contains特殊方法，判断某个key是否存在于BST中，存在则返回所在位置的node
    # 的地址，否则返回None
    def __contains__(self, key):
        return self._search_key(self._root, key) is not None
    
    # 小于等于target的最大键
    def floor(self, target):
        node = self._floor(self._root, target)
        return node._key if node is not None else None
    
    def _floor(self, node, target):
        if node == None:
            return None
        if node._key == target:
            return node
        if target < node._key:
            return self._floor(node._left, target)
        tmp = self._floor(node._right, target)
        # Status 1: 没找到比node要小的，返回的None
        if tmp != None:
            return tmp
        # Status 2: 找到了比node要小的直接返回node
        else:
            return node
    
    # 大于等于target的最大键
    def ceiling(self, target):
        node = self._ceiling(self._root, target)
        return node._key if node is not None else None
    
    def _ceiling(self, node, target):
        if node == None:
            return None
        if node._key == target:
            return node
        if target > node._key:
            return self._ceiling(node._right, target) 
        tmp = self._ceiling(node._left, target)
        
        # Status 1: 没找到比node要小的而比target还要大一点的结点，返回的None
        if tmp != None:
            return tmp
        # Status 2: 找到了比node要小的而比target还要大一点的结点，直接返回node
        else:
            return node
    
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)
        
    # 插入方法输入的是结点的地址，并且接受将要插入结点的key和value，插入过程采用
    # 递归的方式，当结点为None时候，已经到达底部，便新建一个结点。否则递归的寻找
    # 应该插入的地方。
    def _insert(self, node, key, value):
        if node == None:
            node = TreeNode(key, value)
            self._bstSize += 1
            return node
        if key < node._key:
            node._left = self._insert(node._left, key, value)
        elif key > node._key:
            node._right = self._insert(node._right, key, value)
        else:
            node._value = value
        node._size = self._sub_tree_size(node._left) + self._sub_tree_size(node._right) + 1
        return node
    
    def _sub_tree_size(self, node):
        if node == None:
            return 0
        else:
            return node._size
    
    # 最大的键
    def minimum_key(self):
        return self._minimum_key(self._root)._key
    
    def _minimum_key(self, node):
        if node == None:
            return None
        elif node._left == None:
            return node
        else:
            return self._minimum_key(node._left)
    
    # 最小的键
    def maximum_key(self):
        return self._maximum_key(self._root)
    
    def _maximum_key(self, node):
        if node == None:
            return None
        elif node._right == None:
            return node._key
        else:
            return self._maximum_key(node._right)
    
    # 小于key的键的数量
    def rank(self, key):
        nums = self._rank(self._root, key)
        return nums
    
    def _rank(self, node, key):
        pass
    
    # 排名为k的键
    def select(self, k):
        assert k >= 0 and k < self._bstSize, "Out of range!"
        node = self._select(self._root, k)
        return node._key
        
    def _select(self, node, k):
        if node == None:
            return None
        leftSize = self._sub_tree_size(node._left)
        if leftSize > k:
            return self._select(node._left, k)
        elif leftSize < k:
            return self._select(node._right, k-leftSize-1)
        else:
            return node
    
    # 删除某一个键target
    def delete(self, target):
        self._root = self._delete(self._root, target)
        self._bstSize -= 1
        
    def _delete(self, node, target):
        if node == None:
            return None
        if target > node._key:
            node._right = self._delete(node._right, target)
        elif target < node._key:
            node._left = self._delete(node._left, target)
        else:
            if node._left == None:
                return node._right
            if node._right == None:
                return node._left
            
            tmp = TreeNode(key=node._key, value=node._value, size=node._size)
            tmp._left = node._left
            tmp._right = node._right
            
            node = self._minimum_key(tmp._right)
            node._right = self._delete_minimum_key(tmp._left)
            node._left = tmp._left
        node._size = self._sub_tree_size(node._left) + self._sub_tree_size(node._right) + 1
        return node
    
    def delete_minimum_key(self):
        self._root = self._delete_minimum_key(self._root)
        self._bstSize -= 1
        
    def _delete_minimum_key(self, node):
        if node._left == None:
            return node._right
        node._left = self._delete_minimum_key(node._left)
        node._size = self._sub_tree_size(node._left) + self._sub_tree_size(node._right) + 1
        return node
    
    def delete_maximum_key(self):
        self._root = self._delete_maximum_key(self._root)
        self._bstSize -= 1
        
    def _delete_maximum_key(self, node):
        if node._right == None:
            return node._left
        node._right = self._delete_maximum_key(node._right)
        node._size = self._sub_tree_size(node._left) + self._sub_tree_size(node._right) + 1
        return node
    
    # 获取某个key对应的值，若key不存在，则返回None
    def search_key(self, target):
        assert self._root is not None, "Empty tree !"
        node = self._search_key(self._root, target)
        if node is not None:
            return node._value
        else:
            return None
    
    # 递归搜索某个结点的值
    def _search_key(self, node, target):
        if node == None:
            return None
        elif node._key > target:
            return self._search_key(node._left, target)
        elif node._key < target:
            return self._search_key(node._right, target)
        else:
            return node
    
    def pre_order_traversal(self):
        stack = []
        values = []
        node = self._root
        while(len(stack) != 0 or node):
            if node != None:
                values.append(node._key)
                stack.append(node)
                node = node._left
            else:
                node = stack.pop()
                node = node._right
        return values
    
    def in_order_traversal(self):
        stack = []
        values = []
        node = self._root
        while(len(stack) != 0 or node):
            if node != None:
                stack.append(node)
                node = node._left
            else:
                node = stack.pop()
                values.append(node._key)
                node = node._right
        return values
    
#    def post_order_traversal(self):
#        stack = []
#        values = []
#        node = self._root
#        while(len(stack) != 0 or node):
#            if node != None:
#                stack.append(node)
#                node = node._left
#            else:
#                node = stack.pop()
#                values.append(node._key)
#                node = node._right
#        return values
    
    def level_order_traversal(self):
        node = self._root
        ret, currLevel = [], [node]
        while(len(currLevel) != 0):
            ret.extend([nodeTmp._key for nodeTmp in currLevel])
            nextLevel = []
            for nodeTmp in currLevel:
                nextLevel.extend([nodeTmp._left, nodeTmp._right])
            currLevel = [nodeTmp for nodeTmp in nextLevel if nodeTmp != None]
        return ret
    
    def tree_height_recursion(self):
        pass
    
    def _tree_height_recursion(self):
        pass
    
    def is_binary_tree(self):
        pass
    
    def is_binary_search_tree(self):
        pass
###############################################################################
if __name__ == "__main__":
    values = [3.12, 0.32, 2.20, 6.12,
              1.02, 0.03, 0.67, 3.33,
              0.89, 1.12, 0.55, 5.46,
              0.63, 0.67, 0.67, 4.35,
              3.12, 0.03, 0.03, 0.03]
    bst = BinarySearchTree()
    for ind, item in enumerate(values):
        bst.insert(item, ind)
        
    # 删除最小与最大键
#    bst.delete_maximum_key()
#    bst.delete_maximum_key()
#    bst.delete_minimum_key()
#    bst.delete_minimum_key()
    bst.delete(0.32)
    
    preOrder = bst.pre_order_traversal()
    inOrder = bst.in_order_traversal()
    levelOrder = bst.level_order_traversal()
    
    print(bst.select(2))
    print(bst.floor(3))
    print(bst.ceiling(4))
    gc.collect()