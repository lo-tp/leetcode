ffrom typing imporom typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        sz = len(nums)
        k %= sz
        l, r = 0, sz - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = k, sz - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        sz=len(nums)
        k%=sz
        if k:
            count=0
            for start in range(0,k):
                idx=start
                t=nums[idx]
                while True:
                    nxt_idx=(idx+k)%sz
                    te=nums[nxt_idx]
                    nums[nxt_idx]=t
                    t=te
                    count+=1
                    if nxt_idx==start:
                        break
                    idx=nxt_idx
                if count==sz:
                    break
