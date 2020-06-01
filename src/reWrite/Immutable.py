from typing import TypeVar

V = TypeVar(str, int, float)


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):

    def __init__(self):
        self.keyset = []
        self.data = [Node() for _ in range(13)]
        self.size = 13


# 1. add a new element
def add(hash, key, value):
    hash_value = key % hash.size

    if hash.data[hash_value].value == None:
        hash.data[hash_value].value = value
        hash.data[hash_value].key = key
        hash.keyset.append(key)
    else:
        temp = Node(key, value)
        hash.keyset.append(key)
        p = hash.data[hash_value]
        while p.next != None:
            p = p.next
        p.next = temp

    return hash

    # 2. remove an element


def remove(hash, key):
    i = 0
    while i < hash.size:
        if hash.data[i].key == None:
            i += 1
            continue
        else:
            p = hash.data[i]
            if p.key == key:
                if p.next == None:
                    p.key = None
                    p.value = None
                else:
                    temp = p.next
                    p.key = temp.key
                    p.value = temp.value
                    p.next = temp.next
                remove_keyset(hash, key)
                return hash
            else:
                while p != None:
                    if p.key == key:
                        temp = p.next
                        p.next = temp.next
                        remove_keyset(hash, key)
                        return hash
                    else:
                        p = p.next
        i += 1
    return hash


def remove_keyset(hashmap, key):
    for i, k in enumerate(hashmap.keyset):
        if key == k:
            hashmap.keyset.remove(i)
            return hashmap

    # 3. size


def getSize(hash):
    sum = 0

    i = 0
    while i < 13:
        if hash.data[i].value == None:
            i += 1
            continue
        else:
            p = hash.data[i]
            while p != None:
                sum += 1
                p = p.next
            i += 1

    return sum


# 4. conversion from and to python lists
def to_list(hash):
    list = []
    for i in hash.keyset:
        list.append(get(hash, i))
    return list


def from_list(hash, list):
    for k, v in enumerate(list):
        add(hash, k, v)


def get(hash, key: int) -> V:
    hash_value = key % hash.size
    while True:
        if hash.keyset == None:
            return None
        i = 0
        while i < 13:
            if hash.data[i].key == None:
                i += 1
                continue
            else:
                p = hash.data[i]
                while p != None:
                    if p.key == key:
                        return p.value
                    p = p.next
                i += 1
    return None


# 5. ﬁnd element by speciﬁc predicate
def find_iseven(hash):
    mylist = to_list(hash)
    mylist1 = []
    for k in range(len(mylist)):
        if mylist[k] % 2 == 0:
            mylist1.append(mylist[k])
    return mylist1


# 6. ﬁlter data structure by speciﬁc predicate
def filter_iseven(hash):
    mylist = to_list(hash)
    mylist1 = []
    for k in range(len(mylist)):
        if mylist[k] % 2 != 0:
            mylist1.append(mylist[k])
    return mylist1


# 7. map structure by speciﬁc function
def a_map(hash, f):
    i = 0
    list = to_list(hash)
    for v in list:
        list[i] = f(v)
        i += 1
    return list


# 8. reduce:process structure elements to build a return value by speciﬁc functions
def reduce(hash, f, initial_state):
    state = initial_state
    i = 0
    while i < 13:
        if hash.data[i].value == None:
            i += 1
            continue
        else:
            p = hash.data[i]
            state = f(state, p.value)
            while p.next != None:
                p = p.next
                state = f(state, p.value)
        i += 1
    return state


# 9. mempty and mconcat
def mempty(hash):
    i = 0
    while i < 13:
        if hash.data[i].value == None:
            i += 1
            continue
        else:
            p = hash.data[i]
            p.key = None
            p.value = None
            p.next = None
        i += 1
    hash.keyset = []
    return hash



def mconcat(a, b):
    hash = HashMap()
    if a is None:
        if b is None:
            return None
        else:
            for k,v in enumerate(to_list(b)):
                add(hash,k,v)
            return hash
    else:
        if b is None:
            for k, v in enumerate(to_list(a)):
                add(hash, k, v)
            return hash
        else:
            list_a = to_list(a)
            list_b = to_list(b)
            list_a.extend(list_b)
            list_a.sort()
            for k, v in enumerate(list_a):
                add(hash, k, v)
            return hash


# 10. iterator
def iterator(n):
    if n is not None:
        res = []
        list = to_list(n)
        for i in list:
            res.append(i)
        a = iter(res)
    else:
        a = None

    def get_next():
        if a is None:
            return False
        else:
            return next(a)

    return get_next
