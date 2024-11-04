import unittest

from solution import missing_number


class TestSolution(unittest.TestCase):
    def setUp(self):
        input7 = list(range(1000))
        input7.remove(500)
        input8 = list(range(1000))
        input9 = list(range(1, 1001))
        input11 = [i for i in range(100000)]  # 0 to 99999
        input11.remove(12345)

        self.inputs_output = [
            ([0, 1, 3], 2),
            ([0, 1, 2], 3),
            ([1, 2, 3], 0),
            ([1], 0),
            ([0], 1),
            ([0, 1, 2, 3, 4, 5], 6),
            (input7, 500),
            (input8, 1000),
            (input9, 0),
            ([], 0),
            (input11, 12345),
        ]

    def test_solution(self):
        for input_list, expected_output in self.inputs_output:
            self.assertEqual(missing_number(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()