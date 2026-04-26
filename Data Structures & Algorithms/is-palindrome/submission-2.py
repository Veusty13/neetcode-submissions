class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space_lower: str = str.lower(s.replace(" ", ""))
        cleaned_s: str = "".join([c for c in no_space_lower if c.isalnum()])
        if not cleaned_s:
            return True
        n: int = len(cleaned_s)
        remain: int = n%2
        if not remain:
            middle:int = int(n/2)
        else:
            middle:int = int(n-1/2)
        is_palindrome: bool = True
        counter = 0
        while True:
            check: bool = (cleaned_s[counter] == cleaned_s[n-1-counter])
            if check is False:
                is_palindrome = False
                break
            if counter == middle:
                break 
            counter +=1
        return is_palindrome