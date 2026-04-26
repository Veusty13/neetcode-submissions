"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [(interval.start, interval.end) for interval in intervals]
        intervals = sorted(intervals)
        n = len(intervals)
        if n <= 1 :
            return True
        prev = intervals[0]
        for i in range(1, n):
            if prev[1] > intervals[i][0]:
                return False
            else:
                prev = intervals[i]
        return True
