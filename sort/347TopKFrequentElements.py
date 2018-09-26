def heapify(nums, compare):
    size=len(nums)
    index=(size-2)/2
    while index>=0:
        minIndex=index*2+2
        leftIndex=minIndex-1
        if minIndex>=size or compare(nums[leftIndex],nums[minIndex])<0:
            minIndex=leftIndex
        if compare(nums[index],nums[minIndex])>0:
            tmp=nums[index]
            nums[index]=nums[minIndex]
            nums[minIndex]=tmp
        index-=1

class Solution(object):
    def mg(self, numbers):
        size=len(numbers)
        if size>1:
            m=size/2
            r=numbers[:m]
            l=numbers[m:]
            rSize=len(r)
            lSize=len(l)
            rIndex=0
            lIndex=0
            self.mg(r)
            self.mg(l)
            index=0
            while rIndex<rSize and lIndex<lSize:
                if r[rIndex][0]>l[lIndex][0]:
                    numbers[index]=r[rIndex]
                    rIndex+=1
                else:
                    numbers[index]=l[lIndex]
                    lIndex+=1
                index+=1
            while rIndex<rSize:
                numbers[index]=r[rIndex]
                index+=1
                rIndex+=1
            while lIndex<lSize:
                numbers[index]=l[lIndex]
                index+=1
                lIndex+=1



    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        records=dict()
        numbers=[]
        for i in nums:
            if i in records:
                records[i]+=1
            else:
                records[i]=1
                numbers.append(i)
        records=[ (records[i], i) for i in numbers]
        self.mg(records)
        return [i[1] for i in records[0:k]]
    def topKFrequent1(self, nums, k):
        records=dict()
        result=[]
        for i in nums:
            if i in records:
                records[i]+=1
            else:
                result.append(i)
                records[i]=1
        size=len(result)
        if size!=k:
            result=[(i,records[i]) for i in result]
            leftPart=result[:k]
            rightPart=result[k:]
            heapify(leftPart, lambda x,y:x[1]-y[1])
            for i in rightPart:
                if i[1]>leftPart[0][1]:
                    leftPart[0]=i
                    heapify(leftPart, lambda x,y:x[1]-y[1])
            result=[ i[0] for i in leftPart]
        return result

s=Solution()
print s.topKFrequent([1,1,1,2,2,3],2)
