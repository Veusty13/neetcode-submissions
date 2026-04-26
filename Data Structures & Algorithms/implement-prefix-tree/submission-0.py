class PrefixTree:

    def __init__(self):
        self.voc = {}

    def insert(self, word: str) -> None:
        cur = self.voc
        i = 0
        n = len(word)
        while i < len(word):
            if word[i] not in cur:
                cur[word[i]] = {}
            cur = cur[word[i]]
            i += 1
        cur["EXISTS"] = True

    def search(self, word: str) -> bool:
        cur = self.voc
        i = 0
        n = len(word)
        while i < len(word):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
            i += 1
        if "EXISTS" in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.voc
        i = 0
        n = len(prefix)
        while i < len(prefix):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
            i += 1
        return True
