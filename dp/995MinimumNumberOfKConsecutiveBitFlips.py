from collections import deque


class Solution(object):
    def minKBitFlips(self, A, K):
        sz, res, t = len(A), 0, 0
        for i, x in A:
            if not ((t % 2) ^ (x & 1)):
                te = i+K-1
                if te >= sz:
                    return -1
                t += 1
                res += 1
                A[te] += 2
            if x > 1:
                A[i] -= 2
                t -= 1
        return res

    def minKBitFlips(self, A, K):
        sz, count, res = len(A), 0, 0
        for i, j in enumerate(A):
            if not ((count % 2) ^ (j & 1)):
                if i+K > sz:
                    return -1
                res += 1
                count += 1
                A[i+K-1] += 2
            if A[i] > 1:
                A[i] -= 2
                count -= 1
        return res

    def minKBitFlipsWithKSpace(self, A, K):
        data, res = deque(), 0
        for i, j in enumerate(A):
            if data and data[0] == i:
                data.popleft()
            if not ((len(data) % 2) ^ j):
                if i+K > len(A):
                    return -1
                res += 1
                data.append(i+K)
        return res

    def minKBitFlipsMLE(self, A, K):
        seen, step, t = set(), 0, [str(i) for i in A]
        target, sz, stack = ''.join(['1' for _ in A]), len(A), [(0, t)]
        while stack:
            tmp = []
            for i, arr in stack:
                temp = ''.join(arr)
                if temp == target:
                    return step
                if temp in seen:
                    continue
                seen.add(temp)
                for j in xrange(i, sz-K+1):
                    te = arr[:]
                    for k in xrange(j, j+K):
                        te[k] = '1' if te[k] == '0' else '0'
                        tmp.append((k+1, te))
            stack = tmp
            step += 1
        return -1

    def minKBitFlipsTLE(self, A, K):
        step, sz = 0, len(A)
        for i in xrange(0, sz):
            if not A[i]:
                if i+K > sz:
                    return -1
                step += 1
                for j in xrange(i, i+K):
                    A[j] = 0 if A[j] else 1
        return step

