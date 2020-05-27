import hypothesis.strategies as st


# Chain solution collision
def add(n, element):
    n.list_backup.append(element)
    remainer = element % n.mod
    if n.table[remainer][0] is None:
        n.table[remainer][0] = element
    else:
        flag = 0
        for i in n.table[remainer]:
            if n.table[remainer][i]==element:
                flag=1
            # if element == i:
            #     flag = 1
        if flag == 0:
            n.table[remainer].append(element)


def add_from_list(n, element_list):
    for element in element_list:
        remainer = element % n.mod
        if n.table[remainer][0] is None:
            n.table[remainer][0] = element
        else:
            flag = 0
            for i in n.table[remainer]:
                if element == i:
                    flag = 1
            if flag == 0:
                n.table[remainer].append(element)



def remove(n, element):
    remainer = element % n.mod
    if n.table[remainer][0] is None:
        return 0
    else:
        for i in range(len(n.table[remainer])):
            if n.table[remainer][i] == element:
                n.table[remainer][i] = n.table[remainer][len(n.table[remainer]) - 1]
                n.table[remainer].pop()
                break
            while i == len(n.table[remainer]) - 1:
                return 0
    n.count = n.count + 1



def size(n):
    return len(n.list_backup) - n.count


def to_list(n):
    return n.list_backup


def from_list(n,input_list):
    fr_list = input_list
    for i in range(len(fr_list)):
        add(n,fr_list[i])

def find_iseven(n):
    mylist = []
    mylist1 = []
    for i in range(n.mod):
        for j in range(len(n.table[i])):
            if n.table[i][j] != None:
                mylist.append(n.table[i][j])
    for k in range(len(mylist)):
        if mylist[k] % 2 == 0:
            mylist1.append(mylist[k])
    return mylist1

def filter_iseven(n):
    mylist = []
    mylist1 = []
    for i in range(n.mod):
        for j in range(len(n.table[i])):
            if n.table[i][j] != None:
                mylist.append(n.table[i][j])
    for k in range(len(mylist)):
        if mylist[k] % 2 != 0:
            mylist1.append(mylist[k])
    return mylist1

def Map(n,f):
    map_list = []
    for i in range(n.mod):
        for j in range(len(n.table[i])):
            if n.table[i][j] != None:
                n.table[i][j] = f(n.table[i][j])
                map_list.append(n.table[i][j])
    return map_list


def reduce(n, f, initial_state):
    state = initial_state
    for i in range(n.mod):
        for j in range(len(n.table[i])):
            if n.table[i][j] != None:
                state = f(state, n.table[i][j])
    return state




def mempty(n):
    return None


def mconcat(a,b):
    assert type(a) is HashMap
    assert type(b) is HashMap
    list_b = to_list(b)
    add_from_list(a,list_b)
    return a



def iterator(n):
    if n is not None:
        res=[]
        for i in range(n.mod):
            for j in range(len(n.table[i])):
               if n.table[i][j]!= None:
                 res.append(n.table[i][j])
        a=iter(res)
    else:
        a=None

    def get_next():
        if a is None:
            return False
        else:
            return next(a)
    return get_next





class HashMap(object):

    def __init__(self,values=None):
        self.table = [[None for i in range(1)] for i in range(13)]
        self.mod = 13
        # self.list_backup = []
        # self.count = 0

