from sys import maxint
from collections import defaultdict


def makeGraph(data):
    tmp, word_sz, sz = defaultdict(lambda: []), len(data[0]), len(data)
    res = [[]for i in xrange(0, sz)]
    for outter_index, i in enumerate(data):
        word = list(i)
        for index in xrange(0, word_sz):
            tem = word[index]
            word[index] = ' '
            tmp[''.join(word)].append(outter_index)
            word[index] = tem

    for outter_index, i in enumerate(data):
        word = list(i)
        for index in xrange(0, word_sz):
            tem = word[index]
            word[index] = ' '
            res[outter_index].extend(tmp[''.join(word)])
            word[index] = tem
        res[outter_index] = list(set(res[outter_index]))
    return res



class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        if endWord in wordList:
            wordList.append(beginWord)
            wordList = list(set(wordList))
            stack = [(wordList.index(beginWord), [])]
            end_index, graph = wordList.index(endWord), makeGraph(wordList)
            visited = [False] * len(wordList)
            while stack:
                tmp = []
                while stack:
                    index, path = stack.pop()
                    new_path = path[:]
                    new_path.append(index)
                    visited[index] = True
                    if index == end_index:
                        res.append(new_path)
                    else:
                        for child_index in [i for i in graph[index] if not visited[i]]:
                            tmp.append((child_index, new_path))
                if not res:
                    stack = tmp
        return [[wordList[index] for index in indexes] for indexes in res]
