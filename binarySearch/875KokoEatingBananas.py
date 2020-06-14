def qs(arr, start, end):
    m, s, e = arr[start+(end-start)/2], start, end
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    if s < end:
        qs(arr, s, end)
    if start < e:
        qs(arr, start, e)


class Solution(object):
    def minEatingSpeed(self, piles, H):
        # piles.sort()
        qs(piles, 0, len(piles)-1)
        l, r, res = 1, piles[-1], piles[-1]
        while l <= r:
            t, m = 0, (l+r)/2
            for i in piles:
                t += i/m
                t += 1 if i % m else 0
                if t > H:
                    break
            if t <= H:
                res = m
                r = m-1
            else:
                l = m+1
        return res


