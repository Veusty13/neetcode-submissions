class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        full_product : int = 0
        full_product_skip_zero: int = 1
        partial_products : List[int] = []
        index_zeroes: List[int] = []
        output: List[int] = []
        for i in range(n):
            if nums[i] == 0:
                index_zeroes.append(i)
            if i == 0:
                full_product = nums[i]
                if nums[i] != 0:
                    full_product_skip_zero = nums[i]
            else:
                full_product *= nums[i]
                if nums[i] != 0:
                    full_product_skip_zero *= nums[i]
        if len(index_zeroes) == 0:
            output = [int(full_product/el) for el in nums]
        elif len(index_zeroes) >= 2:
            output = [0]*n
        else:
            output = [0]*n
            only_index_zero: int = index_zeroes[0]
            output[only_index_zero] = full_product_skip_zero
        return output
        

        
            