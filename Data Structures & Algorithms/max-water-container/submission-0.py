class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(set(heights)) == 1:
            return heights[0] * (len(heights) -1)
        n: int = len(heights)
        max_area: int = 0
        for i in range(n):
            for j in range(i+1, n):
                width: int = j - i
                height: int = min(heights[i], heights[j])
                area: int = height * width
                max_area = max(max_area, area)
        return max_area