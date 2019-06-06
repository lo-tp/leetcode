from sys import maxint
from collections import defaultdict, deque


def makeGraph(words):
    word_size, tmp, temp, tem = len(words[0]), [list(word)
                                                for word in words], defaultdict(set), [[] for word in words]
    for index, word in enumerate(tmp):
        for i in xrange(0, word_size):
            k = word[i]
            word[i] = '*'
            str = ''.join(word)
            word[i] = k
            temp[str].add(index)
            tem[index].append(str)

    for index in xrange(0, len(words)):
        tem[index] = set().union(*[temp[k] for k in tem[index]])
        tem[index].remove(index)
        tem[index] = list(tem[index])
    return tem


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        wordList.append(beginWord)
        list(set(wordList))
        source_index, target_index = wordList.index(
            beginWord), wordList.index(endWord)
        visited = {}
        graph = makeGraph(wordList)
        dq = deque()
        dq.append((source_index, 1))
        while dq:
            index, level = dq.popleft()
            if index == target_index:
                return level
            visited[index] = True
            for next_index in [index for index in graph[index] if index not in visited]:
                dq.append((next_index, level+1))
        return 0

def getGraphBetter(wordList):
    size, graph, data, data1 = len(wordList[0]), defaultdict(
        lambda: []), defaultdict(lambda: []), defaultdict(lambda: [])
    for i in wordList:
        word = list(i)
        for index in xrange(0, size):
            tmp = word[index]
            word[index] = ' '
            symbol = ''.join(word)
            word[index] = tmp
            data[i].append(symbol)
            data1[symbol].append(i)

    for i in wordList:
        tmp = []
        for symbol in data[i]:
            tmp.extend(data1[symbol])
        graph[i] = list(set(tmp))

    return graph


class SolutionBetter(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord in wordList:
            wordList.append(beginWord)
            graph, visited, queue = getGraph(
                wordList), {}, deque()
            queue.append((beginWord, 1))
            while queue:
                word, level = queue.popleft()
                if word == endWord:
                    return level
                if word not in visited:
                    visited[word] = True
                    level += 1
                    queue.extend([(w, level) for w in graph[word]])
        return 0
    def ladderLengthBidirectional(self, beginWord, endWord, wordList):
        res=maxint
        if endWord in wordList:
            wordList.append(beginWord)
            graph, visited_1, queue_1,visited_2, queue_2 = getGraph(
                wordList), {}, deque(),{}, deque()
            queue_1.append((beginWord, 1))
            queue_2.append((endWord, 1))
            while res==maxint and (queue_1 or queue_2):
                tmp_queue=deque()
                while queue_1:
                    word, level = queue_1.popleft()
                    if word in visited_2:
                        res=min(res, level+visited_2[word]-1)
                    if word not in visited_1:
                        visited_1[word]=level
                        level+=1
                        for w in graph[word]:
                            tmp_queue.append((w, level))
                queue_1=tmp_queue
                tmp_queue=deque()
                while queue_2:
                    word, level = queue_2.popleft()
                    if word in visited_1:
                        res=min(res, level+visited_1[word]-1)
                    if word not in visited_2:
                        visited_2[word]=level
                        level+=1
                        for w in graph[word]:
                            tmp_queue.append((w, level))
                queue_2=tmp_queue
        return 0 if res==maxint else res
