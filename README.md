# Different approach for algorithms and data structure implementation

 - ## **list of group members:**
 
192050214  Mu Yuankai
  192050208 Jia Yuebin
 
 - ## **variant description:**
 
Hash-map (collision resolution: separate chaining, for array and bucket you can use built-in list) based set.
 
 - ## **synopsis:**
 
Build a hash map, use chain addresses to solve address conflicts, write two versions of mutable and immutable, respectively: add, delete, size, transform list, find, filter, map, reduce, concate, iterator.
 
 - ## **contribution summary for each group member**
 
Mu Yuanai complete the hash_mutable module  
 Jia Yuebin complete the hash_immutable module
 
 - ## **explanation of taken design decisions and analysis;**
 
Firstly, the implementation method of hash table in data structure is introduced.
Secondly, the teacher gives a reference to the realization of single linked list structure.
Third, dig into the hashmap structure and design the structure accordingly
 Finally, divide the work into two parts and finish them separately.
 
 - ## **work demonstration**
 
In the hash_mutabable module, I defined a class HashMap and used chained addresses to resolve address conflicts.It is a data structure that USES stored data to define functions.In HashMap_mutable, I tested this function.
 In hashMap_immutable, the chain address method is used to resolve address conflicts.The generated hash table is stored in a two-dimensional array. The functions are: add, delete, size, transform list, find, filter, map, reduce, concate, iterator.In the end, he passed the exam successfully.
 
 - ## **conclusion.**

  Hash mapping is to calculate the mapped address according to the incoming key, and each key has a different mapped address. For the mapped address, the value stored therein is immutable, but for the hash table, the value should be mutable. This experiment implements hash mapping by writing two different versions of mutable and immutable, and solves the object's mutable and immutable by different methods and tests it. In the experiment, list is used as the hash mapping table. In the mutable and immutable versions, re-hashing and linear detection in the open address method are used to solve the address conflict problem. In the mutable version, we can directly operate on the original data. On the contrary, we cannot directly operate on the data in the immutable version. It is necessary to indirectly operate by introducing intermediate variables or local variables.  
```

```



## Partial code introduction

#### 1. Initialize hash map

```python
def __init__(self, dict=None):
    self.key_set = []  # used to store the elements key added to the hash map
    self.data = [self.empty for _ in range(13)]  # Used to store element nodes
    self.size = 13  # table size
    # Initialization by dict
    if dict is not None:
        self.from_dict(self, dict)

    self.len = 0
    self.index = 0
```

#### 2. get hash value by key

```python
def add(self, key, value):
    """
       Insert key-value pairs into hash map
       :param key: The key to insert into the hash map
       :param value: element value
    """
    hash_value = self.get_hash(key)
    kv_entry = Node(key, value)

    if self.data[hash_value] == self.empty:
        self.data[hash_value] = kv_entry
        self.key_set.append(key)
        self.len = self.len + 1
    else:
        p = self.data[hash_value]
        while p.next != None:
            if p.key is key:
                p.value = value
                return
            p = p.next
        if p.key is key:
            p.value = value
            return
        p.next = kv_entry
        self.key_set.append(key)
        self.len = self.len + 1
```

Test function add

```python
def test_add(self):
    hash = HashMap()
    hash.add(2, 6)
    self.assertEqual(hash.get(2), 6)
    self.assertEqual(hash.to_dict(), {2: 6})
    hash.add(4, 5)  # add  value 5;
    self.assertEqual(hash.get(4), 5)
    hash.add(1, 5)  # add another 5 with different key
    self.assertEqual(hash.get(1), 5)
```

#### 3. Remove element in hash map by key 

```python
def remove(self, key):
    '''
    Delete element in hash map by key
    :param key:element key
    :return:eoolean type for delete success or failure
    '''
    hash_value = self.get_hash(key)
    if self.data[hash_value] is self.empty:
        return False
    elif self.data[hash_value].key is key:
        self.data[hash_value] = self.data[hash_value].next
        self.remove_key_set(key)
        return True
    p = self.data[hash_value]
    q = self.data[hash_value].next
    while q.next is not None:
        if q.key is key:
            p.next = q.next
            self.remove_key_set(key)
            return True
        p = q
        q = q.next
    if q.key is key:
        p.next = None
        self.remove_key_set(key)
        return True
    return False
```

Test remove function

```python
def test_remove(self):
    hash = HashMap()
    dict1 = {1: 1, 3: 3, 5: 7}
    hash.from_dict(dict1)
    hash.remove(1)
    dict2 = {3: 3, 5: 7}
    self.assertEqual(hash.to_dict(), dict2)
```

