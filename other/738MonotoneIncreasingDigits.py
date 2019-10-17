class Solution(object):
    def monotoneIncreasingDigits(self, N):
        data = []
        while N:
            data.append(N % 10)
            N /= 10
        size, minimum = len(data), -1
        tmp = size-1
        while tmp >= 0:
            if data[tmp] < minimum:
                data[tmp+1] -= 1
                while tmp >= 0:
                    data[tmp] = 9
                    tmp -= 1
                tmp = size-1
                minimum = -1
            else:
                minimum = data[tmp]
                tmp -= 1
        res = 0
        for i in data[::-1]:
            res = res*10+i
        return res

