class Preprocessor:
    def __init__(self):
        # Set of stopwords
        self.stopwords = {
            "the", "is", "are", "and", "or", "not", "to", "of", "in", "on",
            "for", "with", "that", "this", "an", "a", "as", "at", "by", "from",
            "it", "be", "has", "have", "was", "were", "will", "would", "can",
            "could", "should", "but", "about", "into", "over", "after", "before"
        }
    def to_lower_case(self, s: str) -> str:
        """Convert a string to lowercase."""
        return s.lower()

    def tokenize(self, s: str) -> list[str]:
        """Split a string into alphanumeric tokens."""
        tokens = []
        word = ""
        for c in s:
            if c.isalnum():
                word += c
            elif word:
                tokens.append(word)
                word = ""
        if word:
            tokens.append(word)
        return tokens

    def is_stop_word(self, word: str) -> bool:
        """Check if a word is a stopword."""
        return word in self.stopwords

    def preprocess_email(self, text: str) -> list[str]:
        """Preprocess email: lowercase, tokenize, and remove stopwords."""
        lowered = self.to_lower_case(text)
        tokens = self.tokenize(lowered)
        return [w for w in tokens if not self.is_stop_word(w)]
