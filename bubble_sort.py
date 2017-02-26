#!/usr/bin/env python
# coding:utf-8

'''
Ref: http://www.cnblogs.com/qlshine/p/6017957.html
'''

def bubble_sort(coll):
    for i in range(len(coll) - 1):
        for j in range(len(coll) - i -1):
            if coll[j] > coll[j+1]:
                coll[j], coll[j+1] = coll[j+1], coll[j]
    return coll

if __name__ == "__main__":
    L = [1, 7, 3, 8, 2, 4, 5]
    print "Pre-Sort:  %s" % L
    bubble_sort(L)
    print "Post-Sort: %s" % L
