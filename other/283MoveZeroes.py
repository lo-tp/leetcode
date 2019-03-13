class Heap():
    def __init__(self):
        self.data = []

    def push(self, n):
        self.data.append(n)
        self.sort()

    def sort(self):
        sz = len(self.data)
        index = (sz-2)/2
        while index >= 0:
            minIndex = index*2+1
            rightIndex = minIndex+1
            if rightIndex < sz and self.data[rightIndex] < self.data[minIndex]:
                minIndex = rightIndex
            if self.data[minIndex] < self.data[index]:
                self.data[minIndex], self.data[index] = self.data[index], self.data[minIndex]
            index -= 1

    def popAndReplace(self, n):
        res = self.data[0]
        self.data[0] = n
        self.sort()
        return res

    def sz(self):
        return len(self.data)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        l=len(nums)-1
        while i<l:
            while i<l and nums[i]!=0:
                i+=1
            k=i+1
            while k<=l and nums[k]==0:
                k+=1
            if i<l and k<=l:
                nums[i]=nums[i]^nums[k]
                nums[k]=nums[i]^nums[k]
                nums[i]=nums[i]^nums[k]
            i+=1
    def moveZeroesWithHeap(self, nums):
        hp = Heap()
        for i in xrange(0, len(nums)):
            if nums[i]:
                if hp.sz():
                    tmp = hp.popAndReplace(i)
                    nums[tmp], nums[i] = nums[i], nums[tmp]
            else:
                hp.push(i)
