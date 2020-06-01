from typing import TypeVar

V = TypeVar(str, int, float)


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):
#Initializes the hashmap, if there is a dictionary, through the dictionary
    def __init__(self,dict=None):
        self.keyset = []
        self.data = [Node() for _ in range(13)]
        self.size = 13
        #Initialization by dict
        if dict is not None:
            from_dict(self,dict)



#Convert list to hash map
def from_dict(hash,dict):
        for k,v in dict.items():
            put(hash,k,v)

#Convert this map to the dict {}
def to_dict(hash) -> {}:
   kvList={}
   if hash is None:
       return kvList
   else:
       i = 0
       while i < 13:
           if hash.data[i].value == None:
               i += 1
               continue
           else:
               p = hash.data[i]
               while p != None:
                   kvList[p.key]=p.value
                   p = p.next
               i += 1
   return kvList

# 1. add a new element
def put(hash, key:int, value:V) ->HashMap:
    """
       Insert key-value pairs into hash map

       :param hash: HashMap
       :param key: The key value to insert into the hash map
       :param value: The content corresponding to the key value of the hash map to be inserted
       :return: Hash map obtained after inserting key-value pairs
       """
    hash_key = key % 13
    if hash.data[hash_key].value == None:
        hash.data[hash_key].value = value
        hash.data[hash_key].key = key
        hash.keyset.append(key)
    else:
        temp = Node(key, value)
        hash.keyset.append(key)
        p = hash.data[hash_key]
        while p.next != None:
            p = p.next
        p.next = temp

    return hash

# 2. remove an element
def del_(hash, key) ->HashMap:
    """
    delete the map node in map where the key = key
    :param key: map value
    :return:  hashmap
    """
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
            arr=hashmap.keyset
            del arr[i]
            return hashmap

# 3. size
def getSize(hash) ->int:
    """
     Gets the number of values of the hashmap
    :param hash: hashmap
    :return:  the number of values of the hashmap
    """
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
    """
    make this map to a list. just use the values in the map
    :return: []
    """
    list = []
    for i in hash.keyset:
        list.append(get(hash, i))
    return list


def from_list(hash, list):
    """
   add the map value from list make the i,v(enumerate) to the k and v
   :param list: list like [1,2,31,5]
   """
    for k, v in enumerate(list):
        put(hash, k, v)


def get(hash, key: int) -> V:
    """
   Get value by key
   :param hash: hashmap
   :param key:the key of map
   :return the value of hashmap
   """
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
def find_iseven(hash) -> HashMap:
    """
   ﬁnd element by speciﬁc predicate
   :param hash: hashmap
   :return the speciﬁc hashmap
   """
    mylist = to_list(hash)
    mylist1 = []
    for k in range(len(mylist)):
        if mylist[k] % 2 == 0:
            mylist1.append(mylist[k])
    return mylist1


# 6. ﬁlter data structure by speciﬁc predicate
def filter_iseven(hash):
    """
   ﬁlter data structure by speciﬁc predicate
   :param hash: hashmap
   :return the speciﬁc hashmap
   """
    mylist = to_list(hash)
    mylist1 = []
    for k in range(len(mylist)):
        if mylist[k] % 2 != 0:
            mylist1.append(mylist[k])
    return mylist1


# 7. map structure by speciﬁc function
def a_map(hash, f) -> list:
    """
     map structure by speciﬁc function
    :param f: the function to map
    :return list
    """
    i = 0
    list = to_list(hash)
    for v in list:
        list[i] = f(v)
        i += 1
    return list


# 8. reduce:process structure elements to build a return value by speciﬁc functions
def reduce(hash, f, initial_state):
    """
    reduce:process structure elements to build a return value by speciﬁc functions
    :param hash:hashmap
    :param f: the function to map
    :param: original state
    :return final state
    """
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
    """
    clear the hashmap
    :param hash:hashmap
    """
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
    """
   concat two maps to one
   :param a:  hashmap
   :param b:  hashmap
   :return: new hashmap
   """
    hash = HashMap()
    if a is None:
        if b is None:
            return None
        else:
            for k,v in enumerate(to_list(b)):
                put(hash,k,v)
            return hash
    else:
        if b is None:
            for k, v in enumerate(to_list(a)):
                put(hash, k, v)
            return hash
        else:
            list_a = to_list(a)
            list_b = to_list(b)
            list_a.extend(list_b)
            list_a.sort()
            for k, v in enumerate(list_a):
                put(hash, k, v)
            return hash


# 10. iterator
def iterator(hash):
    """
    iterator
    :param hash:  hashmap
    :return: The next value in the hashmap
    """
    if hash is not None:
        res = []
        list = to_list(hash)
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


def __eq__(a, b):
    return a.__dict__ == b.__dict__
