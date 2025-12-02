# Lab 4 - Generator (fibonacci)


def myTest():
    yield 1
    yield 5
    yield 6
    yield 99



def fibonacci(limit):
    a, b = 1, 1
    while a < limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    a = myTest()
    b = myTest()


    print (     a.__next__()    )
    print (     a.__next__()    )

    print(      b.__next__()    )
    print(      b.__next__()    )

    print(      a.__next__()    )

    for i in fibonacci(1000000):
        print(i)