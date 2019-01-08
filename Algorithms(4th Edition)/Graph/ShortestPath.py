# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:13:16 2019

@author: XPS13
"""
from DirectedGraphEdge import DirectedEdge, DirectedGraphEdge, read_graph
from IndexMinHeap import IndexMinHeap
from MyStack import Stack
from functools import wraps
import time
###############################################################################
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print("@timefn: " + fn.__name__ + " took " + str(end-start) + " seconds")
        return result
    return measure_time

###############################################################################
###############################################################################
class DijkstraSP():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = DirectedGraphEdge()
        for edge in self.edges:
            self.graph.add_edge(int(edge[0]), int(edge[1]), weight=edge[2])
    
    def dijkstra_shortest_path(self, source=0):
        numVertices = len(self.graph.vertList)
        self.source = source
        
        # 初始化edgeTo[], marked[], distTo[]数组
        self.edgeTo = [None] * numVertices
        self.distTo = [float("inf")] * numVertices
        
        # 初始化对于边的优先队列与队列
        self.indexMinHeap = IndexMinHeap(numVertices)
        self.distTo[source] = 0
        self.indexMinHeap.insert(source, 0)
        
        while(len(self.indexMinHeap) != 0):
            valMin, keyMin = self.indexMinHeap.extract_min()
            self.relax_node(keyMin)
    
    # 优先队列里始终保持着从source到达wId的最短距离
    def relax_node(self, source):
        for edge in self.graph.vertList[source]:
            wId = edge.destination()
            if self.distTo[wId] > self.distTo[source] + edge.weight:
                self.distTo[wId] = self.distTo[source] + edge.weight
                self.edgeTo[wId] = edge
                
                if self.indexMinHeap.contains(wId):
                    self.indexMinHeap.change(wId, self.distTo[wId])
                else:
                    self.indexMinHeap.insert(wId, self.distTo[wId])
    
    def distance_to(self, targetId=0):
        print("From " + str(self.source) + " to " + str(targetId) + ": " + str(self.distTo[targetId]))
        return self.distTo[targetId]
    
    def has_path_to(self, targetId=0):
        return self.distTo[targetId] < float("inf")
    
    def path_to(self, targetId=0):
        if self.has_path_to(targetId) is False:
            return None
        
        res = "Path from " + str(self.source) + " to " + str(targetId) + ": "
        stack = Stack()
        edgeTmp = self.edgeTo[targetId]
        stack.push(targetId)
        while(edgeTmp is not None):
            targetId = edgeTmp.origin()
            stack.push(targetId)
            edgeTmp = self.edgeTo[targetId]
        
        for i in stack:
            res = res + str(i) + "-->"
        return res
        
        
###############################################################################    
###############################################################################
if __name__ == "__main__":
    edges = read_graph("mediumEWD.txt")
    numVertices = edges[0][0]
    numEdges = edges[1][0]
    edges = edges[2:]
    
    # Dijkstra算法的即时形式
    sp = DijkstraSP(edges.copy())
    sp.construct_graph()
    sp.dijkstra_shortest_path(source=0)
    res = sp.distTo
    
    sp.distance_to(targetId=6)
    print(sp.has_path_to(targetId=6))
    print(sp.path_to(targetId=6))