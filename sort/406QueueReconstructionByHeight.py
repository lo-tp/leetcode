class Solution(object):
    def reconstructQueue(self, people):
        result=[]
        tem=sorted(people,key=lambda x:(-x[0],x[1]))
        for i in tem:
            w,pos=i
            result.insert(pos,i)
        return result
