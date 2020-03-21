from collections import defaultdict
from sys import maxint
from heapq import heappop, heappush


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        step_to_buses, res = defaultdict(lambda: set()), maxint
        for index, route in enumerate(routes):
            for step in route:
                step_to_buses[step].add(index)

        for s in step_to_buses[S]:
            for t in step_to_buses[T]:
                dis, seen = [(1, s)], set([s])
                while dis:
                    val, bus = heappop(dis)
                    if bus == t:
                        res = min(val, res)
                        break
                    if val < res:
                        for step in routes[bus]:
                            for next_bus in step_to_buses[step]:
                                if next_bus not in seen:
                                    heappush(dis, (val+1, next_bus))
                                    seen.add(next_bus)
        return -1 if res == maxint else res
