class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        target = sorted(set(s))
        sz = len(target)
        seen = []
        stack = [(i, -1, False) for i in range(len(target) - 1, -1, -1)]
        while stack:
            index, startIndex, flag = stack.pop()
            if flag:
                if len(seen) == sz:
                    return "".join(seen)
                target[index] = seen.pop()
            else:
                curIndex = s.find(target[index], startIndex + 1)
                if curIndex != -1:
                    stack.append((index, startIndex, True))
                    seen.append(target[index])
                    target[index] = ""
                    stack.extend(
                        [
                            (i, curIndex, False)
                            for i in range(sz - 1, -1, -1)
                            if target[i]
                        ]
                    )

