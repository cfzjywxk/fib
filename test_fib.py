import unittest

import io
from contextlib import redirect_stderr, redirect_stdout

from fib import fib, main


class FibTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual([fib(i) for i in range(8)], [0, 1, 1, 2, 3, 5, 8, 13])

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            fib(-1)

    def test_cli_prints_value(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(main(["fib.py", "10"]), 0)
        self.assertEqual(out.getvalue().strip(), "55")

    def test_cli_rejects_bad_input(self):
        err = io.StringIO()
        with redirect_stderr(err):
            self.assertEqual(main(["fib.py", "x"]), 1)
            self.assertEqual(main(["fib.py", "-3"]), 1)
            self.assertEqual(main(["fib.py"]), 2)
        self.assertIn("non-negative integer", err.getvalue())


if __name__ == "__main__":
    unittest.main()
