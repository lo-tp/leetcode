def help(n):
    t = 0
    while n:
        m = n % 10
        t += m**2
        n /= 10
    return t


class Solution(object):
    def isHappy(self, n):
        slow = fast = n
        while True:
            t = help(fast)
            if t == 1:
                return True
            fast = help(t)
            if fast == 1:
                return True
            slow = help(slow)
            if slow == fast:
                break
        return False


    def isHappy(self, n: int) -> bool:
        seen = set()
        while not n in seen and n != 1:
            seen.add(n)
            t = 0
            while n:
                t += (n % 10) ** 2
                n //= 10
            n = t
        return n == 1
