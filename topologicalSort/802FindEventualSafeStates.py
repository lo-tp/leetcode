class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        sz = len(graph)
        res = [-1] * sz
        for i in range(0, sz):
            if res[i] == -1:
                seen = set()
                stack = [(i, False)]
                partialResult = 1
                while stack:
                    index, flag = stack.pop()
                    if flag:
                        if reduce(lambda accu, x: accu and res[x], graph[index], True):
                            res[index] = 1
                            seen.remove(index)
                        else:
                            partialResult = 0
                            break
                    elif index in seen:
                        partialResult = 0
                        break
                    elif res[index] == -1:
                        seen.add(index)
                        stack.append((index, True))
                        stack.extend([(i, False) for i in graph[index]])
                res[i] = partialResult
                for i in seen:
                    res[i] = partialResult
        return [i for i in range(0, sz) if res[i]]
