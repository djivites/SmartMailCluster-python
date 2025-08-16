class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.email_ids = set()


class Trie:
    def __init__(self, ds):
        """
        ds: DisjointSet instance
        """
        self.root = TrieNode()
        self.ds = ds

    def insert_with_prefix_union(self, s: str, email_id: int):
        """
        Insert a string into the Trie, and for every word prefix found,
        union the email_id with existing ones in that node.
        """
        node = self.root
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            # If space or end of string, process union
            if ch == ' ' or i == n - 1:
                for other_id in node.email_ids:
                    self.ds.union_by_rank(other_id, email_id)

                node.email_ids.add(email_id)
                node = self.root  # Reset for next word

    def exists_prefix(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
