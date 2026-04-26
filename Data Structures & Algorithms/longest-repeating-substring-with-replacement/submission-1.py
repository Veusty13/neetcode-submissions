class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        r = 0
        l = 0
        n = len(s)
        max_freq = 0
        output = 0
        while r <= n - 1 :
            if s[r] in freq_map:
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            max_freq = max(max_freq, freq_map[s[r]])
            while r - l + 1 - max_freq > k:
                freq_map[s[l]] -= 1
                max_freq = max(max_freq, freq_map[s[l]])
                l += 1
            output = max(output, r - l + 1)
            r += 1
        return output
                

            

