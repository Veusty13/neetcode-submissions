class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n : int = len(nums)
        preffixes: List[int] = [1]*n
        suffixes: List[int] = [1]*n
        product_preffixes: int = 1
        product_suffixes: int = 1
        for i in range(1, n):
            product_preffixes *= nums[i-1]
            product_suffixes *= nums[n-i]
            preffixes[i] = product_preffixes
            suffixes[n-i-1] = product_suffixes
        return [p*s for p,s in zip(preffixes, suffixes)]


        
            