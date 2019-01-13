def mg(arr):
    sz = len(arr)
    if sz > 1:
        lIndex, rIndex, m = 0, 0, sz/2
        l, r = arr[:m], arr[m:]
        index, lSz, rSz = 0, len(l), len(r)
        mg(l)
        mg(r)
        while lIndex < lSz and rIndex < rSz:
            if l[lIndex] < r[rIndex]:
                arr[index] = r[rIndex]
                rIndex += 1
            else:
                arr[index] = l[lIndex]
                lIndex += 1
            index += 1
        while lIndex < lSz:
            arr[index] = l[lIndex]
            index += 1
            lIndex += 1
        while rIndex < rSz:
            arr[index] = r[rIndex]
            index += 1
            rIndex += 1


class Solution(object):
    def leastInterval1(self, tasks, n):
        offset, data = ord('A'), [0]*26
        for i in tasks:
            data[ord(i)-ord('A')] += 1
        mg(data)
        columnSz = data[0]-1
        idleSlots = columnSz*n
        for i in data[1:]:
            idleSlots -= min(columnSz, i)
        return idleSlots+len(tasks) if idleSlots > 0 else len(tasks)
    def leastInterval(self, tasks, n):
        offset, data = ord('A'), [0]*26
        for i in tasks:
            data[ord(i)-ord('A')] += 1
        mg(data)
        res = 0
        while data[0]:
            index = 0
            while index <= n:
                if index < 25 and data[index]:
                    data[index] -= 1
                elif data[0] == 0:
                    break
                res += 1
                index += 1
            mg(data)
        return res


s = Solution()
print s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
print s.leastInterval([], 2)
print s.leastInterval(['A'], 2)
