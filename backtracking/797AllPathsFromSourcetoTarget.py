class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        sz = len(G)
        dp = [None for _ in range(0, sz)]
        dp[-1] = [[sz-1]]
        stack = [(0, False)]
        while stack:
            t, flag = stack.pop()
            if dp[t] == None:
                if flag:
                    dp[t] = []
                    for i in G[t]:
                        dp[t].extend([[t]+j for j in dp[i]])
                else:
                    stack.append((t, True))
                    stack.extend([(j, False) for j in G[t]])
        return dp[0]
