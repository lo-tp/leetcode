class Solution(object):
    def longestAwesome(self, s):
        res, data, binary_nums = 0, [-2]*(2**10), [2**i for i in range(0, 10)]
        state, ord_0, data[0] = 0, ord('0'), -1
        for index, i in enumerate(s):
            m = ord(i)-ord_0
            state ^= binary_nums[m]
            if data[state] == -2:
                data[state] = index
            if not state:
                res = max(res, index+1)
            else:
                for j in binary_nums:
                    tmp = state ^ j
                    if data[tmp] != -2:
                        res = max(res, index-data[tmp])
        return res
