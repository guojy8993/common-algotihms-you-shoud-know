#!/usr/bin/env python
# Author   guojy8993@163.com
# Date     2017/02/25
# Desc     Usage display of Binary-Search-Algorithm

'''
Binary Search Algorithm
Ref: http://www.cnblogs.com/yupeng/p/3418293.html
'''

def binary_search(collection, target):
    print "search %d in %s " % (target, collection)
    if len(collection) > 0:
        low = 0
        high = len(collection) - 1
        while low <= high:
            print "==== new loop ===="
            print "high:", high
            print "low:", low
            half = (low + high) / 2
            print "half:", half
            if collection[half] == target:
                return half
            elif collection[half] > target:
                high = half - 1
            else:
                low = half + 1
         
        return -1
        
    return -1

if __name__ == "__main__":
    ordered_elements = [0, 1, 2, 3, 4, 5, 6, 7,8]
    print binary_search(ordered_elements, 5)    
    print binary_search(ordered_elements, 1)    
    print binary_search(ordered_elements, 6)    
    print binary_search(ordered_elements, 4)    
    print binary_search(ordered_elements, 100)    

