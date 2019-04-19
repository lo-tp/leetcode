def heapify(arr, sz, dict):
    if sz > 1:
        m = (sz-2)/2
        for i in xrange(m, -1, -1):
            minIndex = i*2+1
            rightIndex = minIndex+1
            if rightIndex < sz and dict[arr[rightIndex]][0] < dict[arr[minIndex]][0]:
                minIndex = rightIndex
            if dict[arr[minIndex]][0] < dict[arr[i]][0]:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]




class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        dp, dict = [], {}
        for i in xrange(0, numCourses):
            dp.append(i)
            dict[i] = [0, []]
        for (after, pre) in prerequisites:
            dict[pre][1].append(after)
            dict[after][0] += 1
        while numCourses:
            heapify(dp, numCourses, dict)
            data = dict[dp[0]]
            if data[0] == 0:
                for i in data[1]:
                    dict[i][0] -= 1
                numCourses -= 1
                dp[0], dp[numCourses] = dp[numCourses], dp[0]
            else:
                return False
        return True
