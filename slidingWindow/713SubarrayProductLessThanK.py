class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = l = 0
        total = 1
        for r in range(0, len(nums)):
            total *= nums[r]
            while total >= k and l <= r:
                total /= nums[l]
                l += 1
            if total < k:
                res += (r - l) + 1
        return res
