#!/usr/bin/env python
# coding:utf-8

'''
Ref: http://blog.csdn.net/littlethunder/article/details/9472301
'''

def merge(left, right):
    result = []
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i+1
        else: 
            result.append(right[j])
            j = j+1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(seq):
    if len(seq) <=1:
        return seq
    mid = len(seq)/2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)

if __name__ == "__main__":
    L = [1, 7, 3, 8, 2, 4, 5]
    print "Pre-Sort:  %s" % L
    print "Sorting ..."
    L = merge_sort(L)
    print "Sorting Done !"
    print "Post-Sort: %s" % L
