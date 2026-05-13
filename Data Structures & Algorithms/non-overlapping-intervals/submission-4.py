import functools
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        def is_intersect(previous_interval, current_interval):
            starting_previous = previous_interval[0]
            ending_previous = previous_interval[1]
            starting_current = current_interval[0]
            ending_current = current_interval[1]
            if ending_previous > starting_current:
                return True
            else:
                return False
        @functools.cache   
        def dfs(i,j, counter = 0): 
            if j == n: 
                return counter
            if j >= 1: 
                if not is_intersect(intervals[i], intervals[j]): 
                    return dfs(j, j+1, counter)
                else: 
                    return min(dfs(i, j+1, counter + 1), dfs(j,j +1, counter + 1))

        return dfs(0,1,0)
            


        
