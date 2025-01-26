import unittest
from heapsort.HeapSort import heapsort

class TestHeapSort(unittest.TestCase):
    def test_sorted_list(self):
        mylist = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        heapsort(mylist)
        self.assertEqual(mylist, expected)

    def test_reverse_sorted_list(self):
        mylist = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        heapsort(mylist)
        self.assertEqual(mylist, expected)

    def test_unsorted_list(self):
        mylist = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected = sorted(mylist)
        heapsort(mylist)
        self.assertEqual(mylist, expected)

    def test_single_element_list(self):
        mylist = [42]
        expected = [42]
        heapsort(mylist)
        self.assertEqual(mylist, expected)

    def test_empty_list(self):
        mylist = []
        expected = []
        heapsort(mylist)
        self.assertEqual(mylist, expected)

    def test_duplicate_elements(self):
        mylist = [3, 3, 3, 3, 3]
        expected = [3, 3, 3, 3, 3]
        heapsort(mylist)
        self.assertEqual(mylist, expected)

if __name__ == "__main__":
    unittest.main()
