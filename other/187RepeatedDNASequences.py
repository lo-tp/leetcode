from typing import List, Optional
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = {}, set()
        for i in range(0, len(s) - 9):
            t = s[i : i + 10]
            if t in seen:
                res.add(t)
            seen[t] = True
        return list(res)


    def findRepeatedDnaSequencesBetter(self, s: str) -> List[str]:
        sz = len(s)
        res = []
        if sz > 10:
            mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
            state = 0
            validNum = (1 << 20) - 1
            for i in range(0, 10):
                state <<= 2
                state |= mapping[s[i]]

            seen = defaultdict(lambda: 0)
            seen[state] += 1
            for i in range(10, sz):
                state <<= 2
                state |= mapping[s[i]]
                state &= validNum
                if seen[state] == 1:
                    res.append(s[i - 9 : i + 1])
                seen[state] += 1
        return res
