import unittest

from hashMap_test.hashMap_mutable import HashMap


class TestMutableList(unittest.TestCase):


    # lst = List()
    # self.assertEqual(lst.to_list(), [])
    # lst.add_to_head('a')
    # self.assertEqual(lst.to_list(), ['a'])
    # lst.add_to_head('b')
    # self.assertEqual(lst.to_list(), ['b', 'a'])

    # def test_add_to_head(self):
    #     lst = List()
    #     self.assertEqual(lst.to_list(), [])
    #     lst.add_to_head('a')
    #     self.assertEqual(lst.to_list(), ['a'])
    #     lst.add_to_head('b')
    #     self.assertEqual(lst.to_list(), ['b', 'a'])

    def test_add(self):
        hash= HashMap()
        self.assertEqual(hash.to_list(),[])
        hash.add(1)
        self.assertEqual(hash.to_list(),[1])
        hash.add(2)
        self.assertEqual(hash.to_list(), [1,2])



    def test_remove(self):
        hash = HashMap()
        hash.add(1)
        hash.remove(1)
        self.assertEqual(hash.size(),0)

        # def test_size(self):
        #     self.assertEqual(List().size(), 0)
        #     self.assertEqual(List(Node('a')).size(), 1)
        #     self.assertEqual(List(Node('a', Node('b'))).size(), 2)

    def test_size(self):
        hash = HashMap()
        self.assertEqual(hash.size(),0)
        hash.add(1)
        self.assertEqual(hash.size(), 1)
        hash.add(2)
        self.assertEqual(hash.size(), 2)


    def test_to_list(self):
        hash= HashMap()
        self.assertEqual(hash.to_list(),[])
        hash.add(1)
        self.assertEqual(hash.to_list(),[1])
        hash.add(2)
        self.assertEqual(hash.to_list(), [1,2])



    def test_from_list(self):
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            hash=HashMap()
            hash.from_list(e)
            self.assertEqual(hash.to_list(),e)


    def test_find_iseven(self):
        hash = HashMap()
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.find_iseven(),[2])
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.find_iseven(), [2,4])

    def test_filter_iseven(self):
        hash = HashMap()
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.filter_iseven(), [1])
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.filter_iseven(), [1, 3])

    def test_map(self):
        hash=HashMap()
        hash.map(str)
        self.assertEqual(hash.to_list(), [])
        hash=HashMap()
        hash.from_list([1,2,3])
        hash.map(str)
        self.assertEqual(hash.to_list(), ["1", "2", "3"])



    def test_reduce(self):
        # sum of empty list
         hash=HashMap()
         self.assertEqual(hash.reduce(lambda st, e: st + e, 0), 0)
    # sum of list
         hash=HashMap()
         hash.from_list([1,2,3])
         self.assertEqual(hash.reduce(lambda st, e: st + e, 0),6)
    # size

         test_data = [
                [],
                [1],
                [1, 2]
         ]
         for e in test_data:
             hash=HashMap()
             hash.from_list(e)
             self.assertEqual(hash.reduce(lambda st, _: st + 1, 0), hash.size())


if __name__ == '__main__':
    unittest.main()