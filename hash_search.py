#!/usr/bin/env python
# Author   guojy8993@163.com
# Date     2017/02/25
# Desc     Usage display of Hash-Search-Algorithm

'''
Hash Search Algorithm
Ref: http://blog.csdn.net/xiaoping8411/article/details/7706376
Ref: http://blog.csdn.net/sinat_33363493/article/details/52693668
Ref: http://blog.csdn.net/a359680405/article/details/51152084
'''

def simple_hash(data,hash_len):
    return data % hash_len

def hash_search(hash, hash_len, data):
    hash_addr = simple_hash(data, hash_len)
    while hash.get(hash_addr) and hash.get(hash_addr) != data:
        hash_addr = hash_addr + 1
        hash_addr = hash_addr % hash_len
    if hash.get(hash_addr) == None:
        return None
    return hash_addr

def hash_insert(hash, hash_len, data):
    hash_addr = simple_hash(data, hash_len)
    while hash.get(hash_addr) and hash.get(hash_addr) != data:
        hash_addr = hash_addr + 1
        hash_addr = hash_addr % hash_len
    hash[hash_addr] = data


if __name__ == "__main__":
    hash_len = 20
    L = [23, 45, 76, 12, 47, 89, 100]
    hash = {}
    for item in L:
        hash_insert(hash, hash_len, item)
    print hash

    key = hash_search(hash, hash_len, 47)
    if key:
        print "Key: %s Value: %s" % (key, hash[key])
    else:
        print "Not Found !"

    
    key = hash_search(hash, hash_len, 48)
    print key
