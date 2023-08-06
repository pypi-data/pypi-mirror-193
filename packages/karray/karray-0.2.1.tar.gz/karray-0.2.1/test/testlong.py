import unittest
import numpy as np
import karray as ka

class TestLongClass(unittest.TestCase):
#passes
    def test_get_item_datetime64(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long['one', list(np.array(['2022-11-23'], dtype='datetime64[ns]'))]
        expected = ka.Long({'one': np.array(['2022-11-23'], dtype='datetime64[ns]')},[6.0])
        self.assertEqual(expected, actual)

#passes
    def test_get_item_ndarray(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long['one', np.array(['2022-11-23'], dtype='datetime64[ns]')]
        expected = ka.Long({'one': np.array(['2022-11-23'], dtype='datetime64[ns]')},[6.0])
        self.assertEqual(expected, actual)

#passes
    def test_get_item_list_string(self):
        long = ka.Long({'one':['aaa', 'bbb','ccc']}, [4.0, 5.0, 6.0])
        actual = long['one', ['ccc']]
        expected = ka.Long({'one': ['ccc']},[6.0])
        self.assertEqual(expected, actual)

#passes
    def test_get_item_list_int(self):
        long = ka.Long({'one':[1, 2, 3]}, [4.0, 5.0, 6.0])
        actual = long['one', [1, 3]]
        expected = ka.Long({'one': [1, 3]},[4.0, 6.0])
        self.assertEqual(expected, actual)

#passes
    def test_get_item_list_slice(self):
        long = ka.Long({'one': [1, 2, 3, 5]}, [4.0, 5.0, 6.0, 7.0])
        actual = long['one', 3:]
        expected = ka.Long({'one': [3, 5]}, [6.0, 7.0])
        self.assertEqual(expected, actual)

#passes
    def test_index(self):
        long = ka.Long({'one':np.array(['2022-11-25','2022-11-26'], dtype='datetime64[ns]')}, [4.0, 5.0])
        actual = long.index
        expected = {'one':np.array(['2022-11-25','2022-11-26'], dtype='datetime64[ns]')}
        self.assertTrue(all(np.array_equal(act, exp) for act, exp in zip(actual, expected)))

#passes    
    def test_value(self):  
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long.value
        expected = np.array([4.0, 5.0, 6.0])
        self.assertTrue(np.array_equal(expected,actual))

#passes 
    def test_dims(self):
        long = ka.Long({'one':['aaa', 'bbb','ccc']}, [4.0, 5.0, 6.0])
        actual = long.dims
        expected = ['one']
        self.assertListEqual(expected,actual)

#passes 
    def test_size(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long.size
        expected = 3
        self.assertEqual(expected,actual)

#passes 
    def test_ndim(self):
        long = ka.Long({'one':['aaa', 'bbb','ccc']}, [4.0, 5.0, 6.0])
        actual = long.ndim
        expected = 1
        self.assertEqual(expected,actual)

#passes
    def test_insert_dict_and_list(self):
        long = ka.Long({'one':list(np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]'))}, [4.0, 5.0, 6.0])
        actual = long.insert(two={'one':[np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]'), np.array(['2022-11-16', '2022-11-17','2022-11-18'], dtype='datetime64[ns]')]})
        expected = ka.Long({'two':list(np.array(['2022-11-16', '2022-11-17','2022-11-18'], dtype='datetime64[ns]')),'one':list(np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]'))}, [4.0, 5.0, 6.0])
        self.assertEqual(expected, actual)

#passes
    def test_rename(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long.rename(one='two')
        expected = ka.Long({'two':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        self.assertEqual(expected, actual)

#passes
    def test_drop(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]'), 'two':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long.drop('one')
        expected = ka.Long({'two':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        self.assertEqual(expected, actual)

#passes
    def test_items(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = list(long.items())
        expected = [('one',np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')),('value', np.array([4.0, 5.0, 6.0]))]
        self.assertTrue(all(act[0] == exp[0] for act, exp in zip(actual, expected)))
        self.assertTrue(all(np.array_equal(act[1], exp[1]) for act, exp in zip(actual, expected)))

#passes
    def test_eq_long(self):
        A_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        B_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        self.assertEqual(A_long,B_long)

#passes
    def test_ne_long_by_dim(self):
        A_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        B_long = ka.Long({'two':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        self.assertNotEqual(A_long,B_long)

#passes
    def test_ne_long_by_dim_value(self):
        A_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        B_long = ka.Long({'one':np.array(['2022-11-27', '2022-11-27','2022-11-27'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        self.assertNotEqual(A_long,B_long)

#passes
    def test_ne_long_by_value(self):
        A_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        B_long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [1.0, 1.0, 1.0])
        self.assertNotEqual(A_long,B_long)

#passes
    def test_eq_value_float(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long == 5.0
        expected = np.array([False,True,False])
        self.assertTrue(np.array_equal(expected,actual))

#passes
    def test_eq_value_int(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, 6.0])
        actual = long == 5
        expected = np.array([False,True,False])
        self.assertTrue(np.array_equal(expected,actual))

#passes
    def test_eq_value_nan(self):
        long = ka.Long({'one':np.array(['2022-11-25', '2022-11-24','2022-11-23'], dtype='datetime64[ns]')}, [4.0, 5.0, np.nan])
        actual = long == np.nan
        expected = np.array([False,False,True])
        self.assertTrue(np.array_equal(expected,actual))



if __name__ == '__main__':
    unittest.main()