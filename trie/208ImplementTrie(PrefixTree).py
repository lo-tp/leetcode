class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        node = self.node
        for char in word:
            idx = ord(char)-ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.node
        for char in word:
            idx = ord(char)-ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for char in prefix:
            idx = ord(char)-ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True

