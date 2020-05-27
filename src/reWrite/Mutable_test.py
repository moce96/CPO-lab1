import unittest
from hypothesis import given
import hypothesis.strategies as st

from src.reWrite.Mutable import HashMap


class TestMutableList(unittest.TestCase):
    # 1. add a new element
    def test_add(self):
        hash = HashMap()
        hash.add(1)
        self.assertEqual(hash.to_list(), [1])
        hash.add(2)
        self.assertEqual(hash.to_list(), [1, 2])
        hash.add(3)
        self.assertEqual(hash.to_list(), [1, 2, 3])

    # 2. remove an element
    def test_remove(self):
        hash = HashMap()
        hash.add(0)
        hash.add(1)
        hash.add(2)
        hash.add(3)
        self.assertEqual(hash.to_list(), [0, 1, 2,3])
        hash.remove(2)
        hash.remove(3)
        self.assertEqual(hash.to_list(), [0, 1])
        hash.remove(1)
        self.assertEqual(hash.to_list(), [0])
    #
    # 3. size
    def test_size(self):
        hash = HashMap()
        hash.add(0)
        hash.add(1)
        hash.add(2)
        hash.add(3)
        self.assertEqual(hash.getSize(), 4)
        hash.remove(0)
        self.assertEqual(hash.getSize(), 3)
        hash.add(4)
        hash.add(5)
        self.assertEqual(hash.getSize(), 5)
    #
    #
    # # 4. conversion from and to python lists
    def test_to_list(self):
        hash = HashMap()
        hash.add(0)
        hash.add(1)
        hash.add(2)
        hash.add(3)
        self.assertEqual(hash.to_list(), [0, 1, 2, 3])
        hash2 = HashMap()
        self.assertEqual(hash2.to_list(), [])


    def test_from_list(self):
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            hash = HashMap()
            hash.from_list(e)
            self.assertEqual(hash.to_list(), e)


    #
    # # 5. ﬁnd element by speciﬁc predicate
    def test_find_iseven(self):
        hash = HashMap()
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.find_iseven(), [2])
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.find_iseven(), [2, 4])
    #
    # # 6. ﬁlter data structure by speciﬁc predicate
    def test_filter_iseven(self):
        hash = HashMap()
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.filter_iseven(), [1])
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.filter_iseven(), [1, 3])
    #
    # # 7. map structure by speciﬁc function
    def test_a_map(self):
        hash = HashMap()
        self.assertEqual(hash.a_map(str), [])
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.a_map(str), ['1', '2'])
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.a_map(lambda x: x + 1), [2, 3, 4, 5])
    #
    #
    # # 8. reduce: process structure elements to build a return value by speciﬁc functions
    def test_a_reduce(self):
        hash = HashMap()
        self.assertEqual(hash.reduce(lambda st, e: st + e, 0), 0)
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.reduce(lambda st, e: st + e, 0), 3)
        hash.add(3)
        hash.add(4)
        self.assertEqual(hash.reduce(lambda st, _: st + 1, 0), 4)

    # # 9. mempty and mconcat
    def test_mempty(self):
        hash = HashMap()
        self.assertEqual(hash.mempty().to_list(), [])
        hash.add(1)
        hash.add(2)
        self.assertEqual(hash.mempty().to_list(), [])
    #
    def test_mconcat(self):
        hash = HashMap()
        hash1=HashMap()
        hash.mconcat(hash1)
        self.assertEqual(hash.to_list(), [])
        hash1.add(1)
        hash1.add(2)
        hash.mconcat(hash1)
        self.assertEqual(hash.to_list(), [1, 2])

    #
    #
    # 10. iterator
    def test_iter(self):
        hash = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(hash))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        hash = HashMap()
        hash.from_list(a)
        b = hash.to_list()

        self.assertEqual(a.sort(), b.sort())

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        hash = HashMap()
        hash.from_list(a)
        self.assertEqual(hash.getSize(), len(a))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_monoid_identity(self, a, b):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_a.from_list(a)
        hash_b.from_list(b)
        a_b = hash_a.mconcat(hash_b)  # {}
        b_a = hash_b.mconcat(hash_a)  # {}
        self.assertEqual(a_b, b_a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        dict_a = HashMap()
        dict_b = HashMap()
        dict_c = HashMap()
        dict_a.from_list(a)  # {}
        dict_b.from_list(b)  # {}
        dict_c.from_list(c)  # {0 0}
        a_b = dict_a.mconcat(dict_b)  # {}
        b_a = dict_b.mconcat(dict_a)  # {}
        self.assertEqual(a_b, b_a)
        c_b = dict_c.mconcat(dict_b)  # {0,0}
        b_c = dict_b.mconcat(dict_c)  # {0,0}
        self.assertEqual(c_b, b_c)
        a_b__c = dict_c.mconcat(a_b)
        a__b_c = dict_a.mconcat(b_c)
        self.assertEqual(a_b__c, a__b_c)

    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        hash = HashMap()
        hash.from_list(a)
        self.assertEqual(hash.to_list().sort(), a.sort())


if __name__ == '__main__':
    unittest.main()