class Solution(object):
    def totalHammingDistance(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if not nums or len(nums) == 1:
            return 0
        
        n = len(nums)
        maxx = max(nums)
        ans = 0
        m = 1
        while m <= maxx:
            ones = 0
            for num in nums:
                if m & num:
                    ones += 1
            zeros = n - ones
            ans += ones * zeros
            m <<= 1
        return ans
