import unittest
import group


class TestCases(unittest.TestCase):
    #Task 1
    def test_groups_of_3_1(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        result = group.groups_of_3(numbers)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, result)

    def test_groups_of_3_2(self):
        numbers = [2,4,6,8,9,10,12,14,16]
        result = group.groups_of_3(numbers)
        expected = [[2, 4, 6], [8, 9, 10], [12, 14, 16]]
        self.assertEqual(expected, result)

    def test_groups_of_3_3(self):
        numbers = [2,4,6,8]
        result = group.groups_of_3(numbers)
        expected = [[2, 4, 6], [8]]
        self.assertEqual(expected, result)