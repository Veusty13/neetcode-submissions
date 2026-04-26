class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0
        while l < r:
            width = r - l
            if heights[l] <= heights[r]:
                small_height = heights[l]
                l += 1
            else :
                small_height = heights[r]
                r -= 1
            area = width * small_height
            max_area = max(max_area, area)
        return max_area