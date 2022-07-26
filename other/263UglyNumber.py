class Solution:
    def isUgly(self, n: int) -> bool:
        if n:
            for f in [2, 3, 5]:
                while not n % f:
                    n /= f
                    print(n)
            return n == 1
        return True
