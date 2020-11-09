def isSimple(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return counter == 2


def primes():
    a = 1
    while True:  # просто пример
        a += 1
        if isSimple(a):
            yield a