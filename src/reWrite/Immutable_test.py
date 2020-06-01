import unittest

from hypothesis import given
import hypothesis.strategies as st

from src.reWrite.Immutable import HashMap, add, to_list, remove, getSize, from_list, find_iseven, filter_iseven, a_map, \
    reduce, mempty, mconcat, iterator


class TestImmutableList(unittest.TestCase):
    # 1. add a new element
    def test_add(self):
        hash = HashMap()
        add(hash, 1,1)
        self.assertEqual(to_list(hash), [1])
        add(hash, 2,2)
        self.assertEqual(to_list(hash), [1, 2])

    # 2. remove an element
    def test_remove(self):
        hash = HashMap()
        add(hash, 0,0)
        add(hash, 1,1)
        add(hash, 2,2)
        add(hash, 3,3)
        r_a=remove(hash,0)
        self.assertEqual(to_list(r_a), [1, 2,3])
        # remove(hash, 2)
        # self.assertEqual(to_list(hash), [0, 1])
    #
    # 3. size
    def test_getSize(self):
        hash = HashMap()
        add(hash, 0,0)
        add(hash, 1,1)
        add(hash, 2,2)
        add(hash, 3,3)
        self.assertEqual(getSize(hash), 4)
        remove(hash,3)
        self.assertEqual(getSize(hash), 3)

    # 4. conversion from and to python lists
    def test_from_list(self):
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            hash = HashMap()
            from_list(hash,e)
            self.assertEqual(to_list(hash), e)

    def test_to_list(self):
        hash = HashMap()
        add(hash, 0,0)
        add(hash, 1,1)
        add(hash, 2,2)
        add(hash, 3,3)
        self.assertEqual(to_list(hash), [0, 1, 2, 3])
        hash2 = HashMap()
        self.assertEqual(to_list(hash2), [])

    # 5. ﬁnd element by speciﬁc predicate
    def test_find_iseven(self):
        hash = HashMap()
        add(hash, 1,1)
        add(hash, 2,2)
        self.assertEqual(find_iseven(hash), [2])
        add(hash, 3,3)
        add(hash, 4,4)
        self.assertEqual(find_iseven(hash), [2, 4])

    # 6. ﬁlter data structure by speciﬁc predicate
    def test_filter_iseven(self):
        hash = HashMap()
        add(hash, 1,1)
        add(hash, 2,2)
        self.assertEqual(filter_iseven(hash), [1])
        add(hash, 3,3)
        add(hash, 4,4)
        self.assertEqual(filter_iseven(hash), [1, 3])

    # 7. map structure by speciﬁc function
    def test_a_map(self):
        hash = HashMap()
        self.assertEqual(a_map(hash,str), [])
        add(hash, 1,1)
        add(hash, 2,2)
        self.assertEqual(a_map(hash,str), ['1', '2'])
        add(hash, 3,3)
        add(hash, 4,4)
        self.assertEqual(a_map(hash,lambda x: x + 1), [2, 3, 4, 5])

    # 8. reduce – process structure elements to build a return value by speciﬁc functions
    def test_a_reduce(self):
        # sum of empty list
        hash = HashMap()
        self.assertEqual(reduce(hash, lambda st, e: st + e, 0), 0)
        # sum of list
        hash = HashMap()
        from_list(hash, [1, 2, 3])
        self.assertEqual(reduce(hash, lambda st, e: st + e, 0), 6)


    # 9. mempty and mconcat
    def test_mempty(self):
        hash = HashMap()
        add(hash, 1,1)
        add(hash, 2,2)
        self.assertEqual(to_list(mempty(hash)), [])

    def test_mconcat(self):
        hash = HashMap()
        hash1=HashMap()
        mconcat(hash, hash1)
        self.assertEqual(to_list(hash), [])
        add(hash, 1,1)
        add(hash1, 2,2)
        mconcat(hash,hash1)
        self.assertEqual(to_list(hash), [1, 2])


    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        hash = HashMap()
        from_list(hash, a)
        b = to_list(hash)
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, lst):
        hash = HashMap()
        from_list(hash, lst)
        self.assertEqual(getSize(hash), len(lst))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self,lst):
        hash = HashMap()
        a = from_list(hash,lst)
        self.assertEqual(mconcat(None, a),a)
        self.assertEqual(mconcat(a, None), a)



    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        hash = HashMap()
        from_list(hash,a)
        self.assertEqual(to_list(hash), a)



    # 10. iterator
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