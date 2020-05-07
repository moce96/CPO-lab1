import unittest

from hashMap_test.hashMap_immutable import remove, HashMap, add, to_list, size, from_list, find_iseven, filter_iseven, \
    reduce, concat, iterator


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
        add(hash1, 1)
        add(hash1, 2)
        hash2 = HashMap()
        add(hash2, 3)
        add(hash2, 4)
        hash3 = HashMap()
        add(hash3, 1)
        add(hash3, 2)
        add(hash3, 3)
        add(hash3, 4)
        self.assertEqual(to_list(concat(hash1, hash2)),to_list(hash3))

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