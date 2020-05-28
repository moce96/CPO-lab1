from typing import Generator


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class HashMap(object):

    def __init__(self):

        self.data=[Node() for _ in range(13)]
        self.size = 13

    # 1. add a new element
    def add(self,key):
        hash_value=key % self.size

        if self.data[hash_value].data ==None:
            self.data[hash_value].data=key
        else:

            temp=Node(key)
            p=self.data[hash_value]
            while p.next != None:
                p=p.next
            p.next=temp

    # 2. remove an element
    def remove(self,element):
        hash_value=element%13
        if self.data[hash_value].data == element:
            self.data[hash_value].data = None
        else:
            p=self.data[hash_value]
            pre = None
            while p.next!=None:
                if p != None and p.data!=element:
                    pre = p
                    p = p.next
                if p == None:
                    return 'Delete Error'
                else:
                    pre.next = p.next

    # 3. size
    def getSize(self):
        sum=0

        i = 0
        while i < 13:
            if self.data[i].data == None:
                i += 1
                continue
            else:
                p = self.data[i]
                while p != None:
                    sum+=1
                    p = p.next
                i += 1

        return sum

    # 4. conversion from and to python lists
    def to_list(self):
        list=[]
        i=0
        while i<13:
            if self.data[i].data == None:
                i += 1
                continue
            else:
                p=self.data[i]
                while p !=None:
                    list.append(p.data)
                    p=p.next

                i += 1

        return list

    def from_list(self,list):
        for i in list:
            self.add(i)
        return self

    # 5. ﬁnd element by speciﬁc predicate
    def find_iseven(self):
        mylist = self.to_list()
        mylist1=[]
        for k in range(len(mylist)):
            if mylist[k] % 2 == 0:
                mylist1.append(mylist[k])
        return mylist1


    # 6. ﬁlter data structure by speciﬁc predicate
    def filter_iseven(self):
        mylist = self.to_list()
        mylist1 = []
        for k in range(len(mylist)):
            if mylist[k] % 2 != 0:
                mylist1.append(mylist[k])
        return mylist1

    # 7. map structure by speciﬁc function
    def a_map(self, f):
        i = 0
        list=self.to_list()
        for v in list:
            list[i] = f(v)
            i += 1
        return list

    # 8. reduce:process structure elements to build a return value by speciﬁc functions
    def reduce(self, f, initial_state):
        state = initial_state
        i = 0
        while i < 13:
            if self.data[i].data == None:
                i += 1
                continue
            else:
                p = self.data[i]
                state = f(state, p.data)
                while p.next != None:
                    p = p.next
                    state = f(state, p.data)
            i += 1
        return state

    # 9. mempty and mconcat
    def mempty(self):
        i = 0
        while i < 13:
            if self.data[i].data == None:
                i += 1
                continue
            else:
                p = self.data[i]
                p.data = None
                p.next = None
            i += 1
        return self

    def mconcat(self, b):
        if self is None:
            return b

        if b is not None:
            list=b.to_list()
            for i in list:
                self.add(i)



    # 10. iterator
    def __iter__(self):
        return self

    def __next__(self):
        start = 0
        end = self.getSize()
        if start == end:
            raise StopIteration
        tmp = self.to_list[start]
        start += 1
        return tmp
