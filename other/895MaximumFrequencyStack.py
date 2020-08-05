from collections import defaultdict


class FreqStackWA():
    def __init__(self):
        self.max, self.freq, self.data = 0, defaultdict(lambda: 0), []

    def push(self, t):
        self.freq[t] += 1
        self.max = max(self.freq[t], self.max)
        if self.max < len(self.data):
            self.data.append([])
        self.data[self.freq[t]].append(t)

    def pop(self):
        res = self.data[self.max].pop()
        self.freq[res] -= 1
        if not self.data[self.max]:
            self.max -= 1
        return res

class FreqStack():
    def __init__(self):
        self.max, self.freq, self.data = 0, defaultdict(lambda: 0), []

    def push(self, t):
        self.freq[t] += 1
        self.max = max(self.freq[t], self.max)
        if self.max < len(self.data):
            self.data.append([])
        self.data[self.freq[t]].append(t)

    def pop(self):
        res = self.data[self.max].pop()
        self.freq[res] -= 1
        if not self.data[self.max]:
            self.max -= 1
        return res
