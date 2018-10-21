class Solution(object):
    def findMinDifference(self, timePoints):
        timePoints = sorted((60 * int(pt[:2])) + int(pt[3:]) for pt in timePoints)
        return min(min(b - a for (a, b) in zip(timePoints, timePoints[1:])), (24 * 60) + timePoints[0] - timePoints[-1])
