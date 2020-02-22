import sys
import unittest
import sort.list_sorting as srt

class TestProcessFunction(unittest.TestCase):

    def setUp(self):
        self.list_ = [4, 7, 19, 95, 50, 71, 11, 133, 1, 99, 59]
        self.list_out = [1, 4, 7, 11, 19, 50, 59, 71, 95, 99, 133]
        
    def test_list_sort(self):
        list_update = srt.listsort(self.list_)
        self.assertListEqual(self.list_out, list_update)
        


if __name__ == '__main__':
    unittest.main() 