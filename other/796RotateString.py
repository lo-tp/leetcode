class Solution(object):
    def rotateString(self, A, B):
        size = len(A)
        if size:
            if size==len(B):
                for i in xrange(0, size):
                    flag, i_A, i_B = True, i, 0
                    while flag and i_A < size:
                        if A[i_A] != B[i_B]:
                            flag = False
                        i_A += 1
                        i_B += 1
                    i_A = 0
                    while flag and i_B < size:
                        if A[i_A] != B[i_B]:
                            flag = False
                        i_A += 1
                        i_B += 1
                    if flag:
                        return True
            return False
        elif not B:
            return False
        else:
            return True


