class Solution(object):
    def hammingDistance(self, x, y):
        tem = 1
        i = []
        for k in range(31):
            i.append(tem)
            tem*=2
        i.reverse()
        a = [0]*31
        b = [0]*31
        index = 0;
        for k in i:
            if x >= k:
                a[index]=1
                x-=k
            if y >= k:
                b[index]=1
                y-=k
            index+=1
        count=0
        for k in range(31):
            if a[k]!=b[k]:
                count+=1
        return count

soluction = Solution()
print soluction.hammingDistance(9,7)
