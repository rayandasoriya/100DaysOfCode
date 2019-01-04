from collections import Counter

class Solution:
    def findTargetSumWays(self, nums, S):
        """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """
        counter = Counter()
        counter[nums[0]] += 1
        counter[-nums[0]] += 1
        for num in nums[1:]:
            temp = Counter()
            for k, v in counter.items():
                temp[k-num] += v
                temp[k+num] += v
            counter = temp
        return counter[S]
