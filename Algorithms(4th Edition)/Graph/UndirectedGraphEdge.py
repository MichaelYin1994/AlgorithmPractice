# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:05:20 2018

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
class UndirectedGraphEdge():
    def __init__(self):
        self.vertList = {}
        self.numEdges = 0
    
    def add_edge(self, first, second, weight=0):
        if first not in self.vertList:
            self.vertList[first] = []
        if second not in self.vertList:
            self.vertList[second] = []
        edge = Edge(first, second, weight)
        
        bagListTmp = self.vertList[first]
        bagListTmp.append(edge)
        self.vertList[first] = bagListTmp
        
        bagListTmp = self.vertList[second]
        bagListTmp.append(edge)
        self.vertList[second] = bagListTmp
        
        self.numEdges += 1
    
    # 返回Edge列表
    def get_vertices(self):
        return list(self.vertList.keys())
###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyEWG.txt")
    numVertices = edges[0][0]
    numEdges = edges[1][0]
    edges = edges[2:]
    
    g = UndirectedGraphEdge()
    for edge in edges:
        g.add_edge(edge[0], edge[1], weight=edge[2])