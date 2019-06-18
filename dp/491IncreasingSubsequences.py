from collections import deque


class Solution(object):
    def findSubsequences(self, nums):
        visited, res, size = {}, [], len(nums)
        stack = [[index] for index in xrange(0, size)]
        stack.reverse()
        while stack:
            path = stack.pop()
            last_index = path[-1]
            strg = ' '.join([str(nums[index]) for index in path])
            for i in xrange(last_index+1, size):
                if nums[last_index] <= nums[i]:
                    new_str = strg+' '+str(nums[i])
                    if new_str not in visited:
                        visited[new_str] = True
                        new_path = path[:]
                        new_path.append(i)
                        res.append(new_path)
                        stack.append(new_path)
        return [[nums[index] for index in indexes] for indexes in res]
    def findSubsequencesWithoutDeque(self, nums):
        visited, res, size = {}, [], len(nums)
        stack = deque([[index] for index in xrange(0, size)])
        while stack:
            path = stack.popleft()
            last_index = path[-1]
            strg = ' '.join([str(nums[index]) for index in path])
            for i in xrange(last_index+1, size):
                if nums[last_index] <= nums[i]:
                    new_str = strg+' '+str(nums[i])
                    if new_str not in visited:
                        visited[new_str] = True
                        new_path = path[:]
                        new_path.append(i)
                        res.append(new_path)
                        stack.append(new_path)
        return [[nums[index] for index in indexes] for indexes in res]
