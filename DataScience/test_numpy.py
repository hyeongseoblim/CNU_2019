import sys
from datetime import datetime
import numpy


def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

def numptsum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b
    return c


if __name__ == '__main__':
    input_data = int(sys.argv[1])
    start = datetime.now()
    pythonsum(input_data)
    end = datetime.now()-start
    print(end)
    start = datetime.now()
    numptsum(input_data)
    end2 = datetime.now()-start
    print(end2)

