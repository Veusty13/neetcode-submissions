class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n : int = len(nums)
        mapper : Dict[int, Dict[str, int]] = {}
        for i in range(n) : 
            remain = target - nums[i]
            try :
                j = mapper[remain]["index"]
                return [j, i]
            except KeyError: 
                pass    
            mapper[nums[i]] = {
                "index" : i,
                "remain" : remain
            }
        return []