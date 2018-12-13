class Solution(object):
    def firstBadVersion(self, n):
        """
            :type n: int
            :rtype: int
            """
        
        first = 1
        end = n
        
        while first <= end:
            mid = (first + end) / 2
            
            if isBadVersion(mid):
                end = mid - 1
            else:
                first = mid + 1
        return first
