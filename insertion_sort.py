#!/usr/bin/env python
# coding:utf-8

'''
Ref: http://www.cnblogs.com/ucos/p/5885620.html
'''

def insertion_sort(coll):
    for i in range(1, len(coll)):
        if coll[i] < coll[i-1]:
            print coll
            tmp = coll[i]
            index = i
            while index > 0 and coll[index -1] > tmp:
                coll[index] = coll[index -1]
                index = index - 1
            coll[index] = tmp


if __name__ == "__main__":
    L = [1, 7, 3, 8, 2, 4, 5]
    print "Pre-Sort:  %s" % L
    insertion_sort(L)
    print "Post-Sort: %s" % L
