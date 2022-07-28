class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = [0] * 26
        stack = []
        indexMapping = {}
        seen = set()
        for i in range(0, 26):
            indexMapping["abcdefghijklmnopqrstuvwxyz"[i]] = i
        for i in s:
            count[indexMapping[i]] += 1
        for i in s:
            if i not in seen:
                while stack and count[indexMapping[stack[-1]]] and stack[-1] >= i:
                    seen.remove(stack.pop())
                stack.append(i)
                seen.add(i)
            count[indexMapping[i]] -= 1
        return "".join(stack)
