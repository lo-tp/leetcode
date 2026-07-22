class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                r = mid - 1
            else:
                l = mid + 1
        return l
