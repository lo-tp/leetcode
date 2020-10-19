from sys import maxint


class Solution(object):
    def connectTwoGroups(self, cost):
        v_sz, h_sz = len(cost), len(cost[0])
        binary_numbers = [1 << i for i in range(0, h_sz)]
        max_state = 1 << h_sz
        tmp = [maxint]*max_state
        tmp[0] = 0
        for v in range(0, v_sz):
            dp = [maxint]*max_state
            for state in range(0, max_state):
                for index in range(0, h_sz):
                    next_state = state | (1 << index)
                    dp[next_state] = min(
                        dp[next_state], dp[state]+cost[v][index], tmp[state]+cost[v][index])
            dp, tmp = tmp, dp
        return tmp[-1]
    def connectTwoGroups(self, cost):
        sz1, sz2 = len(cost), len(cost[0])
        max_state, binary_numbers = 1 << sz2, [
            1 << i for i in range(0, sz2)]
        tmp = [maxint]*max_state
        tmp[0] = 0
        for v in range(0, sz1):
            dp = [maxint]*max_state
            for state in range(0, max_state):
                for j, binary_number in enumerate(binary_numbers):
                    next_state = state | binary_number
                    dp[next_state] = min(dp[next_state],
                                         tmp[state]+cost[v][j], dp[state]+cost[v][j])
            tmp = dp
        return tmp[-1]
