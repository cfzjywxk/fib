"""Tiny fibonacci library used to rehearse the hcom GitHub PR lane."""

import sys


def fib(n: int) -> int:
    """Return the n-th Fibonacci number, with fib(0) == 0 and fib(1) == 1."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: fib.py N", file=sys.stderr)
        return 2
    try:
        n = int(argv[1])
        value = fib(n)
    except ValueError:
        print(f"fib.py: N must be a non-negative integer, got {argv[1]!r}", file=sys.stderr)
        return 1
    print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
