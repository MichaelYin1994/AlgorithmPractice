# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:31:47 2018

@author: XPS13
"""
###############################################################################
def read_graph(filePath=None):
    assert filePath, "Invalid Path !"
    data = []
    with open(filePath, 'r') as f:
        data = f.readlines()
    data = [list(map(float, str.split(x))) for x in data]
    return data
###############################################################################
###############################################################################
class MinPriorityQueue():
    def __init__(self, maxSize):
        # Count扮演了堆目前的最大尺寸的角色
        self._keys = maxSize * [None]
        self._values = maxSize * [None]
        self._count = 0
        self._maxSize = maxSize
        
    def __len__(self):
        return self._count
    
    def less(self, pos_1, pos_2):
        return self._keys[pos_1] < self._keys[pos_2]
    
    def exchange(self, pos_1, pos_2):
        tmp = self._keys[pos_1]
        self._keys[pos_1] = self._keys[pos_2]
        self._keys[pos_2] = tmp
        
        tmp = self._values[pos_1]
        self._values[pos_1] = self._values[pos_2]
        self._values[pos_2] = tmp
        
    def capacity(self):
        return len(self._keys)
    
    def sink(self, pos):
        while(2*pos <= self._maxSize):
            left = 2 * pos + 1
            right = 2 * pos + 2
            minum = pos
            # 这里先判断左右孩子是不是存在，再交换值（可能比较的次数会增多）
            if (left < self._count) and (self.less(left, pos)):
                minum = left
            if (right < self._count) and (self.less(right, minum)):
                minum = right
            if minum == pos:
                break
            else:
                self.exchange(pos, minum)
                pos = minum
                
    def swim(self, pos):
        # 设想[5, 12, 3]这种有3个元素的堆来套问题
        # (pos-1) // 2)计算pos父亲节点的值的大小
        while(pos > 0 and self.less(pos, (pos-1) // 2)):
            self.exchange((pos-1) // 2, pos)
            pos = (pos-1) // 2
    
    # 是否存在索引为k的元素
    def contains(self, k):
        return k in self._keys
    
    # 将索引为k的元素改为item
    def change(self, k, item):
        self._keys[k] = item
        
    # 输入键key, 值value对
    def insert(self, key, value):
        assert self._count < self.capacity(), "Cannot add an element to a full heap."
        self._keys[self._count] = key
        self._values[self._count] = value
        
        self.swim(self._count)
        self._count += 1
    
    def extract_min(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        key = self._keys[0]
        value = self._values[0]
        
        self._keys[0] = self._keys[self._count - 1]
        self._keys[self._count - 1] = None
        self._values[0] = self._values[self._count - 1]
        self._values[self._count - 1] = None
        self._count -= 1
        self.sink(0)
        return key, value
###############################################################################
###############################################################################
class Edge():
    def __init__(self, vertice_1, vertice_2, weight):
        self.vertice_1 = vertice_1
        self.vertice_2 = vertice_2
        self.weight = weight
    
    def get_weight(self):
        return self.weight
    
    # 返回一个顶点的编号
    def either(self):
        return self.vertice_1
    
    # 返回边的另外一个顶点的编号
    def other(self, verticeId):
        if verticeId == self.vertice_1:
            return self.vertice_2
        elif verticeId == self.vertice_2:
            return self.vertice_1
        else:
            return None
    # compare_to方法，传入一个Edge的实例，返回
    # 边的权值的对比结果：
    # +1: 该边大于传入的边
    # 0: 该边权值与传入的边相等
    # -1: 该边的权值小于传入的边
    def compare_to(self, edgeObj):
        weightTmp = edgeObj.weight
        if self.weight == weightTmp:
            return 0
        elif self.weight > weightTmp:
            return 1
        elif self.weight < weightTmp:
            return -1

###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyEWG.txt")
    numVertices = edges[0][0]
    numEdges = edges[1][0]
    edges = edges[2:]
    maxHeapSize = int(numEdges)
    
    pq = MinPriorityQueue(maxHeapSize)
    for edge in edges:
        pq.insert(edge[2], Edge(int(edge[0]), int(edge[1]), edge[2]))
    
    res = []
    for i in range(maxHeapSize):
        weightTmp, edgeTmp = pq.extract_min()
        res.append([weightTmp, edgeTmp.either(), edgeTmp.other(edgeTmp.either())])