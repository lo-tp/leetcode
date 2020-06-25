class Solution(object):
    def findBestValue(self, arr, target):
        sz = len(arr)
        t = sz
        arr.sort()
        for i in xrange(0, sz):
            if arr[i]*t >= target:
                m = target/t
                if target -t* m > (m+1)*t-target:
                    return m+1
                return m
            t -= 1
            target -= arr[i]
        return arr[-1]
    def findBestValue(self, arr, target):
        total, sz = sum(arr), len(arr)
        arr.sort()
        m, res = sz, arr[-1]
        if total > target:
            i = 0
            while target > arr[i]*m:
                target -= arr[i]
                i += 1
                m -= 1
            res = target/m
            t = res + 1
            if abs(target-t*m) < abs(target-res*m):
                res = t
        return res
