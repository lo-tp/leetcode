class Solution(object):
    def wordBreak(self, s, wordDict):
        data, current, stack, res, sz = set(wordDict), [], [], [], len(s)
        stack = [(0, i, False) for i in range(1, sz+1)]
        while stack:
            start_index, end_index, visited = stack.pop()
            if visited:
                if end_index == sz:
                    res.append(' '.join(current))
                current.pop()
            else:
                word = s[start_index:end_index]
                if word in data:
                    stack.append((start_index, end_index, True))
                    current.append(word)
                    stack.extend([(end_index, i, False)
                                  for i in range(end_index+1, sz+1)])
        return res
