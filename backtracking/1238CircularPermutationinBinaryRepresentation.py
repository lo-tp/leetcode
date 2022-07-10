from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        sz, bitMask = (1 << n), [1 << i for i in range(0, n)]
        seen = set()
        stack = [(start, False)]
        while stack:
            num, flag = stack.pop()
            if flag:
                if len(res) == sz :
                    if [
                        i for i in range(0, n) if res[0] ^ res[-1] == bitMask[i]
                    ]:
                        return res
                seen.remove(num)
                res.pop()
            else:
                seen.add(num)
                stack.append((num, True))
                res.append(num)
                if len(res) < sz:
                    for bit in bitMask:
                        t = num ^ bit
                        if t not in seen:
                            stack.append((t, False))

        return []
