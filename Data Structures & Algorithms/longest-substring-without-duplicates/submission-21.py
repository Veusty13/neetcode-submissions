class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        l = 0
        seen = set()
        seen.add(s[l])
        r = 1
        max_len = 0
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r +=1
                max_len = max(max_len, r - l)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return max_len
