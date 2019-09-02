class Prie:
    def __init__(self):
        self.children = [None]*26

    def add(self, str):
        node = self
        for letter in str[::-1]:
            index = ord(letter)-97
            if not node.children[index]:
                node.children[index] = Prie()
            node = node.children[index]

    def get_length(self):
        deepth, stack, res = 0, [_ for _ in self.children if _], 0
        while stack:
            tmp = []
            deepth += 1
            for child in stack:
                children = [_ for _ in child.children if _]
                if children:
                    tmp.extend(children)
                else:
                    res += deepth+1
            stack = tmp
        return res


class Solution(object):
    def minimumLengthEncoding(self, words):
        prie = Prie()
        for word in words:
            prie.add(word)
        return prie.get_length()

