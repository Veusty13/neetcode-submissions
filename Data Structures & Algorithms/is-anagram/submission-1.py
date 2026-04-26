class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_as_list = [el for el in s]
        t_as_list = [el for el in t]
        s_as_list.sort()
        t_as_list.sort()
        if s_as_list == t_as_list :
            return True
        else :
            return False
        