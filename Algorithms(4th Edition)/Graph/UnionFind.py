# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:04:29 2018

@author: XPS13
"""
###############################################################################
def read_data(filePath=None):
    assert filePath, "Invalid Path !"
    data = []
    with open(filePath, 'r') as f:
        data = f.readlines()
    data = [list(map(int, str.split(x))) for x in data]
    return data

###############################################################################
class WeightedQuickUnionPathCompression():
    def __init__(self, arraySize):    
        self.id = [i for i in range(arraySize)]
        self.treeSize = [1] * arraySize
        self.arraySize = arraySize
    
    # 寻找p节点的根节点
    def find(self, p):
        while (p != self.id[p]):
            # Path compression, 孙子结点的爸爸不是
            # 树的头结点，将孙子结点的爸爸设为爷爷结点
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return self.id[p]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
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
    
    def main(self, data):
        # 读取数据
        self.lines = data
        
        for tmp in self.lines:
            pID = int(tmp[0])
            qID = int(tmp[1])
            
            # 判断二者是否相联系
            if self.connected(pID, qID):
                continue
            else:
                self.union(pID, qID)
        return self.id
###############################################################################
if __name__ == "__main__":
    data = read_data("tinyUF.txt")
    numVertices = data[0][0]
    data = data[1:]
    uf = WeightedQuickUnionPathCompression(numVertices)
    res = uf.main(data)