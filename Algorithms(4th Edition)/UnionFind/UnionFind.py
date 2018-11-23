# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:51:23 2018

@author: Administrator
"""
###############################################################################
class union_find_base(object):
    def __init__(self, fileName=None):    
        self.fileName = fileName
        
    def load_nums(self):
        f = open(self.fileName, 'r')
        self.arraySize = int(f.readline())
        self.id = [i for i in range(self.arraySize)]
        
        lines = f.readlines()
        self.lines = [[0., 0.]] * len(lines)
        self.treeSize = [1] * len(lines) # 建立数组，用于存储树的高度
        for ind, line in enumerate(lines):
            self.lines[ind] = line.replace('\n', '').split(' ')
        f.close()
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def main(self):
        # 读取数据
        self.load_nums()
        
        for tmp in self.lines:
            pID = int(tmp[0])
            qID = int(tmp[1])
            
            # 判断二者是否相联系
            if self.connected(pID, qID):
                continue
            # 合并
            self.union(pID, qID)
        return self.id
    
###############################################################################
class union_find(union_find_base):
    def __init__(self, fileName):
        super(union_find, self).__init__(fileName)
        
    def find(self, p):
        return self.id[p]
    
    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        
        if pID == qID:
            return
        else:
            for ind, item in enumerate(self.id):
                if item == pID:
                    self.id[ind] = qID
                    
###############################################################################
class quick_union(union_find_base):
    def __init__(self, fileName=None):    
        super(quick_union, self).__init__(fileName)
        
    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return self.id[p]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        
        if pRoot == qRoot:
            return
        else:
            self.id[pRoot] = qRoot
            
###############################################################################
class weighted_quick_union(union_find_base):
    def __init__(self, fileName=None):    
        super(weighted_quick_union, self).__init__(fileName)
     
    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return self.id[p]
    
    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        
        if pRoot == qRoot:
            return
        if (self.treeSize[pRoot] < self.treeSize[qRoot]):
            self.id[pRoot] = qRoot
            self.treeSize[qRoot] += self.treeSize[pRoot]
        else:
            self.id[qRoot] = pRoot
            self.treeSize[pRoot] += self.treeSize[qRoot]
        return
    
###############################################################################
class weighted_quick_union_path_compression(union_find_base):
    def __init__(self, fileName=None):    
        super(weighted_quick_union_path_compression, self).__init__(fileName)
     
    def find(self, p):
        while (p != self.id[p]):
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return self.id[p]
    
    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        
        if pRoot == qRoot:
            return
        if (self.treeSize[pRoot] < self.treeSize[qRoot]):
            self.id[pRoot] = qRoot
            self.treeSize[qRoot] += self.treeSize[pRoot]
        else:
            self.id[qRoot] = pRoot
            self.treeSize[pRoot] += self.treeSize[qRoot]
        return

###############################################################################
if __name__ == "__main__":
    uf = weighted_quick_union_path_compression("mediumUF.txt")
    idArray = uf.main()