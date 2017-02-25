#!/usr/bin/env python
# Author   guojy8993@163.com
# Date     2017/02/25
# Desc     Usage display of Binary-Tree-Traversal

'''
Binary Tree Traversal
http://blog.csdn.net/gfj0814/article/details/51637696
'''

class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self):
        pass

    def preOrder(self, node):
        if not node:
            return
        print node.data
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print node.data
        self.inOrder(node.right)

    def postOrder(self, node):
        if not node:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print node.data

if __name__ == "__main__":
    g = """
                               (1)
                   -------------+------------
                  +                          +
                 (2)                        (3)
         ---------+-----------      ---------+-----------
        +                    +     +                     +
       (4)                   (5)   (6)                   (7)
     --------
     +(8) +(9)
    """
    print g

    node05 = Node(data=5)
    node06 = Node(data=6)
    node07 = Node(data=7)
    node03 = Node(data=3, left=node06, right=node07)
    node09 = Node(data=9)
    node08 = Node(data=8)
    node04 = Node(data=4, left=node08, right=node09)
    node02 = Node(data=2, left=node04, right=node05)
    node01 = Node(data=1, left=node02, right=node03)
    
    tree = BTree()
    print "PreOrder traversal:"
    tree.preOrder(node01) 
    print "InOrder traversal:"
    tree.inOrder(node01)
    print "PostOrder traversal:"
    tree.postOrder(node01)
    
