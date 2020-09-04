class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        if n < 4:
            return 1
        res, t, data = 1, 3, set()
        while t < n:
            if t not in data:
                res += 1
                te = t
                while te < n:
                    data.add(te)
                    te += t
            t += 2
        return res

