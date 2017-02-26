#!/usr/bin/env python
# Author   guojy8993@163.com
# Date     2017/02/25
# Desc     Element insert/remove of Liner-List

'''
Ref: http://blog.csdn.net/w2211384272/article/details/47152917
'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkList(object):
    def __init__(self, head):
        self.head = head
        self.tail = head

    def getLength(self):
        if self.head:
           len = 1
           next = self.head.next
           while next:
               len = len + 1
               next = next.next
           return len
               
        else:
           return 0

    def is_empty(self):
        return self.getLength() == 0


    def clear(self):
        if self.head:
            self.head = None

    def append(self, item):
        if self.is_empty():
            self.head = item
            self.tail = item
        else:
            seld.tail.next = item

    def getitem(self, index):
        if self.head:
            i = 0
            if index == i:
                return self.head
            next = self.head.next
            while next:
                i = i + 1
                if i == index:
                    return next
                next = next.next
        return None

    def reverse(self):
        pre = None 
        current = self.head
        if not current:
            return True
        post = self.head.next
        if not post:
            return True
        
        current.next = pre
        while post:
            pre = current
            current = post
            post = post.next

            current.next = pre

            if not post:
                self.head = current
                return True    
        return True
            

            

    def index(self, index):
        if index not in range(0, self.getLength()):
            raise IndexError
        next = self.head.next
        count = 0
        if count == index:
            return self.head.data
        while next:
            count = count + 1
            if count == index:
                return next.data
            next = next.next    

    def delete(self, index):
        if index == 0 and not self.is_empty():
            next = self.head.next
            self.head = next
            if not self.head.next:
                self.tail = next
            return True
        
        if index > 0 and index < sel.getLength():
            before = self.head
            next = self.head.next
            count = 0
            while next:
                count = count + 1
                if count == index:
                    before.next = next.next
                    return True
                before = next
                next = next.next
                
        return False

    def toString(self):
        result = ""
        if self.head:
            result = "%s %s" % (result, self.head.data)
            post = self.head.next
            while post:
                result = "%s %s" % (result, post.data)
                post = post.next
            print result
                

    def insert(self, index, item):
        if self.is_empty() and index == 0:
            self.head = item
            self.tail = item
            return True
        elif not self.is_empty() and index == 0:
            item.next = self.head
            self.head = item
            return True
        elif not self.is_empty() and index > 0 and index < self.getLength():
            next = self.head.next
            before = self.head
            count = 0
            while next:
                count = count + 1
                if index == count:
                    item.next = next
                    before.next = item
                    return True
                before = next
                next = next.next
                             
        return False
            

if __name__ == "__main__":

    L = LinkList(Node(data=123))
    print L.getLength()
    print L.is_empty()

    print "Add element: 100"
    print L.insert(0, Node(data=100))
    print L.getitem(1).data
    print L.getitem(0).data
    print L.getLength()
    print L.delete(0)
    print L.getitem(0).data
    print L.index(0)
    
    # print "Insert Element: 110"
    L.insert(0, Node(data=110))

    '''
    # print "Insert Element: 100"
    L.insert(0, Node(data=100))
    # print "Insert Element: 90"
    L.insert(0, Node(data=90))
    # print "Insert Element: 80"
    L.insert(0, Node(data=80))
    '''
    # print "Insert Element: -1"
    print L.insert(0, Node(data=-1))
 
    # print L.getitem(0).data 
    
    
    print "Pre-reverse:"
    L.toString()
    print L.reverse()
    print "Post-reverse:"
    L.toString()
    

     
    