#### 4. get value by key in hash map

```python
def get(self, key):
    '''
    Find element in hash map by key.
    :param key:element key
    :return:element value response to the input key
    '''
    dict = self.to_dict()
    value = dict[key]
    return value
```

Test get function

```python
def test_get(self):
    hash = HashMap()
    hash.add(1, 2)
    hash.add(2, 3)
    hash.add(4, 5)
    hash.add(5, 5)
    self.assertEqual(hash.get(4), 5)
    self.assertEqual(hash.get(2), 3)
    self.assertEqual(hash.get(1), 2)
    self.assertEqual(hash.get(5), 5)
```

#### 5. add key-value pairs from dict

```python
def from_dict(self, dict):
    '''
    add elements from dict type
    :param dict:input dict
    :return:
    '''
    for k, v in dict.items():
        self.add(k, v)
```

Test from dict function

```python
def test_to_dict(self):
    hash = HashMap()
    hash.add(1, 2)
    hash.add(2, 3)
    hash.add(3, 2)
    hash.add(5, 1)
    hash.to_dict()
    self.assertEqual(hash.to_dict(), {1: 2, 3: 2, 5: 1, 2: 3})
```

#### 6. transfer hash map to dict

```python
def to_dict(self):
    '''
    transfer hash map into dict
    :return: resule dict
    '''
    kvDict = {}
    if self.len is 0:
        return kvDict
    else:
        i = 0
        while i < self.size:
            if self.data[i] is self.empty:
                i += 1
                continue
            else:
                p = self.data[i]
                while p != None:
                    kvDict[p.key] = p.value
                    p = p.next
                i += 1
    return kvDict
```

Test for to dict function

```python
def test_to_dict(self):
    hash = HashMap()
    hash.add(1, 2)
    hash.add(2, 3)
    hash.add(3, 2)
    hash.add(5, 1)
    hash.to_dict()
    self.assertEqual(hash.to_dict(), {1: 2, 3: 2, 5: 1, 2: 3})
```

#### 7. get element number in hash map

```python
def get_size(self):
    '''
    Element number in hash map.
    :return:number of element in hash map
    '''
    size = len(self.key_set)
    return size
```

Test for get size function

```python
def test_get_size(self):
    hash = HashMap()
    self.assertEqual(hash.get_size(), 0)
    hash.add(1, 2)
    self.assertEqual(hash.get_size(), 1)
    hash.add(14, 2)
    self.assertEqual(hash.get_size(), 2)
    hash.add(1, 3)
    self.assertEqual(hash.get_size(), 2)  # same key ,new value alter the old one
    
@given(st.lists(st.integers()))
def test_python_len_and_list_size_equality(self, a):
    hash = HashMap()
    hash.from_list(a)
    self.assertEqual(hash.get_size(), len(a))
```

#### 8. add key-value pairs from list

```python
def from_list(self, list):
    '''
    add element from list type
    :param list:input list
    '''
    for k, v in enumerate(list):
        self.add(k, v)
```

Test for from list function

```python
def test_from_list(self):
    test_data = [
        [],
        ['a'],
        ['0', '11'],
        [1, 2, 3],
        [None]
    ]
    for e in test_data:
        hash = HashMap()
        hash.from_list(e)
        self.assertEqual(hash.to_list(), e)

@given(st.lists(st.integers()))
def test_from_list(self, a):
    hash = HashMap()
    hash.from_list(a)
    self.assertEqual(hash.to_list(), a)
```

#### 9. transfer hash map to list

```python
def to_list(self):
    '''
    Transfer hash map into list type
    :return:result list
    '''
    list = []
    for key in self.key_set:
        list.append(self.get(key))
    return list
```

Test to list function

```python
def test_to_list(self):
    hash = HashMap()
    dict = {4: 2, 3: 2, 5: 1, 1: 3}
    hash.from_dict(dict)
    self.assertEqual(hash.to_list(), [2, 2, 1, 3])
    
@given(st.lists(st.integers()))
def test_from_list_to_list_equality(self, a):
    hash = HashMap()
    hash.from_list(a)
    b = hash.to_list()
    self.assertEqual(a, b)
```

#### 10. find element by specific predicate(is even)

```python
def find_iseven(self):
    '''
    Find element with even value in hash map.
    :return:list with even number value
    '''
    list = self.to_list()
    my_list = []
    for value in list:
        if type(value) is int or type(value) is float:
            if value % 2 == 0:
                my_list.append(value)
    return my_list
```

Test for it

