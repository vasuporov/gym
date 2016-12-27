"""
Generators - the producer of data.
- Very fast
- Lesser memory consumption
- Lazy generation (or on demand) of values.

"""


def fibo():
    """
    iterator/generator that produces fibonacci series
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for f in fibo():
    print f
    if f > 10:
        break