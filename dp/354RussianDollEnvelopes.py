from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        lis = []
        for env in envelopes:
            if not lis or env[1] > lis[-1]:
                lis.append(env[1])
            else:
                index = bisect_left(lis, env[1])
                lis[index] = env[1]
        return len(lis)

