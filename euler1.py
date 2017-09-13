import sys


if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
    except TypeError:
        n = 1000
else:
    n = 1000

print sum(range(1, n, 3), range(1, n, 5))
