class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n <= 1 : 
            return False
        if n % 2 != 0:
            return False
        mapper = {
            "]" : "[",
            "}" : "{",
            ")" : "(" 
        }
        if s[0] in mapper:
            return False
        stack = []
        for i in range(n):
            if s[i] not in mapper:
                stack.append(s[i])
            else:
                if stack and (mapper[s[i]] == stack[-1]):
                    del stack[-1]
                else:
                    return False
        if stack:
            return False
        else :
            return True
                

