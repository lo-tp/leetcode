class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        prev1, prev2 = 1, 2
        for i in xrange(2, n):
            prev1, prev2 = prev2, prev1+prev2
        return prev2
    def find_ways(self, n:int):
        if not n in self.cache:
            self.cache[n]=self.find_ways(n-1)+self.cache[n]+=self.find_ways(n-2)
        return self.cache[n]
        
        

    def climbStairs_dp_recursive(self, n: int) -> int:
        self.cache={}
        self.cache[1]=1
        self.cache[0]=1
        self.cache[-1]=1
        return self.find_ways(n)

