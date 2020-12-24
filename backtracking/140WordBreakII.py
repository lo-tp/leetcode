from re import sub
from collections import Counter

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
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        data, sz, sizes = {}, len(s), set(len(w) for w in wordDict)
        data[sz] = ['']
        stack = [(0, False)]
        te, t = set(s), set()
        for w in wordDict:
            t |= set(w)
        if te & t == te:
            while stack:
                index, visited = stack.pop()
                if visited:
                    data[index] = []
                    for next_index in [index+i for i in sizes if index+i <= sz]:
                        w = s[index:next_index]
                        if w in wordDict:
                            for surfix in data[next_index]:
                                data[index].append('{} {}'.format(w, surfix))
                else:
                    if index not in data:
                        stack.append((index, True))
                        stack.extend([(next_index, False)
                                      for next_index in [j+index for j in sizes] if next_index <= sz if next_index not in data])
        else:
            data[0] = []
        return [sub(' $', '', i) for i in data[0]]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tmp = set("".join(wordDict))
        if any([i not in tmp for i in s]):
            return []
        dp = [[""], [s[0]]*(s[0] in wordDict)]
        for i in range(1, len(s)):
            dp.append(sum([[f"{k} {s[j: i+1]}" if k else s[j: i+1] for k in dp[j]] for j in range(i+1) if s[j: i+1] in wordDict and dp[j]], []))
        return dp[-1]
