class Solution(object):
    def calculate(self, arr):
        if len(arr)==len(self.nums):
            self.data.append(arr)
        for i in self.nums:
            if not i in arr:
                tmp=arr[0:]
                tmp.append(i)
                self.calculate(tmp)
    def permute(self, nums):
        self.nums=nums
        self.data=[]
        self.calculate([])
        return self.data

    def permute(self, n):
        res, sz, seen, stack,data = [], len(n),  set(
        ), [(i, False) for i in xrange(0, len(n))],[]
        data=[]
        while stack:
            index, flag = stack.pop()
            if index == sz:
                continue
            if flag:
                seen.remove(index)
                data.pop()
                continue
            data.append(n[index])
            if len(data) == sz:
                res.append(data[:])
            seen.add(index)
            stack.append((index, True))
            stack.extend([(i, False)
                          for i in xrange(0, sz) if i not in seen])
        return res
s=Solution()
print s.permute([1,2,3])
