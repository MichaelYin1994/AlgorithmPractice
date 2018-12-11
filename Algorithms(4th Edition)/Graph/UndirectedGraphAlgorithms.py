# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:16:09 2018

@author: XPS13
"""
from UndirectedGraph import UndirectedGraph, read_graph
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
# 搜索最短路径，对应最短路径问题
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
        # 显式的使用队列，保存邻接的顶点
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
    
    # 基于BFS寻找最短的路径
    def find_shortest_path(self, targetId):
        self.tree = self.breadth_first_search_path(targetId)
        vertList = self.graph.get_vertices()
        
        # 防止不连通的现象发生，self.edgeTo索引为None，发生错误
        # 代码待修改
#        if tmp == None:
#                print(p + "None")
#                break
        
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
        self.hasCycle = False
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None

        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        
    def dfs(self, father, child):
        self.marked[father] = True
        
        for w in self.graph.vertList[child].connectedTo.keys():
            wId = w.id
            if self.marked[wId] == False:
                self.dfs(child, wId)
            # 若顶点w出现在child顶点的邻接节点集合里面，
            # 并且该顶点不是child顶点的父节点，则肯定是带环的。
            elif wId != father:
                self.hasCycle = True
    
    def has_cycle(self):
        self.marked = [False] * self.graph.numVertices
        
        for v in self.graph.vertList.keys():
            if self.marked[v] == False:
                self.dfs(v, v)
            else:
                continue
        return self.hasCycle
###############################################################################
class TwoColor():
    def __init__(self, edges):
        self.edges = edges
        self.isTwoColorable = True

    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        
        # 构建图
        self.graph = UndirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
    
    def dfs(self, v):
        self.marked[v] = True
        for w in self.graph.vertList[v].connectedTo.keys():
            wId = w.id
            if self.marked[wId] == False:
                self.color[wId] =  'black' if self.color[v] == 'red' else 'black'
                self.dfs(wId)
            elif self.color[wId] == self.color[v]:
                self.isTwoColor = False
                
    def is_two_color(self):
        self.marked = [ False ] * self.graph.numVertices
        self.color = [ 'red' ] * self.graph.numVertices
        
        for v in self.graph.vertList.keys():
            if self.marked[v] == False:
                self.dfs(v)
            else:
                pass
###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyCG.txt")
    edges = edges[2:]
    
#    # BFS搜索最短路径测试
#    bfs = BreadthFirstSearch(edges)
#    bfs.construct_graph()
#    edgeTo = bfs.find_shorest_path(0)
    
    # DFS判断图是否连通
#    dfs = DepthFirstSearch(edges)
#    dfs.construct_graph()
#    marked = dfs.is_conected()
#    dfs.find_path(0)
    
#    # CC判断连通集的个数
#    cc = ConnectedComponents(edges)
#    cc.construct_graph()
#    cc.calc_connected()
#    print(cc.check_connected(), cc.count())
#    cc.print_components()
#    res = cc.id
    
    # 判断图是不是有环
#    cycle = Cycle(edges)
#    cycle.construct_graph()
#    print("Is looped?: {}".format(cycle.has_cycle()))
    
    # TwoColor判断图是不是双色图
#    color = TwoColor(edges)
#    color.construct_graph()
#    color.is_two_color()
#    print("Is two colorable: {}".format(color.isTwoColorable))