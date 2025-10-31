# backend/src/trie.py

class TrieNode:
    def __init__(self):
        self.next = {}            # dict: char -> TrieNode
        self.emailids = []        # list of email IDs
        self.end = False          # word end marker

    def put(self, ch: str, node: "TrieNode"):
        """Insert a child node for character ch"""
        self.next[ch] = node

    def get(self, ch: str):
        """Get the child node for character ch (or None)"""
        return self.next.get(ch)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str, emailid: int):
        """Insert a word into the Trie, associating it with an email ID"""
        node = self.root
        for c in word:
            if c not in node.next:
                node.put(c, TrieNode())
            node = node.get(c)

        node.end = True
        # Prevent duplicate consecutive email IDs
        if not node.emailids or node.emailids[-1] != emailid:
            node.emailids.append(emailid)

    def get_root(self) -> TrieNode:
        return self.root
