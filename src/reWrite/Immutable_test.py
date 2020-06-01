import unittest

from hypothesis import given
import hypothesis.strategies as st

from src.reWrite.Immutable import HashMap, to_list, getSize, from_list, find_iseven, filter_iseven, a_map, \
    reduce, mempty, mconcat, iterator, get, put, del_, to_dict


class TestImmutableList(unittest.TestCase):
    # 1. add a new element
    def test_put(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(put(put(HashMap(), 1, 2), 2, 3)), {1: 2, 2: 3})


    def test_get(self):
        self.assertEqual(get(put(HashMap(), 1, 2), 1), 2)
        self.assertEqual(get(put(HashMap(), 3, 4), 3), 4)

    # 2. remove an element
    def test_del_(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(del_(put(HashMap(), 1, 2), 1)), {})


    #
    # 3. size
    def test_getSize(self):
        self.assertEqual(getSize(put(HashMap(), 1, 2)), 1)
        self.assertEqual(getSize(del_(put(HashMap(), 1, 2), 1)), 0)


    # 4. conversion from and to python lists
    def test_from_list(self):
        lis = [1, 2]
        self.assertEqual(to_list(from_list([])), [])
        self.assertEqual(to_list(from_list(lis)), lis)

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(put(HashMap(), 1, 2)), [2])
        self.assertEqual(to_list(put(put(HashMap(), 1, 2), 2, 3)), [2, 3])

    # 5. ﬁnd element by speciﬁc predicate
    def test_find_iseven(self):
        self.assertEqual(find_iseven(put(put(HashMap(), 1, 2), 2, 3)), [2])
        self.assertEqual(find_iseven(put(put(put(HashMap(), 1, 2), 2, 3),3,4)), [2, 4])

    # 6. ﬁlter data structure by speciﬁc predicate
    def test_filter_iseven(self):
        self.assertEqual(filter_iseven(put(put(HashMap(), 1, 2), 2, 3)), [3])
        self.assertEqual(filter_iseven(put(put(put(HashMap(), 1, 2), 2, 3),3,1)), [3, 1])


    # 7. map structure by speciﬁc function(有错)
    def test_a_map(self):
        self.assertEqual(to_dict(map(HashMap(), str)), {})
        # self.assertEqual(to_dict(map(put(HashMap(), 1, 2), str)), {1: '2'})
        # hash = HashMap()
        # self.assertEqual(a_map(hash, str), [])
        # put(hash, 1, 1)
        # put(hash, 2, 2)
        # self.assertEqual(a_map(hash, str), ['1', '2'])
        # put(hash, 3, 3)
        # put(hash, 4, 4)
        # self.assertEqual(a_map(hash, lambda x: x + 1), [2, 3, 4, 5])

    # 8. reduce – process structure elements to build a return value by speciﬁc functions（有错）
    def test_a_reduce(self):
        self.assertEqual(reduce(HashMap(), lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce(HashMap({'3': 23, '4': 323}), lambda st, e: st + e, 0), 346)
        # # sum of empty list
        # hash = HashMap()
        # self.assertEqual(reduce(hash, lambda st, e: st + e, 0), 0)
        # # sum of list
        # hash = HashMap()
        # from_list(hash, [1, 2, 3])
        # self.assertEqual(reduce(hash, lambda st, e: st + e, 0), 6)

    # 9. mempty and mconcat
    def test_mempty(self):
        self.assertEqual(to_list(mempty(put(HashMap(), 1, 2))), [])
        self.assertEqual(to_list(mempty(put(put(HashMap(), 1, 2), 2, 3))), [])

    # 有错
    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(to_dict(mconcat(put(HashMap(), 1, 2), None)), to_dict(put(HashMap(), 0, 2)))
        self.assertEqual(to_dict(mconcat(None, put(HashMap(), 1, 2))), to_dict(put(HashMap(), 0, 2)))

        # hash = HashMap()
        # hash1 = HashMap()
        # mconcat(hash, hash1)
        # self.assertEqual(to_list(hash), [])
        # from_list(hash, [1])
        # from_list(hash1, [2])
        # hash2 = mconcat(hash, hash1)
        # self.assertEqual(to_list(hash2), [1, 2])

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
    def test_monoid_identity(self, lst):
        hash = HashMap()
        a = from_list(hash, lst)
        self.assertEqual(mconcat(None, a), a)
        self.assertEqual(mconcat(a, None), a)

    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        hash = HashMap()
        from_list(hash, a)
        self.assertEqual(to_list(hash), a)

    @given(st.lists(st.integers()))
    def test_to_list(self, lst):
        hash = HashMap()
        from_list(hash, lst)
        self.assertEqual(to_list(hash), lst)

    @given(key=st.integers(), value=st.integers())
    def test_add(self, key, value):
        hash = HashMap()
        a = put(hash, key, value)
        self.assertEqual(get(hash, key), value)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        from_list(hash_a, a)
        from_list(hash_b, b)
        from_list(hash_c, c)
        a_b = mconcat(hash_a, hash_b)
        b_a = mconcat(hash_b, hash_a)
        self.assertEqual(to_list(a_b), to_list(b_a))
        c_b = mconcat(hash_c, hash_b)
        b_c = mconcat(hash_b, hash_c)
        self.assertEqual(to_list(c_b), to_list(b_c))
        a_b__c = mconcat(hash_c, a_b)
        a__b_c = mconcat(hash_a, b_c)
        self.assertEqual(to_list(a_b__c), to_list(a__b_c))

        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(to_list(mconcat(None, hash_a)), to_list(hash_a))
        self.assertEqual(to_list(mconcat(hash_a, None)), to_list(hash_a))

    # 10. iterator
    def test_iter(self):
        x = [1, 2, 3]
        hash = HashMap()
        from_list(hash, x)
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
