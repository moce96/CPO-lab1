import unittest

from hypothesis import given
import hypothesis.strategies as st

from src.hashMap_immutable import to_dict, put, HashMap, get, del_, getSize, to_list, from_list, find_iseven, \
    filter_iseven, reduce, mempty, mconcat, iterator,map


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


    # 7. map structure by speciﬁc function
    def test_map(self):
        self.assertEqual(to_dict(map(HashMap(), str)), {})
        self.assertEqual(to_dict(map(put(HashMap(), 1, 2), str)), {1: '2'})


    # 8. reduce – process structure elements to build a return value by speciﬁc functions
    def test_a_reduce(self):
        self.assertEqual(reduce(HashMap(), lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce(put(put(HashMap(), 1, 2), 2, 3), lambda st, e: st + e, 0), 5)

    # 9. mempty and mconcat
    def test_mempty(self):
        self.assertEqual(to_list(mempty(put(HashMap(), 1, 2))), [])
        self.assertEqual(to_list(mempty(put(put(HashMap(), 1, 2), 2, 3))), [])

    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(to_dict(mconcat(put(HashMap(), 1, 2), None)), to_dict(put(HashMap(), 1, 2)))
        self.assertEqual(to_dict(mconcat(None, put(HashMap(), 1, 2))), to_dict(put(HashMap(), 1, 2)))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), key=st.integers(), value=st.integers())
    def test_immutable(self, a, b, key, value):
        table = from_list(HashMap(),a)
        table_temp = table
        table1 = put(table, key, value)
        self.assertNotEqual(id(table), id(table1))
        self.assertEqual(to_dict(table), to_dict(table_temp))

        table3 = del_(table, key)
        table_temp = table1
        self.assertNotEqual(id(table1), id(table3))
        self.assertEqual(to_dict(table_temp), to_dict(table1))

        table4 = from_list(HashMap(),b)
        table3_temp = table3
        table4_temp = table4
        table5 = mconcat(table3, table4)
        table6 = mconcat(table4, table3)
        # self.assertNotEqual(id(table5), id(table6))
        self.assertEqual(to_dict(table3_temp), to_dict(table3))
        self.assertEqual(to_dict(table4_temp), to_dict(table4))

    def test_hash_collision(self):
        table1 = HashMap()
        table2 = HashMap()
        table1 = put(table1, 1, 3)
        table2 = put(table2, 14, 3)
        self.assertEqual(get(table1, 1), get(table2, 14))
        # means the key of 1 and 12 have the same hash_value;
        # put the the key that have same init_hash_value
        table1 = put(table1, 14, 4)

        # now they have different hash_value, beacase the collision happen, to deal the collision the key rehash unit have not coollision
        self.assertNotEqual(get(table1, 14), get(table2, 14))



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
    def test_put(self, key, value):
        hash = HashMap()
        a = put(hash, key, value)
        self.assertEqual(get(hash, key), value)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_monoid_identity(self, a, b):
        hash = HashMap()
        hash_a = HashMap()
        from_list(hash_a,a)
        a_b=mconcat(mempty(hash),hash_a)  # {}
        b_a=mconcat(hash_a,mempty(hash))  # {}
        self.assertEqual(a_b, hash_a)
        self.assertEqual(a_b, b_a)




    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        hash_a = HashMap()
        hash_b = HashMap()
        hash_c = HashMap()
        from_list(hash_a, a)
        from_list(hash_b, b)
        from_list(hash_c, c)
        a_b = mconcat(hash_a, hash_b)
        b_c = mconcat(hash_b, hash_c)
        a_b__c=mconcat( a_b,hash_c)
        a__b_c=mconcat(hash_a,b_c)
        self.assertEqual(a_b__c, a__b_c)

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
