# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:59:39 2018

@author: XPS13
"""
import gc
import sys
###############################################################################
def read_graph(filePath=None):
    assert filePath, "Invalid Path !"
    data = []
    with open(filePath, 'r') as f:
        data = f.readlines()
    data = [list(map(int, str.split(x))) for x in data]
    return data

###############################################################################
class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def __str__(self):
        return "Vertex " + str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    # 这里的Vertex对应的字典的key存储的是相连接的Vertex内存地址
    def get_connections(self):
        return self.connectedTo.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, nbr):
        return self.connectedTo[nbr]

###############################################################################
# vertList: dict，key是顶点id，value是Vertex的object类型，
# Vertex包含两个主要部分：int类型的id，dict类型的connectedTo。
# numVertices：顶点的个数。
# numEdges：边的个数。

class UndirectedGraph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0
        
    def __contains__(self, key):
        return key in self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def add_edge(self, first, second, weight=0):
        if first not in self.vertList:
            newVertex = self.add_vertex(first)
        if second not in self.vertList:
            newVertex = self.add_vertex(second)
        
        # 无向图体现之处
        self.vertList[first].add_neighbor(self.vertList[second], weight=weight)
        self.vertList[second].add_neighbor(self.vertList[first], weight=weight)
        self.numEdges += 1
    
    # 返回key对应的顶点
    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    # 计算无向图的度数
    def degree(self, vertexId):
        if vertexId not in self.vertList.keys():
            return None
        else:
            vertex = self.vertList[vertexId]
            return len(vertex.connectedTo)
    
    # 计算所有顶点的最大的度数
    def max_degree(self):
        maxDegree = 0
        for ind in self.vertList.keys():
            tmp = self.degree(ind)
            if tmp > maxDegree:
                maxDegree = tmp
        return maxDegree
    
    # 计算平均的度数
    def mean_degree(self):
        totalDegree = 0
        for ind in self.vertList.keys():
            tmp = self.degree(ind)
            totalDegree += tmp
        return totalDegree / self.numVertices if self.numVertices != 0 else 0
    
    # 计算自环的数目
    def number_of_self_loops(self):
        loops = 0
        # vertex_1是第一个顶点
        for ind in self.vertList.keys():
            vertex_1 = self.vertList[ind]
            # vertex_1.connectedTo是字典，key是vertex object类型。
            for vertex_2 in vertex_1.connectedTo.keys():
                if vertex_1.id == vertex_2.id:
                    loops += 1
        return loops
    
    # 返回Vertex列表
    def get_vertices(self):
        return list(self.vertList.keys())

if __name__ == "__main__":
    g = UndirectedGraph()
    for i in range(10):
        g.add_vertex(i)
    
#    g.add_edge(0, 1, 10)
#    g.add_edge(14, 13, 5)
#    g.add_edge(2, 3, 7)
#    g.add_edge(10, 1, 10)
#    g.add_edge(99, 5, 43)
#    g.add_edge(32, 2, 10)
#    g.add_edge(5, 7, 1)
#    g.add_edge(6, 1, 5)
#    g.add_edge(10, 5, 9)
#    
#    for v in g:
#        print(v)
    
    edges = read_graph("tinyG.txt")
    edges = edges[2:]
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    for v in g:
        print(v)
        
    print("\nMax degree : {}".format(g.max_degree()))
    print("Mean degree : {}".format(g.mean_degree()))
    print("Total edges : {}".format(g.numEdges))
    print("Self loops : {}".format(g.number_of_self_loops()))