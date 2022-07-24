class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        maxPts += 1
        total, stack = 0, [(i, False) for i in range(1, maxPts)]
        totalGame = goodGame = 0
        pathLen = 0
        while stack:
            p, flag = stack.pop()
            if flag:
                total -= p
                pathLen -= 1
            else:
                total += p
                stack.append((p, True))
                pathLen += 1
                if total >= k:
                    prob = (1 / (maxPts - 1)) ** pathLen
                    totalGame += prob
                    if total <= n:
                        goodGame += prob
                else:
                    stack.extend([(i, False) for i in range(1, maxPts)])
