
class HashMap(object):

    def __init__(self):
        self.table = [[None for i in range(1)] for i in range(13)]
        self.mod = 13



    def add(self, element):
        remainer = element % self.mod
        if self.table[remainer][0] is None:
            self.table[remainer][0] = element
        else:
            flag = 0
            for i in self.table[remainer]:
                if element == i:
                    flag = 1
            if flag == 0:
                self.table[remainer].append(element)



    def add_from_list(self, element_list):

        for element in element_list:
            remainer = element % self.mod
            if self.table[remainer][0] is None:
                self.table[remainer][0] = element
            else:
                flag = 0
                for i in self.table[remainer]:
                    if element == i:
                        flag = 1
                if flag == 0:
                    self.table[remainer].append(element)


    def remove(self, element):
        remainer = element % self.mod
        if self.table[remainer][0] is None:
            return 0
        else:
            for i in range(len(self.table[remainer])):
                if self.table[remainer][i] == element:
                    self.table[remainer][i] = self.table[remainer][len(self.table[remainer]) - 1]
                    self.table[remainer].pop()
                    break
                while i == len(self.table[remainer]) - 1:
                    return 0


    # def remove(self,element):
    #     remainder=element % self.mod
    #     for i in range(len(self.table[remainder])):
    #         if self.table[remainder][i]==element:
    #             self.table[remainder][i]=None
    #     return 0



    def size(self):
        sum = 0
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    sum += 1

        return sum


    def to_list(self):
        mylist = []
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    mylist.append(self.table[i][j])
        return mylist


    def from_list(self, input_list):
        fr_list = input_list
        for i in range(len(fr_list)):
            self.add(fr_list[i])



    def find_iseven(self):
        mylist = []
        mylist1 = []
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    mylist.append(self.table[i][j])
        for k in range(len(mylist)):
            if mylist[k] % 2 == 0:
                mylist1.append(mylist[k])
        return mylist1

    def filter_iseven(self):
        mylist = []
        mylist1 = []
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    mylist.append(self.table[i][j])
        for k in range(len(mylist)):
            if mylist[k] % 2 != 0:
                mylist1.append(mylist[k])
        return mylist1

    def map(self, f):
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    self.table[i][j] = f(self.table[i][j])

    def reduce(self, f, initial_state):
        state = initial_state
        for i in range(self.mod):
            for j in range(len(self.table[i])):
                if self.table[i][j] != None:
                    state = f(state, self.table[i][j])

        return state

    def mempty(self):
        return None

    def mconcat(a, b):
        assert type(a) is HashMap
        assert type(b) is HashMap
        list_b = b.to_list()
        a.add_from_list(list_b)
        return a


    def __iter__(self):
        return self

    def __next__(self):

        start = 0
        end = len(self.to_list)
        if start == end:
            raise StopIteration
        tmp = self.to_list[start]
        start += 1
        return tmp