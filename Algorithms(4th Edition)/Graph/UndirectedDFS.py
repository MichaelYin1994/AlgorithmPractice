# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:16:09 2018

@author: XPS13
"""
from UndirectedGraph import UndirectedGraph, read_graph
#from MyQueue import Queue
from MyQueue import Queue
###############################################################################
class DepthFirstSearch():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        
    def depth_first_search(self, graph, vertice):
        self.marked[vertice] = True
        # 遍历vertice的邻接节点，v是一个Vertex的实例，很麻烦:(
        for v in self.graph.vertList[vertice].connectedTo.keys():
            vId = v.id
            if self.marked[vId] == True:
                continue
            else:
                self.depth_first_search(self.graph, vId)
    
    def depth_first_path(self, graph, vertice):
        self.marked[vertice] = True
        # 遍历vertice的邻接节点，v是一个Vertex的实例，很麻烦:(
        for v in self.graph.vertList[vertice].connectedTo.keys():
            vId = v.id
            if self.marked[vId] == True:
                continue
            else:
                self.tree[vId] = vertice
                self.depth_first_path(self.graph, vId)
        return self.tree
    
    def is_conected(self):
        source = self.graph.get_vertices()[0]
        self.marked = [False] * self.graph.numVertices
        self.depth_first_search(self.graph, source)
        return self.marked
    
    # 找出所有与targetId相连的路径
    def find_path(self, targetId):
        vertList = self.graph.get_vertices()
        self.marked = [False] * self.graph.numVertices
        self.tree = [None] * self.graph.numVertices
        self.tree = self.depth_first_path(self.graph, targetId)
        
        for v in vertList:
            p = str(targetId) + " to " + str(v) + " :"
            tmp = v
            while(tmp != targetId):
                p = p + str(tmp) + "-"
                tmp = self.tree[tmp]
            print(p + str(targetId))
###############################################################################
class BreadthFirstSearch():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
    
    def breadth_first_search_path(self, targetId):
        marked = [ False ] * self.graph.numVertices
        edgeTo = [ None ] * self.graph.numVertices
        queue = Queue()
        queue.enqueue(self.graph.vertList[targetId])
        
        marked[targetId] = True
        while(queue.is_empty() == False):
            vertice = queue.dequeue()
            for v in vertice.connectedTo.keys():
                vId = v.id
                if marked[vId] == False:
                    queue.enqueue(v)
                    marked[vId] = True
                    edgeTo[vId] = vertice.id
        return edgeTo
    
    def find_shorest_path(self, targetId):
        self.tree = self.breadth_first_search_path(targetId)
        vertList = self.graph.get_vertices()
        
        for v in vertList:
            p = "\n" + str(targetId) + " to " + str(v) + " :"
            tmp = v
            while(tmp != targetId):
                p = p + str(tmp) + "-"
                tmp = self.tree[tmp]
            print(p + str(targetId))
        return self.tree
    
###############################################################################
class ConnectedComponents():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        
    # 判断图是否连通
    def check_connected(self):
        return None not in self.id
    
    # 判断两个顶点是否连通
    def is_connected(self, v, w):
        return self.id[v] == self.id[w] if self.id[v] != None and self.id[w] != None else False
    
    # 连通分量的个数
    def count(self):
        return self.numCompoents
    
    def dfs(self, verticeId, componentId):
        self.marked[verticeId] = True
        self.id[verticeId] = componentId
        for v in self.graph.vertList[verticeId].connectedTo.keys():
            vId = v.id
            if self.marked[vId] == None:
                self.dfs(vId, componentId)
            else:
                pass
    
    def calc_connected(self):
        self.marked = [None] * len(self.graph.vertList)
        self.id = [None] * len(self.graph.vertList)
        
        self.numCompoents = 0
        for ind, item in enumerate(self.marked):
            if item == None:
                self.dfs(ind, self.numCompoents)
                self.numCompoents += 1
            else:
                pass
            
    def print_components(self):
        eachComponents = [ "" ] * self.count()
        for ind, item in enumerate(self.id):
            eachComponents[item] = eachComponents[item] + str(ind) + " "
        
        for ind, item in enumerate(eachComponents):
            print("Component " + str(ind) + " contains: " + str(item) )
###############################################################################
class Cycle():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
    
    def has_cycle(self):
        pass
###############################################################################
class TwoColor():
    def __init__(self, edges):
        self.edges = edges
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])

###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyCG.txt")
    edges = edges[2:]
    
#    bfs = BreadthFirstSearch(edges)
#    bfs.construct_graph()
#    edgeTo = bfs.find_shorest_path(0)
    
#    dfs = DepthFirstSearch(edges)
#    dfs.construct_graph()
#    marked = dfs.is_conected()
#    dfs.find_path(0)
    
    cc = ConnectedComponents(edges)
    cc.construct_graph()
    cc.calc_connected()
    print(cc.check_connected(), cc.count())
    cc.print_components()
    res = cc.id