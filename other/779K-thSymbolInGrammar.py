class Solution(object):
    def kthGrammar(self, N, K):
        t, te = 2 ** (N-1), [0, 1]
        while K > 2:
            tem = t/2
            if K > t:
                if K > 3*tem:
                    K -= 3*tem
                else:
                    K -= tem
            t = tem
