class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [char.lower() for char in s if char.isalnum()]
        n = len(clean_s)
        for i in range(n):
            if i != n - 1 - i:
                if clean_s[i] != clean_s[n-1-i]:
                    return False
            else :
                break
        return True