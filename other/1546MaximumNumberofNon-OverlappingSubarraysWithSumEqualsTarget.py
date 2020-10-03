from collections import defaultdict


class Solution(object):
    def maxNonOverlapping(self, nums, target):
        data, t, te = [], 0, defaultdict(lambda: [])
        for index, num in enumerate(nums):
            t += num
            if t == target:
                data.append((0, index))
            if t-target in te:
                for i in te[t-target]:
                    data.append((i+1, index))
            te[t].append(index)
        data.sort()
        sz, t, te, tem = len(data), [], [[0, []] for _ in data], {}
        for i in range(0, sz):
            t.append(te[i])
            start, end = data[i]
            tem[data[i]] = i
            for j in range(i+1, sz):
                if data[j][0] <= end:
                    te[i][0] += 1
                    te[i][1].append(data[j])
                    te[j][0] += 1
                    te[j][1].append(data[i])
        t.sort()
        while t and t[-1][0] > 0:
            # print('---')
            # print(t)
            # print(te)
            _, overlapped = t.pop()
            for i in overlapped:
                te[tem[i]][0] -= 1
            t.sort()
        return len(t)
