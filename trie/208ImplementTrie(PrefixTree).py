class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        node = self.node
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def _traversal(self, word):
        node = self.node
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self._traversal(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self._traversal(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()

