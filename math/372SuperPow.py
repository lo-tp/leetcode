class Solution(object):
    def superPow(self, a, b):
        t = 0
        for i in b:
            t *= 10
            t += i
        return (a**t) % 1337
