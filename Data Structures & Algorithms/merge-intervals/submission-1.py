class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals = sorted(intervals)
        queue = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= queue[-1][1] :
                queue[-1] = [queue[-1][0], max(intervals[i][1], queue[-1][1])]
            else:
                queue.append(intervals[i])
        return queue
        
