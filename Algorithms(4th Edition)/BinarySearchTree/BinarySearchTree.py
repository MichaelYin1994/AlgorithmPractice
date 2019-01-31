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
Create Date: 2018/12/25
Modified Date: 2019/1/2
Mail: zhuoyin94@163.com
Title: 二叉搜索树(Binary Search Tree)的实现。
-------------------------------------------------------------------------------
self.__init__(self, maxSize):
    初始化相关参数，其中root初始化为None，初始化bstSize为搜索树的大小。

self.__contains__(self):
    是否包含特定的键值对。

self.floor(self, target):
    小于等于target的最大键。

self._floor(self, node, target):
    floor的私有方法的实现。

self.ceiling(self, target):
    大于等于target的最大键e。

self._ceiling(self, target):
    ceiling方法的私有的实现。

self.insert(self, key, value):
    插入键值对。
    
self._insert(self, node, key, value):
    插入键值对的私有方法。

self._sub_tree_size(self, pos):
    计算以pos为根结点的树的结点个数。
    
self.minimum_key(self):
    BST的最小键。

self._maximum_key(self, node)：
    BST的最小键搜索递归。
    
self.select(self, k):
    BST中key排名为k的结点的值。

self._select(self, node, k):
    BST中key排名为k的结点的值，递归搜索。

self.delete(self, target):
    删除key为target的结点。

self._delete(self, node, target):
    删除方法的递归。

self.delete_minimum_key(self):
    删除最小的键。

self._delete_minimum_key(self, node):
    递归删除最小键。



self.swim(self, pos):
    对堆中pos位置的元素进行上浮。

self.swim(self, pos):
    对堆中pos位置的元素进行上浮。

self.swim(self, pos):
    对堆中pos位置的元素进行上浮。
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
    
    # 全树最大的键
    def minimum_key(self):
        return self._minimum_key(self._root)._key
    
    def _minimum_key(self, node):
        if node == None:
            return None
        elif node._left == None:
            return node
        else:
            return self._minimum_key(node._left)
    
    # 全树最小的键
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
    
    # 递归的删除某一个键target
    # 450. Delete Node in a BST:
    # https://leetcode.com/problems/delete-node-in-a-bst/description/
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
            # 确认node的左右孩子是否为空，确保后面删除的结点两个孩子都在
            if node._left == None:
                return node._right
            if node._right == None:
                return node._left
            
            # 保存当前结点node的各个值
            tmpNode = TreeNode(key=node._key, value=node._value, size=node._size)
            tmpNode._left = node._left
            tmpNode._right = node._right
            
            # 关键操作，找到tmpNode的右边的后继结点，并覆盖node的值
            node = self._minimum_key(tmpNode._right)
            
            # 删除将要删除的结点tmpNode的右子树的先序结点，并返回右子树根结点
            node._right = self._delete_minimum_key(tmpNode._right)
            node._left = tmpNode._left
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
        while(stack or node):
            if node != None:
                stack.append(node)
                node = node._left
            else:
                node = stack.pop()
                values.append(node._key)
                node = node._right
        return values
    
    # https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse?orderBy=most_votes
    # left-right-root ==> root-right-left
    def post_order_traversal(self):
        stack = []
        values = []
        node = self._root
        while stack or node:
            if node is not None:
                stack.append(node)
                values.append(node._key)
                node = node._right
            else:
                node = stack.pop()
                node = node._left
        return values[::-1]
    
    def post_order_traversal_flag(self):
        stack = [(self._root, False)]
        node = self._root
        values = []
        while stack:
            node, used = stack.pop()
            if node is not None:
                if used is True:
                    values.append(node._key)
                else:
                    # 右结点先入栈，然后是左结点入栈，这样stack.pop出来的先是左结点
                    # 然后是右结点，符合后序遍历的顺序
                    stack.append((node, True))
                    stack.append((node._right, False))
                    stack.append((node._left, False))
        return values
    
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
    
    # 树的最大高度
    # 104. Maximum Depth of Binary Tree:
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
    def tree_maximum_height_recursion(self):
        return self._tree_maximum_height_recursion(self._root, 0)
    
    def _tree_maximum_height_recursion(self, node, currHeight):
        if node == None:
            return currHeight
        leftHeight = self._tree_maximum_height_recursion(node._left, currHeight + 1)
        rightHeight = self._tree_maximum_height_recursion(node._right, currHeight + 1)
        return max(leftHeight, rightHeight)
    
    # 计算树的最小高度
    # 最小深度定义为：从根结点出发到没有孩子的叶子结点的路径上的结点的个数
    # 111. Minimum Depth of Binary Tree:
    # https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
    def tree_minimum_height(self):
        currStack = [self._root]
        height = 1
        while(currStack):
            nextStack = []
            for tmpNode in currStack:
                if tmpNode._left == None and tmpNode._right == None:
                    return height
                else:
                    nextStack.extend([tmpNode._left, tmpNode._right])
            currStack = [node for node in nextStack if node is not None]
            height += 1
        return height
    
    # 检查是否为二叉搜索树
    # 98. Validate Binary Search Tree:
    # https://leetcode.com/problems/validate-binary-search-tree/description/
    def is_binary_search_tree(self):
        if self._root is None:
            return True
        nodeStack = [self._root]
        values = []
        node = self._root._left
        
        # 必须nodeStack与node都空才推出循环，有可能nodeStack为空而node不
        # 为空，继续往栈里压元素
        while(nodeStack or node):
            if node != None:
                nodeStack.append(node)
                node = node._left
            else:
                tmpNode = nodeStack.pop()
                values.append(tmpNode._key)
                node = tmpNode._right
            if len(values) >= 2 and values[-1] <= values[-2]:
                return False
        return True
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
    totalKeys = bst.in_order_traversal()
    bst.delete(0.63)
    bst.delete(2.2)
    
    preOrder = bst.pre_order_traversal()
    inOrder = bst.in_order_traversal()
    postOrder = bst.post_order_traversal()
    postOrderFlag = bst.post_order_traversal_flag()
    levelOrder = bst.level_order_traversal()
    
    print(bst.select(2))
    print(bst.floor(3))
    print(bst.ceiling(4))
    print("Is binary search tree : {}".format(bst.is_binary_search_tree()))
    print("Minimum height :{}".format(bst.tree_minimum_height()))
    print("Maximum height :{}".format(bst.tree_maximum_height_recursion()))
    gc.collect()