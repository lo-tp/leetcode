class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix and matrix[0]:
            v, l, r = -1, 0, len(matrix)-1
            while l <= r:
                m = l+(r-l)/2
                if matrix[m][-1] < target:
                    l = m+1
                elif matrix[m][0] > target:
                    r = m-1
                else:
                    v = m
                    break
            if v != -1:
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    m = l+(r-l)/2
                    if matrix[v][m] < target:
                        l = m+1
                    elif matrix[v][m] > target:
                        r = m-1
                    else:
                        return True
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        v_sz, h_sz=len(matrix), len(matrix[0])
        l,r=0, v_sz*h_sz-1
        def getIndexes(n):
            return (n//h_sz, n%h_sz)
        while l<=r:
            mid=l+(r-l)//2
            mid_v, mid_h=getIndexes(mid)
            if matrix[mid_v][mid_h]==target:
                return True
            elif matrix[mid_v][mid_h]>target:
                r=mid-1
            else:
                l=mid+1
        return False
