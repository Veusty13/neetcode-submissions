class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        n: int = len(s)
        l: int = 0
        r: int = 1
        slider: set = set()
        slider.add(s[l])
        longest_seq: int = 1
        while r <= n - 1:
            if s[r] not in slider:
                slider.add(s[r])
                r += 1
            else:
                l += 1
                r = l + 1
                slider = set()
                slider.add(s[l])
            longest_seq = max(longest_seq, len(slider))
        return longest_seq


