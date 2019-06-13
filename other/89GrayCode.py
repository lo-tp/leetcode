class Solution(object):
    def grayCode(self, n):
        end_index, to_add, end = 1, 1, 2 ** n
        res = [0]*end
        while to_add < end:
            right_index, left_index = end_index, end_index-1
            while left_index >= 0:
                res[right_index] = to_add+res[left_index]
                left_index -= 1
                right_index += 1
            to_add *= 2
            end_index = right_index
        return res


S = Solution()