```python
def test_find_iseven(self):
    hash = HashMap()
    hash.from_list([1, 2, 3, 4, 5, 6.0, 7.0, None, 'ss', 'dasd'])
    self.assertEqual(hash.to_list(), [1, 2, 3, 4, 5, 6.0, 7.0, None, 'ss', 'dasd'])
    self.assertEqual(hash.find_iseven(), [2, 4, 6.0])
```

#### 11. filter data structure by specific predicate (is even)

```python
def filter_iseven(self):
    '''
    Filter element with even value in hash map.
    :return: list with not even number value
    '''
    list = self.to_list()
    for value in list:
        if type(value) is int or type(value) is float:
            if value % 2 == 0:
                list.remove(value)
    return list
```

```python
def test_filter_iseven(self):
    hash = HashMap()
    hash.from_list([1, 2, 3, 4, 5, 6.0, 7.0, None, 'ss', 'dasd'])
    self.assertEqual(hash.to_list(), [1, 2, 3, 4, 5, 6.0, 7.0, None, 'ss', 'dasd'])
    self.assertEqual(hash.filter_iseven(), [1, 3, 5, 7.0, None, 'ss', 'dasd'])
```

#### 12. map structure by specific function

```python
def map(self, f):
    '''
    Map element value in hash map with f
    :param f:
    :return:dict store all key-value pairs after map
    '''
    dict = {}
    for key in self.key_set:
        value = f(self.get(key))
        dict[key] = value
    return dict
```

Test for this function

```python
def test_map(self):
    dict1 = {3: 23, 4: 323}
    dict2 = {3: '23', 4: '323'}
    hash = HashMap()
    hash.from_dict(dict1)
    self.assertEqual(hash.map(str), dict2)
```

#### 13. reduce – process structure elements to build a return value by specific functions

```python
def reduce(self, f, initial_state):
    """
    Reduce the mapSet to one value.
    :param f: the reduce method
    :param initial_state:result initial_state
    :return:final res
    """
    state = initial_state
    for key in self.key_set:
        value = self.get(key)
        state = f(state, value)
    return state
```

Test for this function

```python
def test_reduce(self):
    hash = HashMap()
    self.assertEqual(hash.reduce(lambda st, e: st + e, 0), 0)
    dict1 = {3: 23, 4: 323}
    hash1 = HashMap()
    hash1.from_dict(dict1)
    self.assertEqual(hash1.reduce(lambda st, e: st + e, 0), 346)
```

#### 14. monoid

```python
def mempty(self):
    """
    The empty element in property monoid, usually called mempty.
    """
    # return HashMap()
    return None

def mconcat(self, a, b):
    """
    Operation in property monoid.
    :param a:first input hash map
    :param b:second input hash map
    :return: add element in b into a,return a
    """
    if a is None:
        return b
    if b is None:
        return a
    for key in b.key_set:
        value = b.get(key)
        a.add(key, value)
    return a
```

Test for this function

```python
@given(a=st.lists(st.integers()))
def test_monoid_identity(self, a):
    hash = HashMap()
    hash_a = HashMap()
    hash_a.from_list(a)
    self.assertEqual(hash.mconcat(hash.mempty(), hash_a), hash_a)
    self.assertEqual(hash.mconcat(hash_a, hash.mempty()), hash_a)

@given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
def test_monoid_associativity(self, a, b, c):
    hash = HashMap()
    hash_a = HashMap()
    hash_b = HashMap()
    hash_c = HashMap()
    # add list to HashMap
    hash_a.from_list(a)
    hash_b.from_list(b)
    hash_c.from_list(c)
    # (a·b)·c
    a_b = hash.mconcat(hash_a, hash_b)
    ab_c = hash.mconcat(a_b, hash_c)
    # a·(b·c)
    b_c = hash.mconcat(hash_b, hash_c)
    a_bc = hash.mconcat(hash_a, b_c)
    self.assertEqual(ab_c, a_bc)
```

#### 15. iterator

```python
def __iter__(self):
    return iter(self.to_kv_entry_list())

def __next__(self):
    if self.index >= self.len:
        raise StopIteration("end")
    else:
        self.index += 1
        val = self.get(self.key_set[self.index - 1])
        return val
```

Test for this function

```python
def test_iter(self):
    dict1 = {1: 123, 2: 333, 3: 23, 4: 323}
    table = HashMap()
    table.from_dict(dict1)
    tmp = {}
    for e in table:
        tmp[e.key] = e.value
    self.assertEqual(table.to_dict(), tmp)
    i = iter(HashMap())
    self.assertRaises(StopIteration, lambda: next(i))
```