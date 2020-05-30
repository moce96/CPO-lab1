from typing import TypeVar

V = TypeVar(str, int, float)

class Node:
    def __init__(self, key=None,value=None):
        self.key = key
        self.value=value
        self.next = None

class HashMap(object):

    def __init__(self):
        self.keyset = []
        self.data = [Node() for _ in range(13)]
        self.size = 13

    def get(self, key: int) -> V:
        hash_value = key % self.size
        while True:
            if self.keyset == None:
                return None
            i = 0
            while i < 13:
                if self.data[i].key == None:
                    i += 1
                    continue
                else:
                    p = self.data[i]
                    while p != None:
                        if p.key == key:
                            return p.value
                        p = p.next
                    i += 1

    def add(self, key, value):
        hash_value = key % self.size

        if self.data[hash_value].value == None:
            self.data[hash_value].value = value
            self.data[hash_value].key = key
            self.keyset.append(key)
        else:
            temp = Node(key, value)
            self.keyset.append(key)
            p = self.data[hash_value]
            while p.next != None:
                p = p.next
            p.next = temp


    # 1. add a new element
def add(self, key, value):
    hash_value = key % self.size

    if self.data[hash_value].value == None:
        self.data[hash_value].value = value
        self.data[hash_value].key = key
        self.keyset.append(key)
    else:
        temp = Node(key, value)
        self.keyset.append(key)
        p = self.data[hash_value]
        while p.next != None:
            p = p.next
        p.next = temp

    # 2. remove an element
def remove(self,key):
    i = 0
    while i < self.size:
        if self.data[i].key==None:
            i+=1
            continue
        else:
            p = self.data[i]
            if p.key==key:
                if p.next==None:
                    p.key=None
                    p.value=None
                else:
                    temp=p.next
                    p.key=temp.key
                    p.value=temp.value
                    p.next=temp.next
                remove_keyset(self,key)
                return self
            else:
                while p != None:
                    if p.key == key:
                        temp = p.next
                        p.next=temp.next
                        remove_keyset(self, key)
                        return self
                    else:
                        p = p.next
        i += 1
    return self



def remove_keyset(hashmap,key):
    for i,k in enumerate(hashmap.keyset):
        if key==k:
            hashmap.keyset.remove(i)
            break

    # 3. size
def getSize(self):
        sum=0

        i = 0
        while i < 13:
            if self.data[i].value == None:
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
    list = []
    for i in self.keyset:
        list.append(self.get(i))
    return list


def from_list(self, list):
    for k, v in enumerate(list):
        self.add(k, v)
    return self


def get(self, key: int) -> V:
    hash_value = key % self.size
    while True:
        if self.keyset == None:
            return None
        i = 0
        while i < 13:
            if self.data[i].key == None:
                i += 1
                continue
            else:
                p = self.data[i]
                while p != None:
                    if p.key == key:
                        return p.value
                    p = p.next
                i += 1

# 5. ﬁnd element by speciﬁc predicate
def find_iseven(self):
    mylist = to_list(self)
    mylist1=[]
    for k in range(len(mylist)):
        if mylist[k] % 2 == 0:
            mylist1.append(mylist[k])
    return mylist1


# 6. ﬁlter data structure by speciﬁc predicate
def filter_iseven(self):
    mylist = to_list(self)
    mylist1 = []
    for k in range(len(mylist)):
        if mylist[k] % 2 != 0:
            mylist1.append(mylist[k])
    return mylist1

# 7. map structure by speciﬁc function
def a_map(self, f):
    i = 0
    list=to_list(self)
    for v in list:
        list[i] = f(v)
        i += 1
    return list

# 8. reduce:process structure elements to build a return value by speciﬁc functions
def reduce(self, f, initial_state):
    state = initial_state
    i = 0
    while i < 13:
        if self.data[i].value == None:
            i += 1
            continue
        else:
            p = self.data[i]
            state = f(state, p.value)
            while p.next != None:
                p = p.next
                state = f(state, p.value)
        i += 1
    return state

# 9. mempty and mconcat
def mempty(self):
    i = 0
    while i < 13:
        if self.data[i].value == None:
            i += 1
            continue
        else:
            p = self.data[i]
            p.key = None
            p.value = None
            p.next = None
        i += 1
    self.keyset = []
    return self


def mconcat(a, b):
    if a is None:
        return b
    else:
        if b is None:
            return a
        else:
            list = to_list(b)
            for i,v in enumerate(list):
                add(a,i,v)


# 10. iterator
def iterator(n):
    if n is not None:
        res=[]
        list=to_list(n)
        for i in list:
            res.append(i)
        a=iter(res)
    else:
        a=None

    def get_next():
        if a is None:
            return False
        else:
            return next(a)
    return get_next



