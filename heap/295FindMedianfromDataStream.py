import heapq

class MedianFinder:

    def __adjust__(self):
        while len(self.right_heap)>len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        while len(self.right_heap)<len(self.left_heap)-1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))


    def __init__(self):
        self.left_heap=[]
        self.right_heap=[]
        

    def addNum(self, num: int) -> None:
        if not self.left_heap and not self.right_heap:
            self.left_heap.append(-num)
        elif num<-self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)
        self.__adjust__()


    def findMedian(self) -> float:
        if len(self.left_heap)>len(self.right_heap):
            return -self.left_heap[0]
        return -self.left_heap[0]+(self.right_heap[0]+self.left_heap[0])/2
