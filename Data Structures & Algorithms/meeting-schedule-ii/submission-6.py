"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals = [(interval.start, interval.end) for interval in intervals]
        intervals = sorted(intervals)
        meetings_in_parallel = []
        max_nb_rooms = 0
        nb_rooms = 0
        for interval in intervals:
            for meeting in meetings_in_parallel:
                if meeting[1] <= interval[0]:
                    meetings_in_parallel.remove(meeting)
                    nb_rooms -= 1
            meetings_in_parallel.append(interval)
            nb_rooms += 1
            max_nb_rooms = max(max_nb_rooms, nb_rooms)
        return max_nb_rooms




