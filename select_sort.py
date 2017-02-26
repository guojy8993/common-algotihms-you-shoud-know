#!/usr/bin/env python
# coding:utf-8

'''
Ref: http://www.cnblogs.com/ucos/p/5871354.html
'''

def select_sort(coll):
    for i in range(0, len(coll)-1):
        index = i
        print coll
        for j in range(i+1, len(coll)):
            if coll[index] > coll[j]:
                index = j
        coll[i], coll[index] = coll[index], coll[i]


if __name__ == "__main__":
    L = [1, 7, 3, 8, 2, 4, 5]
    print "Pre-Sort:  %s" % L
    print "Sorting ..."
    select_sort(L)
    print "Sorting Done !"
    print "Post-Sort: %s" % L
