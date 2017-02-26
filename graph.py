#!/usr/bin/env python
# Author   guojy8993@163.com
# Date     2017/02/25
# Desc     Graph theory algorithm

'''
Ref: http://blog.csdn.net/zhujunxxxxx/article/details/28429369
'''

class Graph(object):
    def __init__(self, *args, **kwargs):
        self.neighbors = {}
        self.visited = {}


    def add_edge(self, edge):
        u, v = edge
        if v not in self.neighbors[u] \
            and u not in self.neighbors[v]:
            self.neighbors[u].append(v)
            if u != v:
                self.neighbors[v].append(u)

    def nodes(self):
        return self.neighbors.keys()

    def add_node(self, node):
        if node not in self.neighbors:
            self.neighbors[node] = []

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def depth_first_search(self, root=None):
        order = []
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.neighbors[node]:
                if n not in self.visited:
                    dfs(n)
        if root:
            dfs(root)
        for node in self.nodes():
            if node not in self.visited:
                dfs(node)
        print order
        return order

    def breadth_first_search(self, root=None):
        queue = []
        order = []
        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.neighbors[node]:
                    if n not in self.visited and n not in queue:
                        queue.append(n)
                        order.append(n)
        if root:
            queue.append(root)
            order.append(root)
            bfs()
        for node in self.nodes():
            if node not in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print order
        return order

if __name__ == "__main__":
    g = Graph()
    g.add_nodes([ i+1 for i in range(8) ])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    
    print "nodes: %s" % g.nodes()
    order = g.depth_first_search(1)
    print "Depth First Search: %s" % order
    order = g.breadth_first_search(1)
    print "Breadth First Search: %s" % order

