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
        bounds = set()
        for interval in intervals:
            bounds.add(interval[0])
            bounds.add(interval[1])
        bounds = sorted(list(bounds))
        synth_intervals = [(bounds[i], bounds[i+1]) for i in range(len(bounds) - 1)]
        max_nb_rooms = 0
        for synth_interval in synth_intervals:
            nb_rooms = 0
            for interval in intervals:
                if synth_interval[0] >= interval[0] and synth_interval[1] <= interval[1]:
                    nb_rooms +=1
            max_nb_rooms = max(max_nb_rooms, nb_rooms)
        return max_nb_rooms




