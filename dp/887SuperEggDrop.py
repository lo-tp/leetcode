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

    def superEggDrop(self, K, N):
        dp = [[maxsize for _ in range(0, N+1)] for _ in range(0, K+1)]
        calculated = set()

        stack = [(K, N, 1, N, False)]
        while stack:
            i, j, l, r, flag = stack.pop()
            if flag:
                t = int(l+(r-l)/2)
                broken, non_broken = dp[i-1][t-1], dp[i][j-t]
                if broken >= non_broken:
                    dp[i][j] = min(dp[i][j], broken+1)
                    stack.append((i, j, l, t-1, False))
                else:
                    dp[i][j] = min(dp[i][j], non_broken+1)
                    stack.append((i, j, t+1, r, False))
            elif i == 1:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = 0
            elif l <= r and (i, j) not in calculated:
                stack.append((i, j, l, r, True))
                t = int(l+(r-l)/2)
                stack.extend([(i-1, t-1, 1, t-1, False),
                              (i, j-t, 1, j-t, False)])
            else:
                calculated.add((i, j))
        return dp[K][N]

    def superEggDrop(self, K, N):
        m = 1
        dp = [1]*(K+1)
        while dp[K] < N:
            m += 1
            tmp = [m]*(K+1)
            for k in range(2, K+1):
                tmp[k] = dp[k-1]+dp[k]+1
                if tmp[k] >= N:
                    tmp[K] = tmp[k]
                    break
            dp = tmp
        return m
    def superEggDrop(self, K, N):
        if N <= 1:
            return 1
        if K == 1:
            return N
        flag, res, dp, tmp = True, 1, [1]*(K+1), [0]*(K+1)
        while flag:
            res += 1
            tmp[1] = res
            for i in range(2, K+1):
                tmp[i] = dp[i-1]+1+dp[i]
                if tmp[i] >= N:
                    flag = False
                    break
            tmp, dp = dp, tmp
        return res
