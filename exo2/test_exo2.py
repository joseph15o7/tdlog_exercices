import unittest
from exo2 import test

class TestSolution(unittest.TestCase):
    def test_fixed_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for s, ending in fixed_tests_True:
            with self.subTest(s=s, ending=ending):
                self.assertTrue(test(s, ending))

    def test_fixed_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for s, ending in fixed_tests_False:
            with self.subTest(s=s, ending=ending):
                self.assertFalse(test(s, ending))

if __name__ == "__main__":
    unittest.main()