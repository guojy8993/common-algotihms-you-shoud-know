#!/usr/bin/env python
# coding:utf-8

'''
Ref: http://blog.csdn.net/littlethunder/article/details/23877545
'''



if __name__ == "__main__":
    L = [1, 7, 3, 8, 2, 4, 5]
    print "Pre-Sort:  %s" % L
    print "Sorting ..."
    L = merge_sort(L)
    print "Sorting Done !"
    print "Post-Sort: %s" % L
