# O(loglogn)


def findPrimes(n):
    ret = []
    records = dict()
    i = 2
    while i <= n:
        while i in records:
            i += 1
        if i <= n:
            ret.append(i)
            w = i*2
            while w <= n:
                records[w] = True
                w += i
            i += 1
    return ret


def isPrime(n):
    if n <= 1 or n % 2 == 0:
        return False
    if n < 4:
        return True
    i = 3
    end = sqrt(n)
    while i <= end:
        if n % i == 0:
            print i
            return False
        i += 2
    return True
