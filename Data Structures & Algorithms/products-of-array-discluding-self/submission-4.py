class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = 1, 1
        pref_list, suff_list = [1]*n, [1]*n
        for i in range(1, n):
            pref *= nums[i - 1]
            pref_list[i] = pref
        for i in range(n-2, -1, -1):
            suff *= nums[i + 1]
            suff_list[i] = suff
        return [p*s for p, s in zip(pref_list, suff_list)]