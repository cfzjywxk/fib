"""Tiny fibonacci library used to rehearse the hcom GitHub PR lane."""


def fib(n: int) -> int:
    """Return the n-th Fibonacci number, with fib(0) == 0 and fib(1) == 1."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main(argv: list[str]) -> int:
    n = int(argv[1])
    print(fib(n))
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv))
