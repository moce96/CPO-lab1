import hypothesis.strategies as st


# Chain solution collision
def add(n, element):
    remainer = element % n._mod
    if n._table[remainer][0] is None:
        n._table[remainer][0] = element
    else:
        index = 1
        while n._table[remainer][index] != None &n._table[remainer][index] != element:
            index = index+1
        n._table[remainer][index] = element


def add_from_list(n,element__list):
    for element in element__list:
        remainer=element % n._mod
        if n._table[remainer][0] is None:
            n._table[remainer][0]=element
        else:
            flag=0
            for i in n.table[remainer]:
                if element == i:
                    flag = 1
            if flag == 0:
                n.table[remainer].append(element)



def remove(n, element):
    assert n is not None, "element should be in hashMap"
    remainer = element % n._mod
    if n._table[remainer][0] is None:
        return false
    else:
        for i in range(len(n._table[remainer])):
            if n._table[remainer][i] == element:
                n._table[remainer][i] = n._table[remainer][len(n._table[remainer]) - 1]
                n._table[remainer].pop()
                break
            while i == len(n._table[remainer]) - 1:
                return false



def size(n):
    sum = 0
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                sum += 1

    return sum


def to_list(n):
    mylist = []
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                mylist.append(n._table[i][j])
    return mylist


def from_list(n,input_list):
    fr_list = input_list
    for i in range(len(fr_list)):
        add(n,fr_list[i])

def find_iseven(n):
    mylist = []
    mylist1 = []
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                mylist.append(n._table[i][j])
    for k in range(len(mylist)):
        if mylist[k] % 2 == 0:
            mylist1.append(mylist[k])
    return mylist1

def filter_iseven(n):
    mylist = []
    mylist1 = []
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                mylist.append(n._table[i][j])
    for k in range(len(mylist)):
        if mylist[k] % 2 != 0:
            mylist1.append(mylist[k])
    return mylist1

def map(n,f):
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                n._table[i][j] = f(n._table[i][j])


def reduce(n, s):
    val_sum=0
    n1=0
    for i in range(n._mod):
        for j in range(len(n._table[i])):
            if n._table[i][j] != None:
                val_sum+=n._table[i][j]
                n1+=1
    if (s == 'sum'):
        return val_sum
    elif (s == 'mean'):
        return val_sum / n1


def concat(n1,n2):
    res=to_list(n2)
    for val in res:
        add(n1,val)
    return n1

def iterator(n):
    if n is not None:
        res=[]
        for i in range(n._mod):
            for j in range(len(n._table[i])):
               if n._table[i][j]!= None:
                 res.append(n._table[i][j])
        a=iter(res)
    else:
        a=None

    def get_next():
        if a is None:
            return False
        else:
            return next(a)
    return get_next


def mempty(n):
    return None


def mconcat(a,b):
    assert type(a) is HashMap
    assert type(b) is HashMap
    list_b = b.to_list()
    a.add_from_list(list_b)
    return a





class HashMap(object):

    def __init__(self,values=None):
        self._table = [[None for i in range(1)] for i in range(13)]
        self._mod = 13
        if values is not None:
            for val in values:
                add(self,val)