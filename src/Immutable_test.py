import unittest


from hypothesis import given
import hypothesis.strategies as st

from src.hashMap_immutable import HashMap, add, to_list, add_from_list, remove, size, from_list, find_iseven, \
    filter_iseven, Map, reduce, mconcat, iterator


class TestImmutableList(unittest.TestCase):


    def test_add(self):
        hash=HashMap()
        add(hash,1)
        self.assertEqual(to_list(hash),[1])
        add(hash,2)
        self.assertEqual(to_list(hash), [1,2])



    def test_remove(self):

        hash = HashMap()
        add(hash,1)
        remove(hash,1)
        self.assertEqual(size(hash), 0)
    #
    #
    def test_size(self):
        hash = HashMap()
        add(hash, 1)
        self.assertEqual(size(hash), 1)
        add(hash,2)
        self.assertEqual(size(hash), 2)
    #
    #
    def test_to_list(self):
        hash = HashMap()
        add(hash, 1)
        self.assertEqual(to_list(hash), [1])
        add(hash, 2)
        self.assertEqual(to_list(hash), [1, 2])
    #
    #
    def test_from_list(self):
        test_data=[
            [],
            [1],
            [1,2]
        ]
        for e in test_data:
            hash=HashMap()
            from_list(hash,e)
            self.assertEqual(size(hash), len(e))
    #
    #
    #
    def test_find_iseven(self):
        hash = HashMap()
        add(hash,1)
        add(hash,2)
        self.assertEqual(find_iseven(hash), [2])
        add(hash,3)
        add(hash,4)
        self.assertEqual(find_iseven(hash), [2, 4])
    #
    def test_filter_iseven(self):
        hash = HashMap()
        add(hash,1)
        add(hash,2)
        self.assertEqual(filter_iseven(hash), [1])
        add(hash,3)
        add(hash,4)
        self.assertEqual(filter_iseven(hash), [1, 3])
    #
    #
    def test_map(self):
        hash = HashMap()
        Map(hash,str)
        self.assertEqual(to_list(hash), [])
        hash1 = HashMap()
        add(hash1,1)
        add(hash1, 2)
        add(hash1, 3)
        # hash.map(str)
        self.assertEqual(Map(hash1,str), ["1", "2", "3"])
    #
    def test_reduce(self):
        # sum of empty list
        hash = HashMap()
        self.assertEqual(reduce(hash,lambda st, e: st + e, 0), 0)
        # sum of list
        hash = HashMap()
        from_list(hash,[1, 2, 3])
        self.assertEqual(reduce(hash,lambda st, e: st + e, 0), 6)
        # size

        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            hash = HashMap()
            from_list(hash,e)
            self.assertEqual(reduce(hash,lambda st, _: st + 1, 0), size(hash))
    #
    def test_mconcat(self):
        hash1 = HashMap()
        hash2 = HashMap()
        hash3 = HashMap()
        hash4=HashMap()

        add_from_list(hash1,[1, 2, 3])
        add_from_list(hash2,[5, 6, 7])
        add_from_list(hash3,[1, 2, 3, 5, 6, 7])
        add_from_list(hash4,[8, 9, 10])
        self.assertEqual(to_list(mconcat(hash1, hash2)),to_list(hash3))
        self.assertEqual(to_list(mconcat(mconcat(hash1,hash2),hash4)),
                         to_list(mconcat(hash1,mconcat(hash2,hash4))))
    #
    #
    #
    #
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        hash = HashMap()
        from_list(hash,a)
        b = to_list(hash)
        self.assertEqual(a, b)
    #
    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, lst):
        hash = HashMap()
        from_list(hash,lst)
        self.assertEqual(size(hash), len(lst))

    @given(st.lists(st.integers()))
    def test_associative_property(self, a):
            hash_a = HashMap()
            hash_b = HashMap()
            hash_c = HashMap()
            from_list(hash_a,[1, 2, 3])
            from_list(hash_b,[5, 6, 7])
            from_list(hash_c,a)
            self.assertEqual(to_list(mconcat(hash_a, mconcat(hash_b, hash_c))),
                             to_list(mconcat(mconcat(hash_a, hash_b), hash_c)))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_identity_element_property(self, a, b):
                hash_a = HashMap()
                hash_b = HashMap()
                from_list(hash_a,a)
                from_list(hash_b,b)
                a_b =mconcat(hash_a, hash_b)  # {}
                b_a =mconcat(hash_a, hash_b)  # {}
                self.assertEqual(a_b, b_a)
    #
    #
    #
    def test_iter(self):
        x = [1, 2, 3]
        hash=HashMap()
        from_list(hash,x)
        tmp = []
        try:
            get_next = iterator(hash)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(hash), tmp)

        get_next = iterator(None)
        self.assertEqual(get_next(), False)


if __name__ == '__main__':
    unittest.main()