import unittest

from solution import longest_common_prefix


class LongestCommonPrefixTests(unittest.TestCase):
    def setUp(self):
        self.input_outputs = (
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["interspecies", "interstellar", "interstate"], "inters"),
            (["apple", "ape", "april"], "ap"),
            ([""], ""),
            (["a"], "a"),
            (["abc", "abc", "abc"], "abc"),
            (["ab", "a"], "a"),
            (["reflower", "flow", "flight"], ""),
            (["precompute", "prefix", "pretext"], "pre"),
            (["single"], "single"),
            (["hello", "hell", "heaven", "heavy"], "he"),
            (["swift", "swipe", "swirl"], "swi"),
            (["glow", "glorious", "glide"], "gl"),
            (["overlap", "oversee", "overcome"], "over"),
            (["", ""], ""),
            (["same", "same", "same"], "same"),
            (["ant", "antenna", "antique", "ant"], "ant"),
        )

    def test_longest_common_prefix(self):
        for input_list, expected_output in self.input_outputs:
            self.assertEqual(longest_common_prefix(input_list), expected_output)


if __name__ == "__main__":
    unittest.main()
