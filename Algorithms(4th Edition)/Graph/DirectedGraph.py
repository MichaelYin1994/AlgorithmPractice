# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 19:12:22 2018

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

class DirectedGraph():
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
        
        self.vertList[first].add_neighbor(self.vertList[second], weight=weight)
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
    
    # 计算有向图的反向图
    def reverse_graph(self):
        newGraph = DirectedGraph()
        for vId in self.vertList.keys():
            for w in self.vertList[vId].connectedTo.keys():
                wId = w.id
                newGraph.add_edge(wId, vId)
        return newGraph
    
    # 返回Vertex列表
    def get_vertices(self):
        return list(self.vertList.keys())

if __name__ == "__main__":
    g = DirectedGraph()
    
    edges = read_graph("tinyDG.txt")
    edges = edges[2:]
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    for v in g:
        print(v)
        
    print("\nMax degree : {}".format(g.max_degree()))
    print("Mean degree : {}".format(g.mean_degree()))
    print("Total edges : {}".format(g.numEdges))
    
    print("\nNew graph:")
    newGraph = g.reverse_graph()
    for v in newGraph:
        print(v)