import unittest

from fib import fib


class FibTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual([fib(i) for i in range(8)], [0, 1, 1, 2, 3, 5, 8, 13])

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            fib(-1)


if __name__ == "__main__":
    unittest.main()
