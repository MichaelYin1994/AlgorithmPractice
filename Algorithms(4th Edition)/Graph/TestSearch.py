# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:28:48 2018

@author: XPS13
"""
from pythongraph import UndirectedGraph, Vertex, read_graph
class TestSearchMethod():
    def __init__(self, edges):
        self.edges = edges
    
    def test_search(self):
        g = UndirectedGraph()
        for edge in edges:
            g.add_edge(edge[0], edge[1])
            