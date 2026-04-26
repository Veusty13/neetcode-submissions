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
        current_seq: List[str] = [s[l]]
        longest_seq: int = 1
        while r <= n - 1:
            if s[r] not in current_seq :
                current_seq.append(s[r])
            else:
                new_l : int = index_mapper[s[r]] + 1
                jump: int = new_l - l
                l = new_l
                current_seq = current_seq[(jump):]
                current_seq.append(s[r])
            index_mapper[s[r]] = r
            r += 1
            longest_seq = max(longest_seq, len(current_seq))
        return longest_seq


