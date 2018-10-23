class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
            :type intervals: List[Interval]
            :rtype: int
            """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x.end)
        curr = -float('inf')
        count = 0
        for i in range(len(intervals)):
            if intervals[i].start < curr:
                count += 1
            else:
                curr = intervals[i].end
        return count
