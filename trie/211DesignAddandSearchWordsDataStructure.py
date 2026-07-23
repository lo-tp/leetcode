class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.node
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def _traversal(self, word):
        stack = [(self.node, 0)]
        sz = len(word)
        while stack:
            node, idx = stack.pop()
            if word[idx] == ".":
                for n in node.children.values():
                    if idx + 1 == sz:
                        if n.end:
                            return n
                    else:
                        stack.append((n, idx + 1))
            elif word[idx] in node.children:
                nxt_node = node.children[word[idx]]
                if idx == sz - 1 :
                    if nxt_node.end:
                        return nxt_node
                else:
                    stack.append((nxt_node, idx + 1))
        return None

    def search(self, word: str) -> bool:
        node = self._traversal(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self._traversal(prefix)
        return node
