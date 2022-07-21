from typing import List, Optional

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = {}, set()
        for i in range(0, len(s) - 9):
            t = s[i : i + 10]
            if t in seen:
                res.add(t)
            seen[t] = True
        return list(res)
