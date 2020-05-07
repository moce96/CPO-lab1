from hashMap_test.hashMap_immutable import from_list


class HashMap(object):

    def __init__(self):
        self._table = [[None for i in range(1)] for i in range(13)]
        self._mod = 13


    # 链式解决碰撞
    def add(self, element):
        remainer = element % self._mod
        if self._table[remainer][0] is None:
            self._table[remainer][0] = element
        else:
            index = 1
            while self._table[remainer][index] != None & self._table[remainer][index] != element:
                index = index+1
            self._table[remainer][index] = element


    def remove(self, element):
        remainer = element % self._mod
        if self._table[remainer][0] is None:
            return false
        else:
            for i in range(len(self._table[remainer])):
                if self._table[remainer][i] == element:
                    self._table[remainer][i] = self._table[remainer][len(self._table[remainer]) - 1]
                    self._table[remainer].pop()  # 这里还没写完，add也有问题，相同元素的问题
                    break
                while i == len(self._table[remainer]) - 1:
                    return false


    # def remove(self,element):
    #     remainder=element % self._mod
    #     for i in range(len(self._table[remainder])):
    #         if self._table[remainder][i]==element:
    #             self._table[remainder][i]=None
    #     return 0



    def size(self):
        sum = 0
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    sum += 1

        return sum


    def to_list(self):
        mylist = []
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    mylist.append(self._table[i][j])
        return mylist


    def from_list(self, input_list):  # 需要返回set吗
        fr_list = input_list
        for i in range(len(fr_list)):
            self.add(fr_list[i])

    def find_iseven(self):  # 这个方法测试时应该不用tollist了，因为直接输出了个list，下面一样
        mylist = []
        mylist1 = []
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    mylist.append(self._table[i][j])
        for k in range(len(mylist)):
            if mylist[k] % 2 == 0:
                mylist1.append(mylist[k])
        return mylist1

    def filter_iseven(self):
        mylist = []
        mylist1 = []
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    mylist.append(self._table[i][j])
        for k in range(len(mylist)):
            if mylist[k] % 2 != 0:
                mylist1.append(mylist[k])
        return mylist1

    def map(self, f):
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    self._table[i][j] = f(self._table[i][j])

    def reduce(self, f, initial_state):  # 这个没看懂
        state = initial_state
        for i in range(self._mod):
            for j in range(len(self._table[i])):
                if self._table[i][j] != None:
                    state = f(state, self._table[i][j])

        return state

    def mempty(self):
        return None

    def mconcat(self,a, b):  # a,b是list类型
        from_list(a)
        from_list(b)

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