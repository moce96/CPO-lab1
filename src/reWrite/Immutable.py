

# 1. add a new element
def add(self,key):
    hash_value=key % 13
    #If the hash value in the linked list is not already occupied by other data, the pending data (key) is placed there
    if self.data[hash_value].data ==None:
        self.data[hash_value].data=key
    else:

        temp=Node(key)
        p=self.data[hash_value]
        while p.next != None:
            p=p.next
        p.next=temp

def add_from_list(self, element_list):
    for element in element_list:
        hash_value = element % 13

        if self.data[hash_value].data == None:
            self.data[hash_value].data = element
        else:

            temp = Node(element)
            p = self.data[hash_value]
            while p.next != None:
                p = p.next
            p.next = temp

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
    sum = 0

    i = 0
    while i < 13:
        if self.data[i].data == None:
            i += 1
            continue
        else:
            p = self.data[i]
            while p != None:
                sum += 1
                p = p.next
            i += 1

    return sum


    # 4. conversion from and to python lists
def to_list(self):
    list = []
    i = 0
    while i < 13:
        if self.data[i].data == None:
            i += 1
            continue
        else:
            p = self.data[i]
            while p != None:
                list.append(p.data)
                p = p.next

            i += 1

    return list


def from_list(self, list):
    for i in list:
        self.add(i)
    return self


# 5. ﬁnd element by speciﬁc predicate
def find_iseven(self):
    mylist = to_list(self)
    mylist1 = []
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
    return list([])


def mconcat(a, b):
    if a is None:
        return b
    # if b is None:
    #     return a
    if b is not None:
        list = to_list(b)
        for i in list:
            add(a,i)
    return a



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


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
