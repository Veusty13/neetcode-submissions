class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        l = 0
        r = 1
        indexes = defaultdict()
        indexes[s[l]] = l
        max_len = 1
        while r <= n-1:
            if s[r] in indexes and indexes[s[r]] >= l:
                l = indexes[s[r]] + 1
                indexes[s[r]] = r
                r += 1
            else:
                max_len = max(max_len, r - l + 1)
                indexes[s[r]] = r
                r += 1
        return max_len
            


