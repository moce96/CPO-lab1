import unittest
from hypothesis import given
import hypothesis.strategies as st
from src.hashMap_mutable import *


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
        # hash.map(str)
        self.assertEqual( hash.map(str), ["1", "2", "3"])




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

    def test_hash(self):
        hash = HashMap()
        hash.add(14)
        hash.add(1)
        #mod is 13
        a = hash.get_hash(14)
        b = hash.get_hash(1)
        self.assertEqual(a[0],b[0])
        #Two numbers have the same key value


    def test_mconcat(self):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        hash_d = HashMap()
        hash_a.add_from_list([1, 2, 3])
        hash_b.add_from_list([5, 6, 7])
        hash_c.add_from_list([1, 2, 3, 5, 6, 7])
        hash_d.add_from_list([8, 9, 10])
        self.assertEqual(HashMap.mconcat(hash_a, hash_b).to_list(), hash_c.to_list())
        #(a·b)·c = a·(b·c)
        self.assertEqual(HashMap.mconcat(hash_a, HashMap.mconcat(hash_b,hash_d)).to_list(), HashMap.mconcat(HashMap.mconcat(hash_a,hash_b),hash_d).to_list())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        hash = HashMap()
        hash.from_list(a)
        b = hash.to_list()
        self.assertEqual(a,b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        hash = HashMap()

        hash.from_list(a)
        self.assertEqual(hash.size(), len(a))

    @given(st.lists(st.integers()))
    def test_associative_property(self,a):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        hash_a.from_list([1, 2, 3])
        hash_b.from_list([5, 6, 7])
        hash_c.from_list(a)
        self.assertEqual(HashMap.mconcat(hash_a, HashMap.mconcat(hash_b, hash_c)).to_list(),HashMap.mconcat(HashMap.mconcat(hash_a, hash_b), hash_c).to_list())

    @given(a=st.lists(st.integers()),b=st.lists(st.integers()))
    def test_identity_element_property(self, a, b):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_a.from_list(a)
        hash_b.from_list(b)
        a_b = HashMap.mconcat(hash_a,hash_b)  # {}
        b_a = HashMap.mconcat(hash_a,hash_b)  # {}
        self.assertEqual(a_b, b_a)

    def test_hash_collision(self):
        hash = HashMap()
        hash.add(14)
        hash.add(27)
        self.assertEqual(hash.get_hash(27)[0], hash.get_hash(14)[0])
        self.assertNotEqual(hash.get_hash(27)[1], hash.get_hash(14)[1])
        #The two numbers have the same key value, but the serial number in the same bucket is different. The chain solves the collision

if __name__ == '__main__':
    unittest.main()