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
    def heap(self, arr, compare):
        size=len(arr)
        index=(size-2)/2
        while index>=0:
            lIndex=index*2+1
            rIndex=index*2+2
            minIndex=lIndex
            if rIndex<size and compare(arr[lIndex], arr[rIndex])>0:
                minIndex=rIndex
            if minIndex<size and compare(arr[index], arr[minIndex])>0:
                tmp=arr[minIndex]
                arr[minIndex]=arr[index]
                arr[index]=tmp
            index-=1
            
    def topKFrequent1(self, nums, k):
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
        numbers=[(records[i], i) for i in numbers]
        size=len(numbers)
        if size>k:
            tmp=numbers[:k+1]
            index=k+1
            self.heap(tmp, lambda x,y:x[0]-y[0])
            while index<size:
                tmp[0]=numbers[index]
                self.heap(tmp, lambda x,y:x[0]-y[0])
                index+=1
            print tmp
            print numbers
            return [i[1] for i in tmp[1:]]
        return [i[1] for i in numbers]
s=Solution()
print s.topKFrequent([1,1,1,2,2,3],2)
