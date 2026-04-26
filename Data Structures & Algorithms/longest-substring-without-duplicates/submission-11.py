class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        n: int = len(s)
        l: int = 0
        r: int = 1
        index_mapper: Dict = {
            s[l] :l
        }
        longest_seq: int = 1
        while r <= n - 1:
            if s[r] not in index_mapper: 
                index_mapper[s[r]] = r
                r += 1
            elif s[r] in index_mapper:
                l = max(index_mapper[s[r]] + 1, l)
                index_mapper[s[r]] = r 
                r += 1
            longest_seq = max(longest_seq, r - l)
        return longest_seq


