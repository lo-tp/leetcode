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
                    # print(index, seen)
                    if flag:
                        for j in graph[index]:
                            if res[j] == 0:
                                res[i] = 0
                                partialResult = 0
                        seen.remove(index)
                    elif index in seen:
                        res[index] = 0
                        partialResult = 0
                        break
                    elif res[index] == -1:
                        seen.add(index)
                        stack.append((index, True))
                        stack.extend((j, False) for j in graph[index])
                res[i] = partialResult
        return [i for i in range(0, sz) if res[i]]

