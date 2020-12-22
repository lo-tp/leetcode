from sys import maxsize


class Solution(object):
    def superEggDrop(self, K, N):
        dp = [[maxsize for _ in range(0, N+1)] for _ in range(0, K+1)]
        stack = [(K, N, False)]
        while stack:
            i, j, flag = stack.pop()
            if flag:
                for t in range(1, j+1):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][t-1], dp[i][j-t])+1)
            elif dp[i][j] == maxsize:
                if i == 1:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = 0
                else:
                    stack.append((i, j, True))
                    for t in range(1, j+1):
                        stack.extend([(i-1, t-1, False), (i, j-t, False)])
        return dp[K][N]
