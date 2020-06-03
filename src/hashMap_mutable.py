class Node:
    def __init__(self, key=None, value=None, next=None):
        '''
        Used to initialize element nodes
        :param key:key of element node
        :param value:value of element node
        :param next:chain method to solve hash collision
        '''
        self.key = key
        self.value = value
        self.next = next


class HashMap(object):
    empty = object()

    def __init__(self, dict=None):
        self.key_set = []  # used to store the elements key added to the hash map
        self.data = [self.empty for _ in range(13)]  # Used to store element nodes
        self.size = 13  # table size
        # Initialization by dict
        if dict is not None:
            self.from_dict(self, dict)

        self.len = 0
        self.index = 0

    def get_hash(self, key):
        '''
        Hash by key
        :param key:element key
        :return:hash value
        '''
        hash_value = key % self.size
        return hash_value

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

    def get(self, key):
        '''
        Find element in hash map by key.
        :param key:element key
        :return:element value response to the input key
        '''
        dict = self.to_dict()
        value = dict[key]
        return value

    def remove_key_set(self, key):
        '''
        Delete key in key_set list
        :param key:key to delete
        '''
        self.key_set.remove(key)
        self.len = self.len - 1

    def from_dict(self, dict):
        '''
        add elements from dict type
        :param dict:input dict
        :return:
        '''
        for k, v in dict.items():
            self.add(k, v)

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

    def get_size(self):
        '''
        Element number in hash map.
        :return:number of element in hash map
        '''
        size = len(self.key_set)
        return size

    def from_list(self, list):
        '''
        add element from list type
        :param list:input list
        '''
        for k, v in enumerate(list):
            self.add(k, v)

    def to_list(self):
        '''
        Transfer hash map into list type
        :return:result list
        '''
        list = []
        for key in self.key_set:
            list.append(self.get(key))
        return list

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

    def to_kv_entry_list(self):
        '''
        list to store all node in hash map
        :return: result list
        '''
        list = []
        for key in self.key_set:
            list.append(Node(key, self.get(key)))
        return list

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

    def __iter__(self):
        return iter(self.to_kv_entry_list())

    def __next__(self):
        if self.index >= self.len:
            raise StopIteration("end")
        else:
            self.index += 1
            val = self.get(self.key_set[self.index - 1])
            return val
