class Solution(object):
    def insert(self, intervals, newInterval):
        
        new_interval_list = []
        memo_start = newInterval.start
        memo_end = newInterval.end
        add = False
        added = False
        for interval in intervals:
            if not added and memo_end < interval.start:
                new_interval_list.append(Interval(memo_start, memo_end))
                added = True
            if interval.end < memo_start or interval.start > memo_end:
                if add and not added:
                    new_interval_list.append(Interval(memo_start, memo_end))
                    add = False
                    added = True
                new_interval_list.append(interval)
            else:
                add = True
                memo_start = min(memo_start, interval.start)
                memo_end = max(memo_end, interval.end)
        if add and not added:
            new_interval_list.append(Interval(memo_start, memo_end))
            add = False
            added = True
        if not added:
            new_interval_list.append(Interval(memo_start, memo_end))
        return new_interval_list
