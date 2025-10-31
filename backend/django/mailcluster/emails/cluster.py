from collections import defaultdict
from .trie import Trie
from .preprocessor import Preprocessor
from .disjoint_set import DisjointSet
from .models import Email

class Cluster:
    def __init__(self, threshold=5):
        """
        threshold: minimum number of shared words to consider two emails in same cluster
        """
        self.threshold = threshold

    def cluster_emails(self, graph):
        """Cluster emails using Trie + DSU with a threshold."""
        all_emails = Email.objects.all()
        if not all_emails:
            print("No emails to cluster.")
            return {}

        preproc = Preprocessor()
        trie = Trie()
        dsu = DisjointSet(10000)  # assume max 10k emails

        # Insert all tokens into the trie
        for e in all_emails:
            content = f"{e.subject} {e.body}"
            tokens = preproc.preprocess_email(content)
            for token in tokens:
                trie.insert_word(token, e.email_id)

        # Count shared words between email pairs
        shared_counts = defaultdict(lambda: defaultdict(int))
        self._count_shared_words(trie.get_root(), shared_counts)

        # Union emails only if shared words >= threshold
        for email1, neighbors in shared_counts.items():
            for email2, count in neighbors.items():
                if count >= self.threshold:
                    if dsu.find_upar(email1) != dsu.find_upar(email2):
                        dsu.union_by_rank(email1, email2)

        # Build clusters
        clusters = defaultdict(list)
        for e in all_emails:
            root = dsu.find_upar(e.email_id)
            clusters[root].append(e.email_id)

        return clusters

    def _count_shared_words(self, node, shared_counts):
        """Traverse Trie and count how many words each email pair shares."""
        if not node:
            return

        emails = node.emailids
        n = len(emails)
        if n > 1:
            # Increment shared count for every pair of emails at this node
            for i in range(n):
                for j in range(i+1, n):
                    shared_counts[emails[i]][emails[j]] += 1
                    shared_counts[emails[j]][emails[i]] += 1  # symmetric

        # Recurse for children
        for child in node.next.values():
            self._count_shared_words(child, shared_counts)
