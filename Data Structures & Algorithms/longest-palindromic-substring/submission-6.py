class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            n = len(s)
            if n == 0:
                return False
            if n == 1:
                return True
            else :
                l = 0
                r = n - 1
                while l < r :
                    if s[l] != s[r] :
                        return False
                    l += 1
                    r -= 1
                return True
        memo = {}
        def dfs(s):
            if is_palindrome(s):
                return (len(s), s)
            if s not in memo:
                memo[s] = max(dfs(s[1:]), dfs(s[:-1]))
            return memo[s]
        return dfs(s)[1]
            