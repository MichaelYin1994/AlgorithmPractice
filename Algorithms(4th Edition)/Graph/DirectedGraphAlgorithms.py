# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:26:53 2018

@author: XPS13
"""

from DirectedGraph import DirectedGraph, read_graph
from MyQueue import Queue
###############################################################################
# DFS判断图是否连通
class DepthFirstSearch():
    def __init__(self, edges):
        self.edges = edges
    
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        # 构建图
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
            
    def depth_first_search(self, v):
        self.marked[v] = True
        for c in self.graph.vertList[v].connectedTo.keys():
            cId = c.id
            if self.marked[cId] == False:
                self.depth_first_search(cId)
            else:
                continue

    def is_reachable(self, v, w):
        self.marked = [False] * self.graph.numVertices
        self.marked[v] = True
        self.connected = False
        
        # 只访问v的相连接的顶点。若是相连接的顶点被标记，则可达
        for c in self.graph.vertList[v].connectedTo.keys():
            if self.marked[c] == False:
                self.depth_first_search(c)
            else:
                pass
        return self.marked[w] == True
    
    # 打印出v顶点所有可达的顶点
    def print_all_reachable(self, v):
        connected = []
        self.marked = [False] * self.graph.numVertices
        self.marked[v] = True
        self.depth_first_search(v)
        
        for ind, item in enumerate(self.marked):
            if item == True:
                connected.append(ind)
            else:
                continue
        print(connected)
###############################################################################
# BFS寻找结点中的最短路径
class BreadthFirstSearch():
    def __init__(self, edges):
        self.edges = edges
    
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        # 构建图
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
    
    def find_shortest_path(self, v):
        self.marked = [False] * self.graph.numVertices
        self.edgeTo = [None] * self.graph.numVertices
        queue = Queue()
        queue.enqueue(v)
        self.edgeTo[v] = v
        
        while(queue.is_empty() == False):
            vertice = queue.dequeue()
            for w in self.graph.vertList[vertice].connectedTo.keys():
                wId = w.id
                if self.marked[wId] == False:
                    self.marked[wId] = True
                    self.edgeTo[wId] = vertice
                    queue.enqueue(wId)
                else:
                    continue
        return self.edgeTo
    
    def print_all_shortest_path(self, targetId):
        self.tree = self.find_shortest_path(targetId)
        vertList = self.graph.get_vertices()
        
        for v in vertList:
            p = str(targetId) + " to " + str(v) + ": "
            tmp = v
            flag = 0
            while(tmp != targetId):
                if tmp == None:
                    flag = 1
                    break
                p = p + str(tmp) + "-"
                tmp = self.tree[tmp]
            print(p + str(targetId)) if flag == 0 else print(p + "None")
        return self.tree
    
###############################################################################
class Cycle():
    def __init__(self, edges):
        self.edges = edges
    
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        # 构建图
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
    
    
###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyDG.txt")
    edges = edges[2:]
    
    # DFS搜索所有连通的顶点
#    dfs = DepthFirstSearch(edges.copy())
#    dfs.construct_graph()
#    print("\nIs connected ?: {}".format(dfs.is_reachable(1, 2)))
#    dfs.print_all_reachable(0)
    
    # BFS搜索所有的与v相连的最短路径
#    bfs = BreadthFirstSearch(edges.copy())
#    bfs.construct_graph()
#    tree = bfs.print_all_shortest_path(7)
    