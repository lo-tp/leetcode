def findPrimes(n):
    res, record, i = [], {}, 2
    while i <= n:
        while i in record:
            i += 1
        res.append(i)
        k = 2*i
        while k <= n:
            record[k] = True
            k += i
        i += 1
    return res


class Solution(object):
    def groupAnagrams(self, strs):
        primes = findPrimes(100)
        mapping, record, res = {}, {}, []
        for i, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
            mapping[letter] = i
        for s in strs:
            w = reduce(lambda x, y: x*primes[mapping[y]], s, 1)
            if w not in record:
                record[w] = []
                res.append(record[w])
            record[w].append(s)

        return res
