def makeGraph(data):
    size, tmp = len(data), {}
    res = [[] for i in xrange(0, size)]
    for index, word in enumerate(data):
        tmp[word] = index

    for index, word in enumerate(data):
        tem = list(word)
        for i in xrange(0, len(tem)):
            temp = tem[i]
            tem[i] = ''
            potential_pre = ''.join(tem)
            if potential_pre in tmp:
                res[tmp[potential_pre]].append(index)
            tem[i] = temp
    return res


class Solution(object):
    def longestStrChain(self, words):
        graph, res, stack = makeGraph(words), 0, [(
            index, 1) for index in xrange(0, len(words))]
        while stack:
            index, length = stack.pop()
            res = max(length, res)
            length += 1
            for next_index in graph[index]:
                stack.append((next_index, length))
        return res
