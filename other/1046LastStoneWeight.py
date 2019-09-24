class Heap():
    def __init__(t, data):
        t.data = data
        t.size = len(t.data)
        t.sort()

    def add(t, element):
        t.data[t.size] = element
        t.size += 1
        t.sort()

    def pop(t):
        res = t.data[0]
        t.size -= 1
        t.data[0] = t.data[t.size]
        t.sort()
        return res

    def sort(t):
        if t.size > 1:
            index = (t.size-2)/2
            while index >= 0:
                l_index = index*2+1
                r_index = l_index+1
                if r_index < t.size and t.data[r_index] > t.data[l_index]:
                    l_index = r_index
                if t.data[l_index] > t.data[index]:
                    t.data[l_index], t.data[index] = t.data[index], t.data[l_index]
                index -= 1


class Solution(object):
    def lastStoneWeight(self, stones):
        heap = Heap(stones)
        while heap.size >= 2:
            tmp = heap.pop() - heap.pop()
            if tmp:
                heap.add(tmp)
        return heap.pop() if heap.size else 0


