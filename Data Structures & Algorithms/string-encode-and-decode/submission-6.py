class Solution:
    def encode(self, strs: List[str]) -> str:
        sep = str("{size}#")
        encoded = ""
        for s in strs:
            size = len(s)
            encoded += (sep.format(size=size) + s)
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        r = 0
        size_as_string = ""
        n = len(s)
        decoded = []
        while r < n:
            while s[r] != "#":
                size_as_string += s[r]
                r += 1
            size = int(size_as_string)
            decoded.append(s[r + 1: r + size + 1])
            size_as_string = ""
            r = r + size + 1
        return decoded

