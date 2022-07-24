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
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [1] * (n + 1)
        totalProb = 0
        for i in range(1, n + 1):
            if i <= k:
                totalProb += dp[i - 1]
            if k + maxPts >= i > maxPts:
                totalProb -= dp[i - maxPts - 1]
            dp[i] = totalProb / (maxPts)
        return sum(dp[k:])
