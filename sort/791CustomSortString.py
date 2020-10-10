from collections import defaultdict


class Solution(object):
    def qc(self, string, start, end):
        s, e, m = start, end, string[start+(end-start)/2]
        while s <= e:
            while self.weight[string[s]] < self.weight[m]:
                s += 1
            while self.weight[string[e]] > self.weight[m]:
                e -= 1
            if s <= e:
                string[s],  string[e] = string[e], string[s]
                s += 1
                e -= 1
        if s < end:
            self.qc(string, s, end)
        if start < e:
            self.qc(string, start, e)

    def customSortString(self, S, T):
        self.weight = defaultdict(lambda: 0)
        for index, s in enumerate(S):
            self.weight[s] = index
        t = list(T)
        self.qc(t, 0, len(t)-1)
        return ''.join(t)
def customSortString(self, S, T):
        self.weight = defaultdict(lambda: 0)
        for index, s in enumerate(S):
            self.weight[s] = index
        string = list(T)
        stack=[(0, len(string)-1)]
        while stack:
            start, end=stack.pop()
            s, e, m = start, end, string[start+(end-start)/2]
            while s <= e:
                while self.weight[string[s]] < self.weight[m]:
                    s += 1
                while self.weight[string[e]] > self.weight[m]:
                    e -= 1
                if s <= e:
                    string[s],  string[e] = string[e], string[s]
                    s += 1
                    e -= 1
            if s < end:
                stack.append((s, end))
            if start < e:
                stack.append((start, e))
        return ''.join(string)

