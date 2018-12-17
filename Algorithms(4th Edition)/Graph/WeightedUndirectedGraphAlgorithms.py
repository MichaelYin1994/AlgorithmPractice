# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:19:41 2018

@author: XPS13
"""
from UndirectedGraphEdge import Edge, UndirectedGraphEdge, read_graph
from UnionFind import WeightedQuickUnionPathCompression
from MinIndexHeap import IndexMinHeap
from MyQueue import Queue
###############################################################################
class LazyPrimMst():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = UndirectedGraphEdge()
        for edge in self.edges:
            self.graph.add_edge(int(edge[0]), int(edge[1]), weight=edge[2])
    
    # 将vId号顶点与vId对应的边都加入优先队列中
    def visit(self, vId):
        self.marked[vId] = True
        for edge in self.graph.vertList[vId]:
            # 若是vId对应的另外的顶点被标记过，说明边失效
            # 两个顶点都已经在最小生成树之中
            if self.marked[edge.other(vId)] == False:
                self.weightPriorityQueue.insert(edge.weight, edge)
        
    def lazy_prim(self):
        numEdges = len(self.edges)
        numVertices = len(self.graph.vertList)
        
        # 初始化对于边的优先队列与队列
        self.weightPriorityQueue = IndexMinHeap(numEdges)
        self.mstQueue = Queue()
        self.marked = [False] * numVertices
        
        # 默认先从0号顶点开始访问
        self.visit(0)
        while(self.weightPriorityQueue.__len__() != 0):
            weight, edge = self.weightPriorityQueue.extract_min()
            vId = edge.either()
            wId = edge.other(vId)
            
            if (self.marked[vId] == True) and (self.marked[wId] == True):
                continue
            self.mstQueue.enqueue(edge)
            if self.marked[vId] != True:
                self.visit(vId)
                
            if self.marked[wId] != True:
                self.visit(wId)
    
    def print_mst(self):
        self.lazy_prim()
        res = []
        while(self.mstQueue.is_empty() != True):
            edgeTmp = self.mstQueue.dequeue()
            res.append([edgeTmp.either(), edgeTmp.other(edgeTmp.either())])
        return res
###############################################################################    
###############################################################################
class PrimMst():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = UndirectedGraphEdge()
        for edge in self.edges:
            self.graph.add_edge(int(edge[0]), int(edge[1]), weight=edge[2])
    
    def visit(self, vId):
        self.marked[vId] = True
        for edge in self.graph.vertList[vId]:
            wId = edge.other(vId)
            
            # 边的两端都是树节点，失效这条边
            if self.marked[wId] == True:
                continue
            if edge.weight < self.distTo[wId]:
                self.distTo[wId] = edge.weight
                self.edgeTo[wId] = edge
                
                # 更新与树结点相连的非树顶点的最小边权值
                if self.weightPriorityQueue.contains(wId):
                    self.weightPriorityQueue.change(edge.weight, edge)
                else:
                    self.weightPriorityQueue.insert(edge.weight, edge)
        
    def prim(self):
        numEdges = len(self.edges)
        numVertices = len(self.graph.vertList)
        
        # 初始化edgeTo[], marked[]数组
        self.marked = [False] * numVertices
        self.edgeTo = [None] * numVertices
        self.distTo = [float("inf")] * numVertices
        
        # 初始化对于边的优先队列与队列
        self.weightPriorityQueue = IndexMinHeap(numEdges)
        
        self.distTo[0] = 0
        self.visit(0)
        while(self.weightPriorityQueue.__len__ != 0):
            weight, edge = self.weightPriorityQueue.extract_min()
            self.visit(edge.other(edge.either()))
        
    def print_mst(self):
        self.prim()
        res = []
        for i in range(len(self.edgeTo)):
            res.append([self.edgeTo[i].either(), self.edgeTo[i].other(self.edgeTo[i].either())])
        return res
###############################################################################    
###############################################################################
class KruskalMst():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = UndirectedGraphEdge()
        for edge in self.edges:
            self.graph.add_edge(int(edge[0]), int(edge[1]), weight=edge[2])
    
    # Tips: 理论上不需要用到存储边的图，只需要将边按权加入优先队列，
    # 然后挨个索引就可以了
    def kruskal(self):
        numEdges = len(self.edges)
        numVertices = len(self.graph.vertList)
        
        # 初始化对于边的优先队列与队列
        self.weightPriorityQueue = IndexMinHeap(numEdges)
        self.mstQueue = Queue()
        self.uf = WeightedQuickUnionPathCompression(numVertices)
        
        # 所有边按weight进入优先队列
        for edge in self.edges:
            weight = edge[2]
            e = [int(edge[0]), int(edge[1])]
            self.weightPriorityQueue.insert(weight, e)
            
        # 条件1：优先队列为空
        # 条件2：mst的边的个数等于numVertices - 1（树的条件）
        while(self.weightPriorityQueue.__len__ != 0 and self.mstQueue._queueSize < numVertices-1):
            weight, edge = self.weightPriorityQueue.extract_min()
            vId = edge[0]
            wId = edge[1]
            
            if self.uf.connected(vId, wId):
                continue
            self.uf.union(vId, wId)
            self.mstQueue.enqueue(edge)
        
    def print_mst(self):
        self.kruskal()
        res = []
        while(self.mstQueue.is_empty() != True):
            edgeTmp = self.mstQueue.dequeue()
            res.append([edgeTmp[0], edgeTmp[1]])
        return res
###############################################################################    
###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyEWG.txt")
    numVertices = edges[0][0]
    numEdges = edges[1][0]
    edges = edges[2:]
    
    # Prim算法的延时形式
#    lazyprim = LazyPrimMst(edges)
#    lazyprim.construct_graph()
#    res_1 = lazyprim.print_mst()
    
    # Prim算法的实时形式
    prim = PrimMst(edges)
    prim.construct_graph()
    res_2 = prim.print_mst()
    
    # Kruskal算法
#    kruskal = KruskalMst(edges)
#    kruskal.construct_graph()
#    res_3 = kruskal.print_mst()