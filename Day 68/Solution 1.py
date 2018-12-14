class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        x=Counter(nums)
        return x.most_common()[:-2:-1][0][0]
        """
            :type nums: List[int]
            :rtype: int
            """
