from typing import TypeVar

V = TypeVar(str, int, float,object)


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):
    # Initializes the hashmap, if there is a dictionary, through the dictionary
    def __init__(self, dict=None):
        self.keyset = []
        self.data = [Node() for _ in range(13)]
        self.size = 13
        # Initialization by dict
        if dict is not None:
            from_dict(self, dict)


# Convert list to hash map
def from_dict(hash, dict):
    for k, v in dict.items():
        put(hash, k, v)


# Convert this map to the dict {}
def to_dict(hash) -> {}:
    kvList = {}
    if hash is None:
        return kvList
    else:
        i = 0
        while i < hash.size:
            if hash.data[i].value == None:
                i += 1
                continue
            else:
                p = hash.data[i]
                while p != None:
                    kvList[p.key] = p.value
                    p = p.next
                i += 1
    return kvList


# 1. add a new element
def put(hash, key: int, value: V) -> HashMap:
    """
       Insert key-value pairs into hash map

       :param hash: HashMap
       :param key: The key value to insert into the hash map
       :param value: The content corresponding to the key value of the hash map to be inserted
       :return: Hash map obtained after inserting key-value pairs
       """
    if hash == None:
        hash = HashMap()
    hash_key = key % hash.size
    if hash.data[hash_key].key == None:
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

def put_list(hash,list):
    if hash == None:
        hash = HashMap()
    for key,value in enumerate(list):
        hash_key = key % hash.size
        if hash.data[hash_key].key == None:
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
def del_(hash, key) -> HashMap:
    """
    delete the map node in map where the key = key
    :param key: map value
    :return:  hashmap
    """
    if hash == None:
        return None;
    hash_key = key % hash.size
    if hash.data[hash_key].value == None:
        raise Exception('No valid key value was found')
    else:
        p = hash.data[hash_key]
        if key == p.key:
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
    raise Exception('No valid key value was found')


def remove_keyset(hashmap, key):
    for i, k in enumerate(hashmap.keyset):
        if key == k:
            arr = hashmap.keyset
            del arr[i]
            return hashmap


# 3. size
def getSize(hash) -> int:
    """
     Gets the number of values of the hashmap
    :param hash: hashmap
    :return:  the number of values of the hashmap
    """
    sum = 0
    i = 0
    while i < hash.size:
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
    if hash is None:
        return list
    for i, key in enumerate(hash.keyset):
        list.append(get(hash, key))
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
        while i < hash.size:
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
def map(hash, f) -> HashMap:
    """
     map structure by speciﬁc function
    :param f: the function to map
    :return hashmap
    """
    table = cons(hash)
    for key in hash.keyset:
        value = get(hash, key)
        value = f(value)
        put(table, key, value)
    return table


def cons(map) -> HashMap:
    """
    Copy a hash map
    :param map: HashMap
    :return: The copied hash map
    """
    table = HashMap()
    from_dict(table, to_dict(map))
    return table


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
    for key in hash.keyset:
        value = get(hash, key)
        state = f(state, value)
    return state


# 9. mempty and mconcat
def mempty(hash):
    """
    clear the hashmap
    :param hash:hashmap
    """
    return None

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def mconcat(a, b):
    """
   concat two maps to one
   :param a:  hashmap
   :param b:  hashmap
   :return: new hashmap
   """
    if a is None:
        return b
    if b is None:
        return a
    for key in b.keyset:
        value=get(b,key)
        put(a,key,value)
    return a


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
