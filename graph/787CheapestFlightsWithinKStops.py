from sys import maxint


class Solution(object):
    def findCheapestPriceWithDijkstra(self, n, flights, src, dst, K):
        graph, heap, res = [[]
                            for i in xrange(0, n)], [(0, 0, src)], [maxint] * n
        for source, dest, price in flights:
            graph[source].append((dest, price))
        K += 1
        while heap:
            price, step, node = heapq.heappop(heap)
            if step <= K and price<=res[dst]:
                res[node] = min(price, res[node])
                step += 1
                for dest, p in graph[node]:
                    heapq.heappush(heap,(price+p, step, dest))
        return res[dst] if res[dst] != maxint else -1
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph, dp, res, stack = [[] for i in xrange(
            0, n)], [[maxint, maxint] for i in xrange(0, n)], maxint, [(src, 0, 0)]
        K += 1
        for source, dest, price in flights:
            graph[source].append((dest, price))
        while stack:
            node, step, price = stack.pop()
            if step <= K:
                if node == dst:
                    res = min(res, price)
                elif (step < dp[node][0] and price < res) or price < dp[node][1]:
                    dp[node][0], dp[node][1] = step, price
                    for dest, price1 in graph[node]:
                        stack.append((dest, step+1, price+price1))
        return -1 if res == maxint else res
