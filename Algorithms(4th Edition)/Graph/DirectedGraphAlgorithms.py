# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:26:53 2018

@author: XPS13
"""

from DirectedGraph import DirectedGraph, read_graph
from MyQueue import Queue
from MyStack import Stack
###############################################################################
# DFS判断有向图是否连通
class DepthFirstSearchConnected():
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
    
    def depth_first_search_connected(self, v):
        self.marked[v] = True
        for c in self.graph.vertList[v].connectedTo.keys():
            cId = c.id
            if self.marked[cId] == False:
                self.depth_first_search_connected(cId)
            else:
                continue
            
    # 输入两个顶点的id，判断两个顶点是否连通
    def is_reachable(self, v, w):
        self.marked = [False] * self.graph.numVertices
        self.marked[v] = True
        self.connected = False
        
        # 只访问v的相连接的顶点。若是相连接的顶点被标记，则可达
        for c in self.graph.vertList[v].connectedTo.keys():
            if self.marked[c] == False:
                self.depth_first_search_connected(c)
            else:
                pass
        return self.marked[w] == True
    
    # 打印出v顶点所有可达的顶点
    def print_all_reachable(self, v):
        connected = []
        self.marked = [False] * self.graph.numVertices
        self.marked[v] = True
        self.depth_first_search_connected(v)
        
        for ind, item in enumerate(self.marked):
            if item == True:
                connected.append(ind)
            else:
                continue
        print(connected)
###############################################################################
# BFS寻找结点中的最短路径
class BreadthFirstSearchDirectedPath():
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
    
    def breadth_first_search_shortest_path(self, v):
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
        # edgeTo数组实际上是一棵树
        self.tree = self.breadth_first_search_shortest_path(targetId)
        vertList = self.graph.get_vertices()
        
        
        for v in vertList:
            p = str(targetId) + " to " + str(v) + ": "
            tmp = v
            flag = 0
            while(tmp != targetId):
                if tmp == None: # 防止不连通图，有些结点没有标记爸爸节点
                    flag = 1
                    break
                p = p + str(tmp) + "-"
                # 顺着孩子访问爸爸
                tmp = self.tree[tmp]
            print(p + str(targetId)) if flag == 0 else print(p + "None")
        return self.tree
    
###############################################################################
# 寻找图中的有向环
class DirectedCycle():
    def __init__(self, edges):
        self.edges = edges
        self.cycle = []
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        newKey = sorted(list(self.graph.vertList.keys()))
        self.graph.vertList = dict([(ind, self.graph.vertList[ind]) for ind in newKey])
        
    def is_cycle(self):
        self.marked = [False] * self.graph.numVertices
        self.edgeTo = [None] * self.graph.numVertices
        self.onStack = [False] * self.graph.numVertices
        self.hasCycle = False
        
        for v in self.graph.vertList.keys():
            if self.marked[v] == False:
                self.depth_first_search_cycle(v)
            else:
                pass
        return self.hasCycle
    
    def depth_first_search_cycle(self, v):
        self.marked[v] = True
        self.onStack[v] = True
        
        for w in self.graph.vertList[v].connectedTo.keys():
            wId = w.id
            if self.hasCycle == True:
                return
            elif self.marked[wId] == False:
                self.edgeTo[wId] = v
                self.depth_first_search_cycle(wId)
            elif self.onStack[wId] == True:
                self.hasCycle = True
                self.edgeTo[wId] = v
                endPoint = wId
                while(self.edgeTo[wId] != endPoint):
                    self.cycle.append(wId)
                    wId = self.edgeTo[wId]
                self.cycle.append(wId)
        # ！！！结点需要出栈！！！
        self.onStack[v] = False
###############################################################################
# 有向图的顶点排序
# Leetcode 207: Course Schedule I(检测图中是否有环)
# Leetcode 210: Course Schedule II(对图进行拓扑排序)
# https://leetcode.com/problems/course-schedule-ii/description/
class DepthFirstOrder(object):
    def __init__(self, edges):
        self.edges = edges
        self.cycle = []
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        newKey = sorted(list(self.graph.vertList.keys()))
        self.graph.vertList = dict([(ind, self.graph.vertList[ind]) for ind in newKey])
        
    def depth_first_order(self, v):
        self.pre.enqueue(v)
        self.marked[v] = True
        
        for w in self.graph.vertList[v].connectedTo.keys():
            wId = w.id
            if self.marked[wId] == False:
                self.depth_first_order(wId)
            else:
                pass
        self.post.enqueue(v)
        self.reversePost.push(v)
    
    def print_all_order(self):
        self.pre = Queue()
        self.post = Queue()
        self.reversePost = Stack()
        self.marked = [False] * self.graph.numVertices
        
        for v in self.graph.vertList.keys():
            if self.marked[v] == False:
                self.depth_first_order(v)
            else:
                pass
        
        pre = [i for i in self.pre]
        post = [i for i in self.post]
        reversePost = [i for i in self.reversePost]
        print("Pre-order traversal: {}".format(pre))
        print("Post-order traversal: {}".format(post))
        print("Reverse-post-order traversal: {}".format(reversePost))
        return pre, post, reversePost
###############################################################################
# 有向图的强连通分量
class KosarajuSCC():
    def __init__(self, edges):
        self.edges = edges
        self.cycle = []
        
    def construct_graph(self):
        if len(self.edges) == None:
            print("Empty Edges !")
            return None
        self.graph = DirectedGraph()
        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1])
        newKey = sorted(list(self.graph.vertList.keys()))
        self.graph.vertList = dict([(ind, self.graph.vertList[ind]) for ind in newKey])
        self.reverseGraph = self.graph.reverse_graph()
    
    # 计算反向图的深度优先搜索
    def depth_first_order_reverse_graph(self, v):
        self.marked[v] = True
        for w in self.reverseGraph.vertList[v].connectedTo.keys():
            wId = w.id
            if self.marked[wId] == False:
                self.depth_first_order_reverse_graph(wId)
            else:
                pass
        # 计算反向图的逆后续
        self.reversePost.push(v)
    
    # 计算正向图的深度优先搜索
    def depth_first_order(self, v, componentId):
        self.marked[v] = True
        self.id[v] = componentId
        for w in self.graph.vertList[v].connectedTo.keys():
            wId = w.id
            if self.marked[wId] == False:
                self.depth_first_order(wId, componentId)
            else:
                pass
    
    def strongly_connected(self):
        # 第一步，计算反向图的dfs逆后续
        self.reversePost = Stack()
        self.marked = [False] * self.graph.numVertices
        for v in self.reverseGraph.vertList.keys():
            if self.marked[v] == False:
                self.depth_first_order_reverse_graph(v)
            else:
                pass
        reversePost = [i for i in self.reversePost]
        
        # 第二步，计算正向图的按逆后续访问的id数组
        self.id = [None] * self.graph.numVertices
        self.marked = [False] * self.graph.numVertices
        self.numCompoents = 0
        for v in reversePost:
            if self.marked[v] == False:
                self.depth_first_order(v, self.numCompoents)
                self.numCompoents += 1
            else:
                pass
            
    def count(self):
        return self.numCompoents
    
    def print_components(self):
        eachComponents = [ "" ] * self.count()
        for ind, item in enumerate(self.id):
            eachComponents[item] = eachComponents[item] + str(ind) + " "
        
        for ind, item in enumerate(eachComponents):
            print("Component " + str(ind) + " contains: " + str(item) )
        
###############################################################################
if __name__ == "__main__":
    edges = read_graph("tinyDG.txt")
    edges = edges[2:]
    
#    # DFS搜索所有连通的顶点
#    dfs = DepthFirstSearch(edges.copy())
#    dfs.construct_graph()
#    print("\nIs connected ?: {}".format(dfs.is_reachable(1, 2)))
#    dfs.print_all_reachable(6)
    
#    # BFS搜索所有的与v相连的最短路径
#    bfs = BreadthFirstSearch(edges.copy())
#    bfs.construct_graph()
#    tree = bfs.print_all_shortest_path(1)
    
#    # 检测有向图中是否有环，作为拓扑排序的先决条件
#    cycle = DirectedCycle(edges)
#    cycle.construct_graph()
#    res = cycle.is_cycle()
#    print("Cycle is {}".format(cycle.cycle))
    
    # 计算一幅有向图的先序，后序和逆后续遍历结果
#    order = DepthFirstOrder(edges)
#    order.construct_graph()
#    
#    res_0 = order.print_all_order()
#    order.graph = order.graph.reverse_graph()
#    order.graph = order.graph.reverse_graph()
#    res_1 = order.print_all_order()
    
    # 计算一幅有向图的强联通分支
    scc = KosarajuSCC(edges)
    scc.construct_graph()
    scc.strongly_connected()
    scc.print_components()
