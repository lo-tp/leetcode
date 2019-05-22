class Heap():
    def __init__(self, k):
        self.size = 0
        self.data = [None]*k

    def sort(self):
        if self.size > 1:
            index = (self.size-2)/2
            while index >= 0:
                min_index = index*2+1
                right_index = min_index+1
                if right_index < self.size and (
                        self.data[right_index][0] < self.data[min_index][0] or (self.data[right_index][0] == self.data[min_index][0] and
                                                                                self.data[right_index][1] > self.data[min_index][1])):
                    min_index = right_index
                if self.data[min_index][0] < self.data[index][0] or (
                        self.data[min_index][0] == self.data[index][0] and
                        self.data[min_index][1] > self.data[index][1]):
                    self.data[min_index], self.data[index] = self.data[index], self.data[min_index]
                index -= 1

    def pop(self):
        ret = self.data[0]
        self.size -= 1
        if self.size >= 0:
            self.data[0] = self.data[self.size]
        return ret

    def add(self, element):
        self.data[self.size] = element
        self.size += 1


class Solution(object):
    def topKFrequent(self, words, k):
        data = {}
        heap = Heap(k)
        index = 0
        while heap.size < k:
            word = words[index]
            if word not in data:
                data[word] = [0, word, True]
                heap.add(data[word])
            else:
                data[word][0] += 1
            index += 1

        for word in words[index:]:
            if word not in data:
                data[word] = [0, word, False]
            else:
                data[word][0] += 1
            heap.sort()
            if not data[word][2] and (
                    data[word][0] > heap.data[0][0] or (
                        data[word][0] == heap.data[0][0] and data[word][1] < heap.data[0][1])):
                data[word][2] = True
                heap.data[0][2] = False
                heap.pop()
                heap.add(data[word])

        res = []
        while heap.size:
            heap.sort()
            res.append(heap.pop()[1])
        return res[::-1]


