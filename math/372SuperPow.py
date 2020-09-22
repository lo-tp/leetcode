class Solution(object):
    def superPow(self, a, b):
        t = 0
        for i in b:
            t *= 10
            t += i
        return (a**t) % 1337
    def superPow(self, a, b):
        if not a:
            return 0
        mod = 1337
        a, res = a % mod, 1
        while b:
            res = (res*(a**b.pop()) % mod)%mod
            a = (a**10) % mod
        return res
