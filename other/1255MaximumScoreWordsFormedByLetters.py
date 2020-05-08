from collections import Counter, defaultdict
from copy import copy


class Solution(object):
    def maxScoreWords(self, words, letters, score):
        data, stack, words_count, limit = [], [(0, defaultdict(lambda:0))], [
            Counter(w).items() for w in words], Counter(letters)
        sz = len(words)

        while stack:
            index, existing_count = stack.pop()
            if index == sz:
                data.append(copy(existing_count))
            else:
                stack.append((index+1, copy(existing_count)))
                tmp = copy(existing_count)
                flag = True
                for key, val in words_count[index]:
                    tmp[key] += val
                    if tmp[key] > limit[key]:
                        flag = False
                        break
                if flag:
                    stack.append((index+1, tmp))
        ord_a, res = ord('a'), 0
        for count in data:
            tmp = 0
            for key, val in count.items():
                tmp += val*score[ord(key)-ord_a]
            res = max(tmp, res)
        return res
