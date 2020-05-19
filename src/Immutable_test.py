import unittest


from hypothesis import given
import hypothesis.strategies as st

from src.hashMap_immutable import HashMap, add, to_list, remove, size, from_list, find_iseven, filter_iseven, reduce, \
    concat, iterator, add_from_list, mconcat


class TestImmutableList(unittest.TestCase):


    def test_add(self):
        hash=HashMap()
        add(hash,1)
        self.assertEqual(to_list(hash),[1])
        add(hash,2)
        self.assertEqual(to_list(hash), [1,2])


    def test_add_from_list(self):
        hash=HashMap()
        add_from_list(hash,[1,2,3])
        self.assertEqual(to_list(hash), [1, 2,3])


    def test_remove(self):
        hash = HashMap()
        add(hash,1)
        add(hash, 2)
        remove(hash,2)
        self.assertEqual(to_list(hash),[1])
        remove(hash, 1)
        self.assertEqual(to_list(hash), [])


    def test_size(self):
        hash = HashMap()
        add(hash, 1)
        self.assertEqual(size(hash), 1)
        add(hash,2)
        self.assertEqual(size(hash), 2)


    def test_to_list(self):
        hash = HashMap()
        add(hash, 1)
        self.assertEqual(to_list(hash), [1])
        add(hash, 2)
        self.assertEqual(to_list(hash), [1, 2])


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



    def test_find_iseven(self):
        hash = HashMap()
        add(hash,1)
        add(hash,2)
        self.assertEqual(find_iseven(hash), [2])
        add(hash,3)
        add(hash,4)
        self.assertEqual(find_iseven(hash), [2, 4])

    def test_filter_iseven(self):
        hash = HashMap()
        add(hash,1)
        add(hash,2)
        self.assertEqual(filter_iseven(hash), [1])
        add(hash,3)
        add(hash,4)
        self.assertEqual(filter_iseven(hash), [1, 3])


    # def test_map(self):
    #     hash = HashMap()
    #     add(hash, 1)
    #     map(to_list(hash), lambda x : x+1)
    #     self.assertEqual(to_list(hash),[])

    def test_reduce(self):
        hash = HashMap()
        add(hash, 1)
        add(hash, 2)
        self.assertEqual(reduce(hash, 'sum'), 3)

    def test_mconcat(self):
        hash1 = HashMap()
        hash2 = HashMap()
        hash3 = HashMap()
        hash4=HashMap()
        add_from_list(hash1,[1,2])
        add_from_list(hash2, [3,4])
        add_from_list(hash3, [1,2,3, 4])
        add_from_list(hash4,[5,6,7])
        self.assertEqual(to_list(mconcat(hash1, hash2)),to_list(hash3))
        self.assertEqual(to_list(mconcat(mconcat(hash1,hash2),hash4)),
                         to_list(mconcat(hash1,mconcat(hash2,hash4))))




    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        a=[1,2,3]
        hash = HashMap()
        from_list(hash, a)
        self.assertEqual(to_list(hash), a)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, lst):
        lst=[1,2,3]
        hash = HashMap()
        from_list(hash,lst)
        self.assertEqual(size(hash), len(lst))




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